#!/usr/bin/env python3
"""Run bounded checks and reject failed, modified, or stale receipts."""
import argparse, hashlib, json, os, subprocess, sys, time, uuid
from pathlib import Path

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def snapshot(inputs):
    result={}
    for value in inputs:
        p=Path(value)
        if p.is_symlink():
            result[str(p)]={'link':os.readlink(p),'target':digest(p) if p.is_file() else None}
        elif p.is_file():result[str(p)]=digest(p)
        elif p.is_dir():
            result[str(p)]='directory'
            for child in sorted(p.rglob('*')):
                if child.is_file() or child.is_symlink():result.update(snapshot([str(child)]))
        else:raise ValueError(f'Input missing: {p}')
    return result

def revision(cwd):
    r=subprocess.run(['git','rev-parse','HEAD'],cwd=cwd,capture_output=True,text=True)
    return r.stdout.strip() if r.returncode==0 else None

def run(args):
    cwd=Path(args.cwd).resolve(strict=True)
    inputs=[str((cwd/x).absolute()) for x in args.input]
    out=Path(args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    if any(out==Path(x) or Path(x) in out.parents for x in inputs):raise ValueError('Evidence output must be outside inputs')
    before=snapshot(inputs);head=revision(cwd)
    run_dir=out/str(uuid.uuid4());run_dir.mkdir(mode=0o700)
    log=run_dir/'output.log';command=args.command
    if command and command[0]=='--':command=command[1:]
    if not command:raise ValueError('A command is required after --')
    started=time.time();timeout=False
    with log.open('wb') as stream:
        try:
            # Kill the process group on timeout, not only the shell parent.
            p=subprocess.Popen(command,cwd=cwd,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=p.wait(timeout=args.timeout)
            except subprocess.TimeoutExpired:
                import signal
                if os.name == 'nt':
                    subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                    if p.poll() is None:p.kill()
                else:os.killpg(p.pid,signal.SIGKILL)
                p.wait();code=124;timeout=True
        except OSError as e:stream.write(str(e).encode());code=127
    try:after=snapshot(inputs)
    except ValueError:after=None
    receipt={'schema':1,'cwd':str(cwd),'command':command,'inputs':inputs,'before':before,'after':after,
             'head':head,'head_after':revision(cwd),'exit_code':code,'timed_out':timeout,
             'started_at':started,'duration_seconds':time.time()-started,'log':'output.log','log_sha256':digest(log)}
    path=run_dir/'receipt.json';path.write_text(json.dumps(receipt,indent=2))
    print(path)
    return 0 if code==0 and before==after and head==receipt['head_after'] else 1

def verify(path):
    path=Path(path).resolve();r=json.loads(path.read_text())
    if r.get('schema')!=1:raise ValueError('Unknown receipt schema')
    if r['exit_code']!=0 or r['timed_out']:raise ValueError('Check failed or timed out')
    if not r['inputs']:raise ValueError('No input scope')
    if r['before']!=r['after']:raise ValueError('Inputs changed during the check')
    if snapshot(r['inputs'])!=r['after']:raise ValueError('Receipt is stale: inputs changed')
    if r['head']!=r['head_after'] or revision(r['cwd'])!=r['head']:raise ValueError('Receipt is stale: revision changed')
    if r['log']!='output.log' or digest(path.parent/r['log'])!=r['log_sha256']:raise ValueError('Log missing or modified')
    print(json.dumps({'status':'passed','receipt':str(path),'scope':r['inputs'],'command':r['command']}))
    return 0

def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    p=sub.add_parser('run');p.add_argument('--cwd',required=True);p.add_argument('--input',action='append',required=True)
    p.add_argument('--output',required=True);p.add_argument('--timeout',type=float,default=300);p.add_argument('command',nargs=argparse.REMAINDER)
    p=sub.add_parser('verify');p.add_argument('receipt')
    args=parser.parse_args()
    try:return run(args) if args.action=='run' else verify(args.receipt)
    except (ValueError,OSError,KeyError,TypeError) as e:print('BLOCKED: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())

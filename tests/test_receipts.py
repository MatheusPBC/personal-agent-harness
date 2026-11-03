import unittest,tempfile,subprocess,sys,json
from pathlib import Path
SCRIPT=Path(__file__).resolve().parents[1]/'harness/skills/verify-work/scripts/check.py'
class ReceiptTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name);self.work=self.root/'work';self.work.mkdir();self.input=self.work/'input.txt';self.input.write_text('baseline')
 def runcheck(self,code,extra=None):
  args=[sys.executable,str(SCRIPT),'run','--cwd',str(self.work),'--input','input.txt','--output',str(self.root/'evidence'),*(extra or []),'--',sys.executable,'-c',code]
  r=subprocess.run(args,capture_output=True,text=True);self.receipt=Path(r.stdout.strip());return r
 def verify(self):return subprocess.run([sys.executable,str(SCRIPT),'verify',str(self.receipt)],capture_output=True,text=True)
 def test_success(self):
  self.assertEqual(self.runcheck('print("ok")').returncode,0);self.assertEqual(self.verify().returncode,0)
 def test_failed_command(self):
  self.assertNotEqual(self.runcheck('raise SystemExit(3)').returncode,0);self.assertNotEqual(self.verify().returncode,0)
 def test_stale_file(self):
  self.runcheck('print("ok")');self.input.write_text('changed');self.assertNotEqual(self.verify().returncode,0)
 def test_log_tampered(self):
  self.runcheck('print("ok")');(self.receipt.parent/'output.log').write_text('fake');self.assertNotEqual(self.verify().returncode,0)
 def test_input_modified_during_check(self):
  self.assertNotEqual(self.runcheck('from pathlib import Path;Path("input.txt").write_text("changed")').returncode,0);self.assertNotEqual(self.verify().returncode,0)
 def test_timeout(self):
  self.assertNotEqual(self.runcheck('import time;time.sleep(10)',['--timeout','0.05']).returncode,0);self.assertNotEqual(self.verify().returncode,0)
 def test_missing_command(self):
  r=subprocess.run([sys.executable,str(SCRIPT),'run','--cwd',str(self.work),'--input','input.txt','--output',str(self.root/'evidence'),'--','nonexistent-harness-fixture-command'],capture_output=True,text=True);self.assertNotEqual(r.returncode,0)
 def test_unrelated_input_not_claimed(self):
  self.runcheck('print("ok")');(self.work/'uncovered.txt').write_text('not covered');self.assertEqual(self.verify().returncode,0)
if __name__=='__main__':unittest.main()

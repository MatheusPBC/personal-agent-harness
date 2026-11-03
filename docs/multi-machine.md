# Mesmo núcleo em Linux, VPS e Windows

Rollout de 2026-11-03: sete skills centrais e regras compartilhadas instaladas
nos perfis usados pelo BB na VPS e no Windows. Ambos autenticaram no mesmo
servidor ai-memory 3.3.2 existente. Dados da wiki não foram copiados para novos
servidores. As demais skills e plugins locais foram preservados.

## Adaptações

- Linux: links simbólicos para regras e skills pessoais.
- Windows: hard links para AGENTS.md/CLAUDE.md e junctions para skills do Claude.
  Substituir atomicamente um arquivo quebra a associação do hard link; ao promover
  uma nova versão, recrie os links. Não há sincronização automática entre máquinas.
- Windows: atalhos .cmd em ~/.local/bin, acrescentado ao PATH do usuário para novos
  processos. O runner encerra a árvore do processo por taskkill em timeouts.
- VPS/Windows: MCP do Codex usa bridge nativo sem sessão e credencial privada em
  disco; continua exigindo workspace/project explícitos nas ferramentas.
  Claude usa o bridge com sessão. O transporte do Codex local original era HTTP.
- Captura em allowlist, backfill automático desligado e hooks Codex habilitados
  e confiáveis. Configurações existentes foram preservadas pelos instaladores,
  com backups locais dos arquivos substituídos. Credenciais não estão neste repo.

## Verificação

Nos dois destinos: identidade autenticada do servidor, descoberta nativa de
skills Codex e Claude, sete hooks Codex trusted, política dos hooks de ambos
os agentes e oito testes do runner. Não houve turno de modelo no teste de
Claude nem captura de histórico sintético no servidor real.

Abra novas sessões para carregar regras/configurações. No Windows, processos
já abertos podem manter o PATH antigo. Uma sessão completa real continua sendo
a verificação final de captura e continuidade; estes checks não a substituem.

O perfil secundário codex-agent da VPS não foi alterado: o BB inspecionado roda
como root. Para outros usuários da mesma máquina, aplique o núcleo ao perfil
correto, mantendo credenciais e permissões próprias.

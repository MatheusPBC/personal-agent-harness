# Arquitetura e decisões

## Separação de responsabilidades

O agente interpreta o pedido e escolhe ferramentas. As regras compartilhadas
estabelecem limites; o projeto fornece contexto específico; skills oferecem
procedimentos. Testes e ferramentas verificam comportamentos observáveis.
A memória preserva contexto atribuído, cuja atualidade precisa ser revalidada.

## Estrutura instalada

```text
~/.agents/
  AGENTS.md                 fonte global compartilhada
  CATALOG.md                índice de capacidades
  skills/                   skills ativas; playbooks dentro de SKILL.md
  skill-library/            especializações consultadas sob demanda
~/.codex/
  AGENTS.md                 link para a fonte compartilhada
  config.toml               MCP HTTP e confiança de hooks
  hooks.json                lifecycle e ferramentas
  skills/.system/           skills nativas preservadas
~/.claude/
  CLAUDE.md                 link para a fonte compartilhada
  skills/                   links para as skills pessoais
  settings.json             hooks
~/.claude.json              MCP bridge com identidade de sessão
~/.local/bin/
  ai-memory                 cliente nativo
  harness-check             link para o runner verify-work
~/.local/share/ai-memory/   configuração e credenciais locais protegidas
projeto/
  AGENTS.md                 instruções específicas
  .ai-memory.toml           workspace/projeto
  código e testes           comportamento do produto
VPS/
  ai-memory                 serviço, wiki, sessões e handoffs
```

## Por que assim?

- **Uma fonte para dois agentes:** reduz divergência entre regras de Codex e Claude.
- **Global curto, projeto específico:** arquitetura de um produto não vira regra universal.
- **Skills sob demanda:** evita carregar uma biblioteca inteira em cada tarefa.
- **Playbooks dentro das skills:** mantém procedimento e gatilho de descoberta juntos.
- **Captura com marcador:** reduz mistura de projetos. O agente resolve a ausência
  do marcador ao iniciar trabalho; o hook apenas aplica a política configurada.
- **Identidade por projeto, não branch:** worktrees compartilham conhecimento relevante.
- **Memória separada de evidência atual:** uma decisão histórica pode estar desatualizada.
- **Recibos delimitados:** vinculam uma execução a inputs e revisão específicos.
- **Sem processo universal:** planejamento formal, TDD, worktrees e delegação são
  escolhidos conforme projeto e autorização, não impostos a toda tarefa.

Plugins dos runtimes continuam independentes. Este repositório não empacota
nem reivindica autoria dessas extensões. As sete skills aqui são o núcleo
pessoal; outras capacidades permanecem no catálogo instalado.

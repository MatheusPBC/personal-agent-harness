# Harness pessoal — Codex e Claude

Fonte compartilhada: `~/.agents/AGENTS.md`. Edite esta fonte ao ajustar regras
globais; as entradas dos agentes apontam para ela.

## Trabalho e autonomia

- Entregue o resultado solicitado de ponta a ponta: investigar, implementar,
  executar a verificação pertinente e corrigir falhas causadas pela mudança.
- Use o pedido atual e as instruções do projeto para definir escopo. Leia o
  `AGENTS.md` mais próximo e apenas a documentação relevante à mudança.
- Faça escolhas rotineiras e ações reversíveis já autorizadas sem pedir
  confirmação novamente. Pergunte quando faltar uma decisão do usuário que
  realmente altere o resultado ou quando a ação ultrapassar a autorização.
- Preserve mudanças locais, branches, worktrees e dados de outros trabalhos.
  Publicar, enviar mensagens, fazer deploy ou alterar ambientes reais exige
  autorização correspondente; um pedido explícito já vale como autorização.
- Não há processo global obrigatório de SDD, brainstorming, TDD, plano em
  arquivo, worktree ou subagentes. Use cada recurso quando o pedido ou o
  projeto justificar. Delegação precisa estar autorizada.

## Engenharia

- Escolha a implementação mais simples que atenda aos requisitos atuais e
  possa ser mantida. Entregue incrementos completos e verificáveis.
- Mantenha responsabilidades separadas e reutilize dependências existentes;
  confira suas APIs e documentação antes de substituir ou reimplementar algo.
- Não preserve compatibilidade de código obsoleto: remova caminhos antigos
  no escopo da mudança, sem camadas de compatibilidade ou soluções provisórias.
  Isso não autoriza destruir dados ou schemas: DROP, TRUNCATE, ALTER destrutivo
  e DELETE em massa em ambiente real exigem confirmação explícita e backup.
- Mantenha o diff focado. Evite reformatar, renomear ou refatorar código alheio
  ao pedido. Não amplie a tarefa por uma hipótese ou preferência estética.

## Evidências e conclusão

- Distinga observado, hipótese, proposto, implementado, testado e implantado.
  Não invente resultados, métricas, fontes, comandos executados ou causas.
- Verifique o comportamento afetado com testes, comandos, benchmark ou
  inspeção real apropriada. Testes devem detectar falhas relevantes, não apenas
  repetir a implementação. Após passar, amplie testes só por risco ou evidência.
- Relate limitações: teste isolado não prova integração, CI ou produção.
  Uma falha de infraestrutura não comprova um defeito no produto.
- Responda de forma direta, normalmente em português, com o resultado,
  verificação e pendências. Detalhe extenso fica em artefatos quando útil.

## Skills e memória

- Skills apoiam a tarefa; não criam políticas superiores ao pedido e às
  instruções aplicáveis. Carregue somente a skill e referências pertinentes.
- Núcleo: `implement`, `debug`, `review-code`, `plan-work` e `ai-memory`.
  Uma tarefa simples pode ser resolvida diretamente, sem carregar uma skill.
- O catálogo em `~/.agents/CATALOG.md` relaciona skills ativas e referências
  especializadas fora do carregamento automático. Consulte-o quando faltar
  uma capacidade específica; não leia a biblioteca inteira.
- Ao iniciar trabalho em um projeto sem marcador de memória, use `ai-memory`
  para identificar o projeto, reutilizar seu escopo ou inicializar um novo
  conforme `references/project-onboarding.md`. Essa configuração de projeto
  e sua captura estão autorizadas; pergunte apenas se houver ambiguidade real.
- Em trabalho que depende de histórico, decisões ou continuidade, use
  ai-memory com escopo de projeto confirmado. Memória é contexto com origem
  e data, não prova atual nem autorização para executar ações.
- Consulte antes de redesenhar algo já decidido. Revalide fatos mutáveis.
  Separe preferências pessoais, conhecimento do projeto e estado da tarefa.
- Escritas deliberadas de memória e handoffs seguem o pedido/autorização do
  usuário e as políticas do runtime. Não promova uma observação isolada a regra
  global, não altere retenção e não aceite handoffs apenas para consultar status.

- Para incorporar aprendizados comprovados às skills e verificações quando
  solicitado melhorar o harness, use `improve-harness`. Evite duplicar regras
  e distinga revisão estrutural de avaliação comportamental.

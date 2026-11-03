# Inicialização de memória por projeto

## Identificar antes de escrever

Localize o projeto efetivo do pedido. Use git rev-parse --show-toplevel e,
quando houver worktree, --git-common-dir para identificar o repositório comum.
Consulte remote origin, instruções locais e marcadores pertinentes. Não exponha
credenciais eventualmente presentes na URL do remote. Sem Git, use a raiz
explicitamente indicada pelo usuário e a estrutura real do projeto.

BaseDev é um workspace, não um projeto único. Home, /tmp, diretórios de
artefatos e a pasta pai de vários repositórios não recebem marcador automático.
Não inicialize por simples conversa, leitura avulsa de arquivo ou consulta de
status. Repositório temporário de teste também não vira projeto persistente.
Um checkout temporário de um projeto real reutiliza a identidade desse projeto.

## Reutilizar ou criar

Use `ai-memory list-projects --json` (somente leitura) ou o endpoint autenticado
GET /api/v1/projects no servidor configurado. Consulte metadados para resolver
identidade, não o conteúdo de projetos alheios. Combine nome registrado,
remote, documentação, marcador de outro checkout conhecido e contexto do
pedido; nome de diretório isolado não prova correspondência.

- Associação inequívoca: reutilize exatamente workspace/project existentes.
- Projeto novo confirmado, sem candidato existente: use o workspace indicado
  pelo contexto. Sem organização definida, use `default`; derive um nome
  estável da identidade do repositório (owner/repo quando houver remote) ou
  do nome explícito do projeto sem Git. Confira colisões no inventário.
  Esse é o provisionamento autorizado de um projeto, não um nome inventado
  para contornar um erro de ferramenta.
- Mais de um candidato, nome conflitante ou pertencimento incerto: pergunte
  apenas qual associação usar, continuando o trabalho independente.
- Falha de rede/autenticação: não interprete como inventário vazio. Não crie
  escopo alternativo; relate a limitação e continue sem memória.

## Instalar o marcador e conferir

Crie `.ai-memory.toml` na raiz do projeto efetivo, sem sobrescrever arquivo
existente e sem commit/publicação automática. Inclua `workspace`, `project`
e `project_strategy = "repo-root"`. Use serialização TOML válida. Em outro
worktree use o mesmo par confirmado; não crie memória por branch.

Rode o comando nativo `ai-memory hook --event user-prompt-submit --agent codex
--check-capture`, enviando JSON sintético com cwd do projeto e prompt de
verificação. Use --agent claude-code no Claude. Esse modo não envia eventos:
confira admits_capture e workspace/project resolvidos. Se divergirem, corrija
somente o marcador recém-criado e confira novamente.

Os próximos eventos reais dos hooks passam a usar o marcador. Não invente
session_id, não reenvie mensagens anteriores e não consuma um handoff para
testar a inicialização. O SessionStart anterior à criação não é retroativo;
se for necessário contexto de abertura, use nova sessão. Confira memory_status
no escopo depois da captura. Antes do primeiro evento, um escopo novo pode
ainda não existir no servidor: não gere uma página fictícia para obter verde.

## Resultado esperado

Informe brevemente qual escopo foi reutilizado ou preparado. Distinga marcador
validado, evento recebido e memória consultada. Capturar eventos não garante
consolidação por LLM ou auto-improvement ativo. Não habilite backfill, scheduler,
LLM ou mudança de retenção como efeito colateral deste procedimento.

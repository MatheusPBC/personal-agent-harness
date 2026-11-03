# Estado e evidências

Snapshot de 2026-11-03. Resultados desta construção; não são garantias permanentes.

| Item | Verificação realizada | Limite |
|---|---|---|
| Regras e skills compartilhadas | Links e descoberta nativa Codex/Claude | Não mede qualidade de cada skill |
| verify-work | Oito testes de execução e rejeição de recibos | Não prova cobertura do produto |
| Hooks | Quinze checks em servidor local isolado; confiança dos sete hooks Codex | Não é sessão completa real dos dois agentes |
| Servidor 3.3.2 | Container saudável, identidade autenticada, MCP e inventário | Não valida todas as capacidades upstream |
| Histórico existente | Cinco projetos e contagens de páginas preservadas após upgrade | Não é comparação integral de todo conteúdo |
| Onboarding | Seis checks nativos: dois agentes × sem marcador/existente/novo | Decisão semântica do agente ainda não avaliada ponta a ponta |
| improve-harness | Descoberta, links e revisão estrutural | Comparação comportamental ainda pendente |
| Auto-improvement com LLM | Documentado conforme upstream | Ativação efetiva não confirmada |

Os testes reproduzíveis incluídos aqui cobrem o runner. Os testes da integração
foram executados em fixtures locais durante a construção; seus diretórios com
logs e dados não foram publicados neste repo.

## Próximas verificações úteis

- Observar uma tarefa real num projeto novo: inventário, marcador e primeiro evento.
- Retomar o mesmo projeto pelo outro agente sem duplicar escopo ou handoff.
- Avaliar a skill de melhoria no caso original, numa variação e numa exceção.
- Inspecionar política/configuração do LLM antes de afirmar aprendizado autônomo ativo.

## Rollback

Alterações globais tiveram backups locais. O upgrade da VPS preservou container
e volume antigos e um arquivo consistente dos dados. Esses caminhos e backups
privados não são publicados aqui. Após novas escritas, voltar ao snapshot antigo
pode perder atividades posteriores; planeje reconciliação antes de rollback.

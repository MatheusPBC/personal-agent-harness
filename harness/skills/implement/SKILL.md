---
name: implement
description: Implemente uma funcionalidade ou refatoração solicitada, com mudança executável e verificação do comportamento afetado.
---

# Implementação

Entregue código funcionando no ambiente autorizado. O pedido de implementação
já autoriza as edições necessárias dentro do escopo; não o converta em um guia
para copiar e colar nem crie uma etapa de aprovação de plano por padrão.

## Decisões que importam

- Identifique o comportamento esperado, o ponto de integração e o dono dos
  dados. Leia instruções locais, estado do checkout e os caminhos envolvidos.
- Recupere decisões relevantes no ai-memory quando houver histórico. Confirme
  no código os fatos dos quais a mudança depende.
- Use padrões e dependências já presentes. Entregue a menor fatia completa,
  incluindo os consumidores necessários. Remova o caminho obsoleto no escopo.
- Se uma decisão de produto estiver ausente, avance no trabalho independente
  e peça apenas essa decisão. Não pergunte sobre fatos disponíveis no projeto.
- Regras de worktree, documentos, release e testes pertencem ao repositório.
  Não imponha um framework de processo a todos os projetos.

## Evidência para encerrar

Execute as verificações adequadas ao contrato alterado e examine o resultado.
Corrija falhas introduzidas pela mudança. Para comportamento visível, exercite
o fluxo quando o ambiente permitir; compilação não comprova interação.

Informe o que mudou, o que foi executado e o que permanece bloqueado ou não
verificado. Publicação ou deploy só entram quando fazem parte da autorização.

## Evidência reutilizável

Quando precisar de verificação reproduzível ou handoff verificável, use
`verify-work` para executar o check do projeto e validar seu recibo contra
os arquivos atuais. Inclua implementação, testes e configuração afetados
no escopo; recibo verde não substitui a escolha de um bom teste.

## Aprendizados recorrentes

Se a tarefa revelar uma falha reutilizável no procedimento, identifique a
origem e a skill responsável. Quando o pedido incluir melhorar o harness ou
evitar recorrência, aplique `improve-harness`; caso contrário, sinalize a lição
sem ampliar a tarefa ou alterar regras globais automaticamente.

---
name: debug
description: Investigue um bug, falha intermitente ou regressão e, quando solicitado, corrija sua causa com evidências.
---

# Diagnóstico

Defina esperado versus observado, ambiente, versão e entrada. Use uma
reprodução pequena quando possível; se o ambiente não permitir reproduzir,
registre isso e use logs ou artefatos para restringir as hipóteses.

- Consulte histórico relevante no ai-memory e confirme se descreve a mesma
  versão e sintoma. Uma tentativa anterior é evidência a examinar.
- Escolha o próximo experimento pela hipótese que ele distingue. Preserve
  saída original, janela temporal e correlação. Não altere várias causas
  candidatas ao mesmo tempo.
- Em divergências local/produção, confira o caminho de execução real, versões,
  configurações e integrações antes de chamar o código local de causa.
- Revisão e diagnóstico são somente leitura por padrão. Corrija quando o
  pedido incluir correção. A investigação não autoriza reinícios ou deploy.
- Para uma regressão reproduzível, busque um teste que falhe sem a correção e
  passe com ela, em checkout isolado quando necessário. Não reverta trabalho
  alheio para produzir a comparação. Se só houver evidência parcial, diga isso.

Conclua com causa demonstrada ou hipóteses ainda abertas, correção se feita,
verificações executadas e o próximo experimento se houver bloqueio.

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

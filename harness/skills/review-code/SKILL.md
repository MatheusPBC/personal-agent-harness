---
name: review-code
description: Revise um diff, commit ou pull request buscando defeitos verificáveis e regressões, sem alterar código ou publicar comentários.
---

# Revisão de código

Fixe a base e o head da revisão. Leia instruções locais, diff e contexto dos
consumidores necessários para avaliar o comportamento. Preserve o checkout.

- Priorize correção, autorização, integridade de dados, concorrência, erros e
  compatibilidade dos consumidores atuais. Estilo só é achado quando viola
  um requisito aplicável ou causa problema concreto.
- Para cada achado, mostre o gatilho, impacto, arquivo/linha e evidência.
  Diferencie defeito demonstrado, risco condicionado e dúvida não resolvida.
- Examine o que os testes realmente cobrem. Execute verificações focadas e
  isoladas quando ajudarem a confirmar um achado; não execute produção.
- Confira o caminho de build/deploy antes de transformar uma discrepância no
  código em afirmação sobre runtime. Separe checks locais de CI observada.
- Uma descrição do autor ou de outro agente não substitui diff e artefatos.

Retorne achados por impacto e limites da revisão. Se não houver achados,
declare o escopo examinado, sem afirmar ausência universal de defeitos.
Corrigir código, comentar no GitHub e aprovar/mesclar PR são ações separadas
que precisam estar incluídas no pedido.

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

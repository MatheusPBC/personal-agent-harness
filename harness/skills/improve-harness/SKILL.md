---
name: improve-harness
description: Incorpore uma correção do usuário ou aprendizado comprovado em skills, playbooks e verificações, quando solicitado melhorar o harness ou evitar uma recorrência.
---

# Melhorar com evidência

Transforme uma experiência concreta em uma mudança pequena no procedimento
responsável. O resultado é o arquivo ou check corrigido, sua verificação e os
limites conhecidos; não apenas uma nota de memória ou proposta abstrata.

## Encontrar a mudança certa

1. Identifique o episódio: pedido, comportamento esperado, ação observada,
   consequência e evidência. Consulte histórico relevante sem assumir que
   uma hipótese ou recomendação recuperada já foi validada.
2. Confira a fonte efetiva carregada pelo agente. Se a regra já existe,
   investigue descoberta, ambiguidade, conflito ou falta de verificação;
   não acrescente uma duplicata mais enfática.
3. Escolha o menor escopo: fato de produto na memória/docs do projeto;
   procedimento repetível na skill responsável; invariantes gerais no
   AGENTS.md somente se realmente transversais. Crie uma nova skill apenas
   se nenhuma existente for responsável pela capacidade.
4. Se a falha puder ser detectada mecanicamente, prefira um teste ou check
   no caminho de execução existente. Texto complementa a verificação.
   Para julgamento contextual, preserve critérios e exceções no playbook.

## Verificar antes de chamar de melhoria

Defina o que distinguiria a versão anterior da candidata antes de avaliá-la.
Inclua o episódio original, uma variação relevante e um caso em que a nova
regra NÃO deve se aplicar. Critérios devem observar ações ou resultados,
não contar palavras-chave nem premiar seguir um formato.

Para scripts, rode casos negativos e positivos; use verify-work quando um
recibo reutilizável ajudar. Para instruções, reproduza os casos em sessões
isoladas quando houver autorização e ferramenta adequada, com mesmos inputs,
ferramentas e modelo. Não dispare subagentes sem autorização. Se houver apenas
inspeção do texto e descoberta, declare a mudança implementada e a avaliação
comportamental pendente; não invente um ganho de qualidade.

## Aplicar e fechar o ciclo

Preserve versão anterior ou diff recuperável. Edite a fonte compartilhada,
remova a regra substituída e confira referências, links e descoberta pelos
agentes afetados. Em erro de sintaxe ou regressão demonstrada, corrija ou
restaure somente a mudança desta tarefa.

Registre junto às evidências da tarefa: episódio/origem, arquivo responsável,
antes/depois, casos e critérios, observado versus não testado e caminho de
rollback. Use thread storage ou artefato do projeto; não crie uma segunda
base global de memórias. Escrita no ai-memory segue autorização de persistência.

O pedido de melhorar o harness autoriza as edições pertinentes desta tarefa;
não significa autorização permanente para reescrever regras em qualquer chat.
Durante trabalho comum, conclua o objetivo e sinalize uma lição candidata
quando houver evidência útil. Não crie um ritual de retrospectiva obrigatório.

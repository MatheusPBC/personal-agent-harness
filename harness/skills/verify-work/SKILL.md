---
name: verify-work
description: Execute uma verificação técnica com recibo e confira se o resultado ainda corresponde aos arquivos e à revisão avaliados.
---

# Verificação com recibo

Para mudanças técnicas relevantes, use o runner quando precisar de evidência
reutilizável ou handoff verificável. O comando de verificação vem do projeto e
do comportamento alterado; esta skill não escolhe testes por palavra-chave.

Execute `harness-check run --cwd CAMINHO --input ARQUIVO_OU_PASTA --output
DIRETORIO_DE_EVIDENCIAS -- COMANDO ARGUMENTOS`. Repita `--input` para incluir
implementação, testes e configuração necessários ao resultado. A saída fica
fora dos inputs, por exemplo em `$BB_THREAD_STORAGE/evidence` ou `/tmp`.

O runner executa sem shell implícito, registra stdout/stderr, código de saída,
comando, revisão Git e hashes dos inputs antes/depois. Não inclua segredos nos
argumentos ou saídas. Só execute comandos autorizados para aquele ambiente.
Para pipelines, use um script revisado ou shell explícito.

Antes de afirmar que essa verificação passou no estado atual, execute
`harness-check verify CAMINHO_DO_RECIBO`. Falha, timeout, revisão diferente,
input alterado ou log adulterado retornam código não zero. Corrija o problema
ou rode uma nova verificação; não edite o recibo para torná-lo verde.

Isso verifica a execução e atualidade da evidência delimitada. Não demonstra
que o teste cobre todo o produto, não certifica produção e não é atestação
contra um agente que falsifique recibos. Declare o escopo e verificações que
faltam. Revisão sem execução pode usar evidências estáticas, identificadas como
tais; conversa, planejamento e edição textual trivial não exigem recibo.

No ai-memory, quando autorizado, referencie recibo, resultado e revisão. Não
copie logs extensos para a memória nem promova `passed` a `deployed`.

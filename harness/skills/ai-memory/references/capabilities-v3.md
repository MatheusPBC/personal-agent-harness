# Capacidades e uso — ai-memory 3.x

Verificado contra tools/list do servidor 3.3.2 em 2026-11-03.
Fonte: https://github.com/akitaonrails/ai-memory/tree/v3.3.2/docs
Revalide schemas e disponibilidade após upgrades; não carregue toda a documentação.

## Atualizar parte de uma página

Quando a escrita estiver autorizada, prefira `memory_patch_page` para mudanças
localizadas. Leia primeiro com `memory_read_page` e use o `expected_page_id`
retornado. Para `replace_section`, use também o `section_sha256` exato da
leitura e um heading inequívoco. O lote inteiro usa a mesma versão base.
Se houver conflito, releia e reavalie a mudança; não force a versão antiga.
`append` exige target section com âncora, ou end_of_page sem âncora.
`add_section` usa heading ATX único de nível 2 a 6. Metadados são preservados.
Não substitua uma página inteira por um fragmento como fallback.

## Restaurar uma página

Use `memory_restore_page` apenas quando houver pedido de desfazer/restaurar.
Sem `rev`, lista checkpoints; com `rev`, grava a versão escolhida como nova
versão atual. Confira o conteúdo/escopo que será restaurado: pode trazer de
volta material excluído. Exige acesso administrativo e não restaura perfil.
Clientes estáticos passam workspace e project juntos nas duas ferramentas.

## Outras capacidades e limites

- `memory_briefing` fornece estado estruturado sem LLM; `memory_explore`
  produz interpretação com LLM. Observações são a origem para verificar resumos.
- Inbox: `memory_message_list` consulta sem consumir; pop consome. Envio de
  mensagem para outro projeto exige instrução explícita, não só ferramenta disponível.
- Workstreams gerenciados requerem lançamento via `ai-memory run`; instalar
  hooks não transforma sessões BB/Codex/Claude existentes em managed sessions.
  Não substitua o launcher do usuário automaticamente.
- Perfil compartilhado separa preferências pessoais de conhecimento de projeto.
  Não promova fatos locais a preferências globais nem habilite busca global por padrão.
- Consolidação e auto-improvement dependem do LLM/configuração e podem escrever.
  Confira política de aprovação e scheduler antes de ativar; disponibilidade
  no catálogo não comprova que o recurso esteja configurado ou autorizado.
- Retenção pode apagar páginas; o schema/descrição atual governa os passes.
  Não reutilize a descrição de um cliente antigo para planejar limpeza.

## Documentação da versão instalada

O servidor oferece referências autenticadas somente leitura em
GET /api/v1/docs, /api/v1/docs/features, /api/v1/docs/features/status e
/api/v1/docs/changelog?release=3.3.2. Use o transporte configurado sem expor
credenciais. Documentação descreve capacidade; status/configuração e execução
verificada demonstram disponibilidade real. Não execute exemplos automaticamente.

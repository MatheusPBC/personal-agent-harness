# Fontes e atribuição

Consultadas durante a construção em 2026-11-03. A arquitetura deste repo é uma
adaptação pessoal, não uma distribuição oficial de OpenAI, Anthropic ou Akita.

## OpenAI

[A model guide for the GPT-6 family](https://openai.com/index/practical-guide-building-gpt-6/)
orientou instruções consistentes, contexto sob demanda, critérios de conclusão
e limites claros de autonomia. Não é fonte da implementação do ai-memory.

## Akita: arquitetura orientada ao uso

[Creating a Framework for AI with AI — REA Launcher SDK](https://akitaonrails.com/en/2026/11/02/creating-a-framework-for-ai-with-ai-rea-launcher-sdk/)
mostra experiências de projetos virando padrões, playbooks e verificações.
O artigo trata da evolução do SDK; não atribui esse ciclo ao auto-improvement
do ai-memory. A distinção importa para não prometer reescrita automática de skills.

[REA Launcher SDK](https://github.com/akitaonrails/rea-launcher-sdk): referência
para entrada por AGENTS.md, playbooks e padrões. Não copiamos o processo de
engenharia reversa nem suas fases como obrigação global.

## ai-memory — versão consultada 3.3.2

- [Release](https://github.com/akitaonrails/ai-memory/releases/tag/v3.3.2)
- [Recursos](https://github.com/akitaonrails/ai-memory/blob/v3.3.2/docs/features.md)
- [Marcadores e roteamento](https://github.com/akitaonrails/ai-memory/blob/v3.3.2/docs/marker-file.md)
- [Auto-improvement](https://github.com/akitaonrails/ai-memory/blob/v3.3.2/docs/auto-improvement-loop.md)
- [Gates de avaliação](https://github.com/akitaonrails/ai-memory/blob/v3.3.2/docs/auto-improve-eval-gates.md)
- [Workstreams gerenciados](https://github.com/akitaonrails/ai-memory/blob/v3.3.2/docs/managed-workstreams.md)
- [Migração para 3.x](https://github.com/akitaonrails/ai-memory/blob/v3.3.2/docs/upgrading-to-3.0.md)

Os schemas reais de tools/list e as respostas da instalação foram usados para
conferir disponibilidade. Documentação não prova configuração ativa.

## Escolhas locais

Fonte compartilhada em ~/.agents, seleção das skills centrais, allowlist de
captura, onboarding pelo agente, importação histórica automática desligada,
runner verify-work e procedimento improve-harness são escolhas desta montagem.
Não devem ser atribuídas como defaults universais dos produtos citados.

Somente o núcleo pessoal foi incluído. Bibliotecas e plugins externos continuam
sob seus próprios projetos/licenças; não foram redistribuídos neste snapshot.

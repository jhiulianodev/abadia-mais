# Abadia Mais — CONTINUAR DAQUI

Protótipo do novo site e do aplicativo da Prefeitura de Abadia de Goiás.
Feito em 24/11/2026 para apresentação. **Todos os dados e nomes são fictícios.**

## O que está pronto

- **App web para celular** (`index.html`): 23 telas ligadas entre si, publicado no GitHub Pages e instalável na tela inicial (`manifest.json` + ícones).
- **PDFs de apresentação**: `Abadia-Mais-Site.pdf` (12 páginas) e `Abadia-Mais-Aplicativo.pdf` (28 telas + Painel da Farmácia). Ficam guardados fora do repositório.
- **Logo**: ícone com o desenho da bandeira de Abadia (fundo branco, triângulos que se encontram no círculo central) e o "A+" no centro. Versão oficial em azul, com o "+" em vermelho. SVGs em `fonte/logo/`.

## Identidade visual (versão final)

| Uso | Cor |
|---|---|
| Azul principal (botões) | `#005A8E` |
| Azul do logo / site atual | `#0572A7` |
| Azul-marinho (textos, rodapé) | `#0B2540` |
| Azul claro (fundos) | `#EEF5FA` |
| Vermelho (só o "+" do logo) | `#E11D24` |
| Verde (confirmar, sucesso) | `#1B7A43` |
| Amarelo (avisos, ajuda) | `#FFF6DC` / `#FFC83D` |

- Fontes: **Atkinson Hyperlegible** (texto, feita para baixa visão) e **Poppins** (títulos).
- Acessibilidade: texto de 18px para cima, botões com 56–64px de altura, alto contraste, foco amarelo visível, ajuda por WhatsApp e telefone sempre à vista.

## Telas do app

| # | Tela | Arquivo |
|---|---|---|
| 01 | Abertura | AppAbertura |
| 02 | Entrar (gov.br ou CPF + SMS) | AppLogin |
| 03 | Seus dados (preenchidos pelo gov.br ou à mão) | AppCadastro |
| 04 | Início | AppInicio |
| 05–10 | Consulta: tipo → UBS → médico → calendário → confirmar → marcada | AppConsulta* |
| 11–13 | Meus agendamentos, detalhe, outros agendamentos | AppMeusAgendamentos, AppAgendamentoDetalhe, AppOutrosAgendamentos |
| 14–17 | Remédio: receita → paciente → retirar ou receber em casa → confirmar | AppRemedio* |
| 18 | Situação do pedido (Verificando → Aprovada → Aguardando retirada / Aguardando coleta → Saiu para entrega → Entregue) | AppStatusRemedio |
| 19–20 | Meus remédios, Receita recusada | AppMeusPedidos, AppReceitaRecusada |
| 21–23 | Avisos, Perfil e acessibilidade, Ajuda | AppNotificacoes, AppPerfil, AppAjuda |

Telas interativas: calendário, paciente, retirada/entrega e situação do pedido (com o botão "Simular próxima etapa").
Fora do app, só nos PDFs: site (página inicial, agendamento, remédio) e Painel da Farmácia.

## Pendências (dados reais que faltam)

- Nomes e endereços reais das UBS (hoje aparecem como "UBS Unidade 1/2/3" e [Endereço]).
- Endereço e horário da Farmácia Municipal, do CRAS e da Junta Militar.
- Médicos reais e os dias em que atendem (hoje são exemplos inventados).
- Validação da assinatura da receita: ficou para uma fase 2. Por enquanto o farmacêutico confere numa lista de checagem.
- Vapt Vupt é do Governo de Goiás: para agendar de verdade, o app precisa se ligar ao sistema do Estado.

## Próximos passos possíveis

1. Colocar os dados reais e gerar o app e os PDFs de novo.
2. Fazer os dados digitados passarem de uma tela para a outra (hoje cada tela mostra dados fixos).
3. Versão real: um servidor com login gov.br, agenda das UBS, fila da farmácia e avisos por WhatsApp.

## Como os arquivos foram feitos (para continuar com o Claude)

- `fonte/telas/*.dc.html`: cada tela no formato do quadro de design do Claude.
- `fonte/scripts/base.py` + `s1.py`, `s2.py`, `s3.py`: geram as telas do app (`python3 s1.py` etc., grava em `/home/claude/canvas/project`).
- `fonte/scripts/build.py`: junta as telas num `index.html` só, com um mini-motor que faz as telas funcionarem fora do Claude. O logo entra embutido no próprio arquivo.
- `fonte/scripts/pdf.py`: gera os dois PDFs com o Chrome sem tela (Playwright).
- `fonte/logo/*.svg`: logo em vetor (ia = ícone azul, iai = ícone invertido, lh = logo horizontal, lhb = logo horizontal para fundo escuro).

Para continuar numa conversa nova, envie este arquivo e a pasta `fonte/` ao Claude e diga o que quer mudar.

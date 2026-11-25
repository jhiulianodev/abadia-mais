import base64, os
from playwright.sync_api import sync_playwright
OUT = '/home/claude/out'; SH = OUT + '/shots'; os.makedirs(SH, exist_ok=True)
U = 'file:///home/claude/out/all.html'
L = '/home/claude/logo'
def b64(p): return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

APP = [
 ('AppAbertura', None, '01 · Abertura', 'Entrada do aplicativo com o logo Abadia Mais.'),
 ('AppLogin', None, '02 · Entrar', 'Entrar com gov.br ou com CPF e código por SMS.'),
 ('AppCadastro', None, '03 · Seus dados', 'Dados preenchidos pelo gov.br, com opção de preencher à mão.'),
 ('AppInicio', None, '04 · Início', 'Próxima consulta, situação do remédio e atalhos grandes.'),
 ('AppConsultaTipo', None, '05 · Tipo de consulta', 'Clínico, pediatria, dentista, ginecologia, enfermagem, psicologia.'),
 ('AppConsultaUBS', None, '06 · Posto de saúde', 'Distância, horário e médicos disponíveis em cada UBS.'),
 ('AppConsultaMedico', None, '07 · Médico', 'Dias de atendimento e próxima vaga de cada médico.'),
 ('AppConsultaCalendario', {'day': 2, 'time': 2}, '08 · Calendário', 'Dias com vaga, poucas vagas ou lotados, e horários livres.'),
 ('AppConsultaConfirmar', None, '09 · Confirmar', 'Resumo, motivo da consulta e lembrete no WhatsApp.'),
 ('AppConsultaPronto', None, '10 · Consulta marcada', 'Protocolo e comprovante no WhatsApp.'),
 ('AppMeusAgendamentos', None, '11 · Meus agendamentos', 'Próximos e anteriores, com a situação de cada um.'),
 ('AppAgendamentoDetalhe', None, '12 · Detalhe', 'Código para a recepção, remarcar ou cancelar.'),
 ('AppOutrosAgendamentos', None, '13 · Outros agendamentos', 'Identidade, Vapt Vupt, Junta Militar, CRAS e mais.'),
 ('AppRemedioReceita', None, '14 · Enviar receita', 'Foto ou arquivo, observação e confirmação.'),
 ('AppRemedioPaciente', None, '15 · Paciente (gov.br)', 'Para mim: dados preenchidos pelo gov.br.'),
 ('AppRemedioPaciente', {'me': False}, '16 · Paciente (manual)', 'Para outra pessoa: preenchimento manual.'),
 ('AppRemedioEntrega', {'ret': True}, '17 · Retirar na farmácia', 'Quem vai retirar na Farmácia Municipal.'),
 ('AppRemedioEntrega', None, '18 · Receber em casa', 'Endereço completo para o motorista da Saúde.'),
 ('AppRemedioConfirmar', None, '19 · Confirmar pedido', 'Resumo antes de enviar para a farmácia.'),
 ('AppStatusRemedio', {'ret': False, 'stage': 1}, '20 · Verificando receita', 'A Farmácia Municipal confere a receita.'),
 ('AppStatusRemedio', {'ret': True, 'stage': 3}, '21 · Aguardando retirada', 'Pronto para buscar, com código.'),
 ('AppStatusRemedio', {'ret': False, 'stage': 3}, '22 · Aguardando coleta', 'O motorista da Saúde busca na farmácia.'),
 ('AppStatusRemedio', {'ret': False, 'stage': 5}, '23 · Entregue', 'Remédio entregue em casa.'),
 ('AppMeusPedidos', None, '24 · Meus remédios', 'Todos os pedidos e suas situações.'),
 ('AppReceitaRecusada', None, '25 · Receita recusada', 'Motivo da farmácia e envio de nova foto.'),
 ('AppNotificacoes', None, '26 · Avisos', 'Atualizações no app e no WhatsApp.'),
 ('AppPerfil', None, '27 · Perfil e acessibilidade', 'Tamanho da letra, alto contraste, leitura em voz alta.'),
 ('AppAjuda', None, '28 · Ajuda', 'WhatsApp, telefone, atendimento presencial.'),
]
SITE = [
 ('SiteHome', None, 'Página inicial'),
 ('SiteAgendar', {'step': 1}, 'Agendamento · 1. Serviço'), ('SiteAgendar', {'step': 2}, 'Agendamento · 2. Local e horário'),
 ('SiteAgendar', {'step': 3}, 'Agendamento · 3. Seus dados'), ('SiteAgendar', {'step': 4}, 'Agendamento · 4. Confirmação'),
 ('SiteMedicamentos', {'step': 1}, 'Remédio · 1. Receita'), ('SiteMedicamentos', {'step': 2, 'mode': 'entrega'}, 'Remédio · 2. Receber em casa'),
 ('SiteMedicamentos', {'step': 3, 'mode': 'entrega', 'stage': 2}, 'Remédio · 3. Acompanhar'),
]
import json
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
    pg.goto(U); pg.wait_for_timeout(400)
    pg.evaluate("document.body.classList.add('tall')")
    app_imgs = []
    for i, (n, st, cap, desc) in enumerate(APP):
        pg.evaluate(f"window.__go({json.dumps(n)}, {json.dumps(st)})"); pg.wait_for_timeout(60)
        f = f'{SH}/a{i:02d}.png'; pg.locator('#root').screenshot(path=f); app_imgs.append((f, cap, desc))
    pg.evaluate("document.body.classList.remove('tall')")
    pg.set_viewport_size({'width': 1280, 'height': 860})
    pg.evaluate("window.__go('FarmaciaPainel', {st:0})"); pg.wait_for_timeout(60)
    farm = f'{SH}/farm.png'; pg.locator('#root').screenshot(path=farm)
    pg.set_viewport_size({'width': 1440, 'height': 900})
    site_imgs = []
    for i, (n, st, cap) in enumerate(SITE):
        pg.evaluate(f"window.__go({json.dumps(n)}, {json.dumps(st)})"); pg.wait_for_timeout(80)
        f = f'{SH}/s{i:02d}.png'; pg.screenshot(path=f, full_page=True); site_imgs.append((f, cap))

    CSS = '''@page{size:297mm 210mm;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Poppins,Inter,sans-serif;color:#0B2540}
.pg{width:297mm;height:210mm;page-break-after:always;overflow:hidden;position:relative;background:#F5F8FA;padding:12mm 14mm}
.cover{background:#005A8E;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 24mm}
.cover h1{font-size:40pt;margin:8mm 0 2mm;line-height:1.05}.cover p{font-size:15pt;margin:0;color:#D9ECF7}
h2{margin:0 0 6mm;font-size:18pt}.row{display:flex;gap:8mm;height:170mm}
.ph{flex:1;display:flex;flex-direction:column;align-items:center;gap:3mm;min-width:0}
.ph .im{flex:1;width:100%;display:flex;justify-content:center;align-items:flex-start;min-height:0}
.ph img{max-width:100%;max-height:150mm;border-radius:7mm;box-shadow:0 2mm 6mm rgba(0,0,0,.18);border:0.6mm solid #D3E2EC;background:#fff}
.cap{font-weight:700;font-size:12pt;text-align:center}.desc{font-family:Inter,sans-serif;font-size:9.5pt;color:#4A5B6C;text-align:center;max-width:80mm}
.foot{position:absolute;bottom:6mm;right:14mm;font-family:Inter,sans-serif;font-size:8pt;color:#6B7A88}
.full img{width:100%;border-radius:3mm;box-shadow:0 2mm 6mm rgba(0,0,0,.15)}'''
    def cover(title, sub, icon):
        return f'<div class="pg cover"><img src="{b64(icon)}" style="width:40mm;height:40mm;border-radius:9mm"><h1>{title}</h1><p>{sub}</p><p style="margin-top:10mm;font-size:11pt">Prefeitura Municipal de Abadia de Goiás · Protótipo para apresentação · Novembro de 2026<br>Dados e nomes fictícios, apenas para demonstração.</p></div>'
    foot = '<div class="foot">Abadia Mais · protótipo</div>'
    # APP PDF
    pages = [cover('Aplicativo Abadia Mais', 'Consultas, remédios e serviços da Prefeitura no celular — simples e acessível.', L + '/89c9c1171164a74020320258c2870c70.png')]
    for k in range(0, len(app_imgs), 4):
        grp = app_imgs[k:k + 4]
        cells = ''.join(f'<div class="ph"><div class="im"><img src="{b64(f)}"></div><div class="cap">{c}</div><div class="desc">{d}</div></div>' for f, c, d in grp)
        cells += ''.join('<div class="ph"></div>' for _ in range(4 - len(grp)))
        pages.append(f'<div class="pg"><div class="row">{cells}</div>{foot}</div>')
    pages.append(f'<div class="pg full"><h2>Painel da Farmácia Municipal — onde as receitas chegam para verificação</h2><img src="{b64(farm)}" style="max-height:165mm;width:auto;max-width:100%">{foot}</div>')
    open(OUT + '/app_pdf.html', 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    # SITE PDF: home sliced
    from PIL import Image
    pages = [cover('Novo site da Prefeitura', 'Todos os serviços em um só lugar, com agendamento online e pedido de remédio.', L + '/89c9c1171164a74020320258c2870c70.png')]
    home = Image.open(site_imgs[0][0]); W, H = home.size; sliceh = int(W * 0.62); n = 0
    for y in range(0, H, sliceh):
        part = home.crop((0, y, W, min(H, y + sliceh))); fp = f'{SH}/home{n}.png'; part.save(fp); n += 1
        pages.append(f'<div class="pg full"><h2>Página inicial ({n})</h2><img src="{b64(fp)}" style="max-height:168mm;width:auto;max-width:100%">{foot}</div>')
    rest = site_imgs[1:]
    for k in range(0, len(rest), 2):
        grp = rest[k:k + 2]
        cells = ''.join(f'<div class="ph"><div class="cap" style="margin-bottom:2mm">{c}</div><div class="im"><img src="{b64(f)}" style="border-radius:3mm;max-height:160mm"></div></div>' for f, c in grp)
        pages.append(f'<div class="pg"><div class="row">{cells}</div>{foot}</div>')
    open(OUT + '/site_pdf.html', 'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    for nm in ['app', 'site']:
        q = b.new_page(); q.goto(f'file://{OUT}/{nm}_pdf.html'); q.wait_for_timeout(300)
        q.pdf(path=f'/mnt/user-data/outputs/Abadia-Mais-{"Aplicativo" if nm == "app" else "Site"}.pdf', width='297mm', height='210mm', print_background=True)
    b.close()
print('ok')

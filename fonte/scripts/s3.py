from base import *

def linha(lbl, val):
    return f'<div><span style="display: block; font-size: 16px; color: {MUTED}">{lbl}</span><b style="font-size: 19px">{val}</b></div>'

def opt(title, sub, icon, href='#', sel=False):
    border = f'3px solid {B}' if sel else f'2px solid {LINE}'
    bg = LIGHT if sel else '#FFFFFF'
    return f'<a href="{href}" style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 20px; background: {bg}; border: {border}; color: {NAVY}; text-decoration: none"><span style="width: 54px; height: 54px; border-radius: 16px; background: {"#FFFFFF" if sel else LIGHT}; display: flex; align-items: center; justify-content: center; flex: none">{ic(icon, 30)}</span><span style="display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">{title}</span><span style="font-size: 16px; color: {MUTED}">{sub}</span></span></a>'

# ---------- R01 RECEITA ----------
screen('AppRemedioReceita.dc.html', 'App — Enviar receita', h2('Envie a receita') + p('Pode ser foto ou arquivo (PDF).') + f'''
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">
<a href="#" style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 16px 8px; border-radius: 20px; background: {B}; color: #FFFFFF; font-weight: 700; font-size: 18px; text-decoration: none; text-align: center">{ic('camera', 34, '#FFFFFF')}Tirar foto</a>
<a href="#" style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 16px 8px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; font-weight: 700; font-size: 18px; text-decoration: none; text-align: center">{ic('file', 34)}Enviar arquivo</a></div>
<div style="display: flex; gap: 12px; align-items: center; padding: 12px; border-radius: 18px; background: #FFFFFF; border: 2px solid {GREEN}">
<div style="width: 70px; height: 90px; border-radius: 10px; background: #F1F4F6; border: 1px solid #DDE6EE; display: flex; flex-direction: column; gap: 6px; padding: 10px 8px; box-sizing: border-box; flex: none"><span style="height: 4px; background: #B8C4CE; border-radius: 2px"></span><span style="height: 4px; width: 70%; background: #B8C4CE; border-radius: 2px"></span><span style="height: 4px; background: #B8C4CE; border-radius: 2px"></span><span style="height: 4px; width: 50%; background: #B8C4CE; border-radius: 2px"></span></div>
<div style="flex: 1"><p style="margin: 0; font-weight: 700; font-size: 19px; color: {GREEN}">Receita anexada</p><p style="margin: 2px 0 0; font-size: 16px; color: {MUTED}">receita_25-11.jpg</p><a href="#" style="font-size: 17px; font-weight: 700">Trocar</a></div></div>
<label style="display: flex; flex-direction: column; gap: 6px; font-weight: 700; font-size: 17px">Escreva aqui se quiser explicar algo<textarea rows="3" style="padding: 12px 14px; border-radius: 14px; border: 2px solid #8FB3CC; font-size: 18px; color: {NAVY}; resize: none">Remédio de uso contínuo. Preciso para 2 meses.</textarea></label>
<label style="display: flex; gap: 12px; align-items: flex-start; font-size: 18px; line-height: 1.4; padding: 4px 0"><input type="checkbox" checked style="width: 26px; height: 26px; flex: none; margin-top: 2px">Confirmo que a receita é verdadeira e está dentro da validade.</label>
''' + p('A Farmácia Municipal vai conferir a receita antes de separar.', 16) + btn('Continuar', 'AppRemedioPaciente.dc.html'),
    header=topo('Pedir remédio', 'AppInicio.dc.html', 'Passo 1 de 4 · Receita', 25))

# ---------- R02 PACIENTE (interativo) ----------
pac_body = h2('Para quem é o remédio?') + f'''
<button type="button" onClick="{{{{ pickMe }}}}" style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 20px; background: {{{{ meBg }}}}; border: {{{{ meBorder }}}}; color: {NAVY}; text-align: left">{ic('user', 30)}<span style="display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">Para mim</span><span style="font-size: 16px; color: {MUTED}">Usar meus dados do gov.br</span></span></button>
<button type="button" onClick="{{{{ pickOther }}}}" style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 20px; background: {{{{ otherBg }}}}; border: {{{{ otherBorder }}}}; color: {NAVY}; text-align: left">{ic('child', 30)}<span style="display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">Para outra pessoa</span><span style="font-size: 16px; color: {MUTED}">Familiar, vizinho, pessoa que você cuida</span></span></button>
<sc-if value="{{{{ isMe }}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="display: flex; gap: 10px; align-items: center; padding: 12px 14px; border-radius: 16px; background: {GREENBG}; color: #17663A; font-size: 17px">{ic('check', 24, GREEN, 2.5)}Preenchido pelo gov.br</div>
{card(linha('Nome completo', 'Jhiuliano Quinta de Lucia') + linha('CPF', '000.000.000-00') + linha('Cartão do SUS', '000 0000 0000 0000'))}
<a href="#" style="font-size: 17px; font-weight: 700">Corrigir dados</a>
</sc-if>
<sc-if value="{{{{ isOther }}}}" hint-placeholder-val="{{{{ false }}}}">
{field('Nome completo do paciente', 'Maria Aparecida de Lucia')}
<div style="display: flex; gap: 10px">{field('CPF', '000.000.000-00', False)}{field('Nascimento', '00/00/0000', False)}</div>
{field('Cartão do SUS', '000 0000 0000 0000')}
{field('Parentesco', 'Mãe')}
</sc-if>
''' + btn('Continuar', 'AppRemedioEntrega.dc.html')
pac_script = '''class Component extends DCLogic {
  constructor(p) { super(p); this.state = { me: true }; }
  renderVals() {
    const me = this.state.me, on = '3px solid #005A8E', off = '2px solid #D3E2EC';
    return { isMe: me, isOther: !me, meBorder: me ? on : off, meBg: me ? '#EEF5FA' : '#FFFFFF', otherBorder: !me ? on : off, otherBg: !me ? '#EEF5FA' : '#FFFFFF',
      pickMe: () => this.setState({ me: true }), pickOther: () => this.setState({ me: false }) };
  }
}'''
screen('AppRemedioPaciente.dc.html', 'App — Paciente', pac_body, header=topo('Pedir remédio', 'AppRemedioReceita.dc.html', 'Passo 2 de 4 · Paciente', 50), script=pac_script)

# ---------- R03 ENTREGA (interativo) ----------
ent_body = h2('Como o remédio vai chegar até você?') + f'''
<button type="button" onClick="{{{{ pickRet }}}}" style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 20px; background: {{{{ retBg }}}}; border: {{{{ retBorder }}}}; color: {NAVY}; text-align: left">{ic('store', 30)}<span style="display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">Vou retirar na farmácia</span><span style="font-size: 16px; color: {MUTED}">Farmácia Municipal · sem fila</span></span></button>
<button type="button" onClick="{{{{ pickCol }}}}" style="display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 20px; background: {{{{ colBg }}}}; border: {{{{ colBorder }}}}; color: {NAVY}; text-align: left">{ic('truck', 30)}<span style="display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">Receber em casa</span><span style="font-size: 16px; color: {MUTED}">O motorista da Saúde leva até você</span></span></button>
<sc-if value="{{{{ isRet }}}}" hint-placeholder-val="{{{{ true }}}}">
{card(linha('Farmácia Municipal', '[Endereço] · Seg a sex, 7h às 17h') + p('Você recebe um aviso quando estiver pronto para retirar.', 17))}
<p style="margin: 0; font-weight: 700; font-size: 19px">Quem vai retirar?</p>
{field('Nome de quem vai buscar', 'Jhiuliano Quinta de Lucia')}
{p('Outra pessoa pode buscar levando documento com foto.', 16)}
</sc-if>
<sc-if value="{{{{ isCol }}}}" hint-placeholder-val="{{{{ false }}}}">
<div style="display: flex; gap: 10px; align-items: center; padding: 12px 14px; border-radius: 16px; background: {GREENBG}; color: #17663A; font-size: 17px">{ic('check', 24, GREEN, 2.5)}Endereço do seu cadastro gov.br</div>
{field('Nome completo de quem vai receber', 'Jhiuliano Quinta de Lucia')}
{field('Rua', 'Rua [nome]')}
<div style="display: flex; gap: 10px">{field('Número', 'Qd. 00 Lt. 00', False)}{field('Bairro', 'Jardim Nova Abadia', False)}</div>
{field('Ponto de referência', 'Casa azul, perto da praça')}
{field('Telefone para o motorista', '(62) 9 0000-0000')}
<a href="#" style="display: flex; gap: 8px; align-items: center; font-size: 17px; font-weight: 700">{ic('pin', 22)}Usar minha localização agora</a>
</sc-if>
''' + btn('Continuar', 'AppRemedioConfirmar.dc.html')
ent_script = '''class Component extends DCLogic {
  constructor(p) { super(p); this.state = { ret: false }; }
  renderVals() {
    const r = this.state.ret, on = '3px solid #005A8E', off = '2px solid #D3E2EC';
    return { isRet: r, isCol: !r, retBorder: r ? on : off, retBg: r ? '#EEF5FA' : '#FFFFFF', colBorder: !r ? on : off, colBg: !r ? '#EEF5FA' : '#FFFFFF',
      pickRet: () => this.setState({ ret: true }), pickCol: () => this.setState({ ret: false }) };
  }
}'''
screen('AppRemedioEntrega.dc.html', 'App — Retirada ou entrega', ent_body, header=topo('Pedir remédio', 'AppRemedioPaciente.dc.html', 'Passo 3 de 4 · Retirada ou entrega', 75), script=ent_script, gap=12)

# ---------- R04 CONFIRMAR ----------
screen('AppRemedioConfirmar.dc.html', 'App — Confirmar pedido de remédio', h2('Confira seu pedido') + card(
    linha('Paciente', 'Jhiuliano Quinta de Lucia') + linha('Receita', 'receita_25-11.jpg · 1 foto') + linha('Sua observação', 'Remédio de uso contínuo. Preciso para 2 meses.') +
    linha('Como vai receber', 'Em casa, pelo motorista da Saúde') + linha('Endereço', 'Rua [nome], Qd. 00 Lt. 00 · Jardim Nova Abadia') +
    '<a href="AppRemedioEntrega.dc.html" style="font-size: 17px; font-weight: 700">Alterar</a>') +
    f'<div style="padding: 14px; border-radius: 16px; background: {LIGHT}; font-size: 17px; line-height: 1.45"><b>O que acontece agora:</b> a Farmácia Municipal confere a receita. Você recebe cada atualização aqui e no WhatsApp.</div>' +
    btn('Enviar para a farmácia', 'AppStatusRemedio.dc.html', 'green'),
    header=topo('Pedir remédio', 'AppRemedioEntrega.dc.html', 'Passo 4 de 4 · Confirmar', 100))

# ---------- R05 STATUS (interativo) ----------
st_body = f'''
<div style="display: flex; justify-content: space-between; align-items: center"><h2 style="margin: 0; font-family: Poppins; font-size: 24px">Pedido nº 4821</h2><span style="font-size: 16px; color: {MUTED}">25/11 · 10:42</span></div>
<div role="group" aria-label="Ver exemplo" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px; padding: 5px; border-radius: 16px; background: #E4ECF2">
<button type="button" onClick="{{{{ modeRet }}}}" style="min-height: 46px; border-radius: 12px; border: 0; background: {{{{ retTab }}}}; color: {NAVY}; font-size: 17px; font-weight: 700">Retirada</button>
<button type="button" onClick="{{{{ modeCol }}}}" style="min-height: 46px; border-radius: 12px; border: 0; background: {{{{ colTab }}}}; color: {NAVY}; font-size: 17px; font-weight: 700">Entrega em casa</button></div>
<div style="padding: 18px; border-radius: 22px; background: {{{{ curBg }}}}; color: {{{{ curFg }}}}; display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 16px; font-weight: 700; letter-spacing: 1px">SITUAÇÃO AGORA</span>
<span style="font-family: Poppins; font-weight: 700; font-size: 24px; line-height: 1.2">{{{{ curTitle }}}}</span>
<span style="font-size: 18px; line-height: 1.4">{{{{ curText }}}}</span></div>
<ol style="list-style: none; margin: 0; padding: 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}">
<sc-for list="{{{{ track }}}}" as="tr" hint-placeholder-count="6">
<li style="display: flex; gap: 14px"><div style="display: flex; flex-direction: column; align-items: center"><span style="width: 26px; height: 26px; border-radius: 50%; background: {{{{ tr.dot }}}}; border: 3px solid {{{{ tr.ring }}}}; box-sizing: border-box; flex: none"></span><span style="width: 3px; flex: 1; min-height: 18px; background: #DDE6EE"></span></div>
<div style="padding-bottom: 12px"><p style="margin: 0; font-weight: 700; font-size: 18px; color: {{{{ tr.color }}}}">{{{{ tr.label }}}}</p><p style="margin: 2px 0 0; font-size: 15px; color: {MUTED}">{{{{ tr.when }}}}</p></div></li>
</sc-for></ol>
<sc-if value="{{{{ showCode }}}}" hint-placeholder-val="{{{{ false }}}}">
<div style="display: flex; gap: 14px; align-items: center; padding: 14px; border-radius: 20px; background: {B}; color: #FFFFFF"><span style="width: 84px; height: 84px; border-radius: 14px; background: #FFFFFF; color: {NAVY}; font-family: Poppins; font-weight: 700; font-size: 24px; display: flex; align-items: center; justify-content: center; flex: none">4821</span><span style="font-size: 17px; line-height: 1.4">{{{{ codeText }}}}</span></div>
</sc-if>
<button type="button" onClick="{{{{ advance }}}}" style="min-height: 52px; border-radius: 14px; border: 2px dashed #8FB3CC; background: #FFFFFF; color: {NAVY}; font-size: 17px; font-weight: 700">Simular próxima etapa (apresentação)</button>
{btn('Falar com a farmácia', 'AppAjuda.dc.html', 'ghost')}
'''
st_script = r'''class Component extends DCLogic {
  constructor(p) { super(p); this.state = { ret: false, stage: 1 }; }
  renderVals() {
    const S = this.state, r = S.ret;
    const steps = r
      ? [['Receita enviada', '25/11 às 10:42'], ['Verificando receita', 'Farmácia Municipal conferindo'], ['Receita aprovada · separando', 'Farmácia separando os remédios'], ['Aguardando retirada', 'Pode buscar na Farmácia Municipal'], ['Retirado', 'Retirado por Jhiuliano']]
      : [['Receita enviada', '25/11 às 10:42'], ['Verificando receita', 'Farmácia Municipal conferindo'], ['Receita aprovada · separando', 'Farmácia separando os remédios'], ['Aguardando coleta', 'Motorista da Saúde vai buscar na farmácia'], ['Saiu para entrega', 'A caminho do seu endereço'], ['Entregue', 'Recebido por Jhiuliano']];
    const st = Math.min(S.stage, steps.length - 1);
    const info = r
      ? [['Receita enviada', 'Recebemos sua receita.', '#EEF5FA', '#0B2540'], ['Verificando receita', 'A Farmácia Municipal está conferindo sua receita. Isso leva até 1 dia útil.', '#FFF6DC', '#3D2B00'], ['Separando seus remédios', 'Receita aprovada! A farmácia está separando.', '#EEF5FA', '#0B2540'], ['Aguardando retirada', 'Pronto! Busque na Farmácia Municipal até 05/12, de seg a sex, 7h às 17h.', '#005A8E', '#FFFFFF'], ['Retirado', 'Remédio entregue em mãos. Obrigado!', '#E3F5EA', '#17663A']]
      : [['Receita enviada', 'Recebemos sua receita.', '#EEF5FA', '#0B2540'], ['Verificando receita', 'A Farmácia Municipal está conferindo sua receita. Isso leva até 1 dia útil.', '#FFF6DC', '#3D2B00'], ['Separando seus remédios', 'Receita aprovada! A farmácia está separando.', '#EEF5FA', '#0B2540'], ['Aguardando coleta', 'O motorista da Saúde vai buscar seu remédio na farmácia.', '#005A8E', '#FFFFFF'], ['Saiu para entrega', 'O motorista está a caminho. Deixe alguém em casa para receber.', '#005A8E', '#FFFFFF'], ['Entregue', 'Remédio entregue no seu endereço. Obrigado!', '#E3F5EA', '#17663A']];
    const cur = info[st];
    return {
      retTab: r ? '#FFFFFF' : 'transparent', colTab: !r ? '#FFFFFF' : 'transparent',
      modeRet: () => this.setState({ ret: true, stage: 1 }), modeCol: () => this.setState({ ret: false, stage: 1 }),
      curTitle: cur[0], curText: cur[1], curBg: cur[2], curFg: cur[3],
      track: steps.map((s, i) => { const d = i <= st; return { label: s[0], when: d ? s[1] : 'Aguardando', dot: i < st ? '#1B7A43' : d ? '#005A8E' : '#FFFFFF', ring: i < st ? '#1B7A43' : d ? '#005A8E' : '#C5D3DD', color: d ? '#0B2540' : '#4A5B6C' }; }),
      showCode: st >= 3 && st < steps.length - 1,
      codeText: r ? 'Mostre este número e um documento com foto na farmácia.' : 'Diga este número ao motorista para receber.',
      advance: () => this.setState({ stage: st + 1 >= steps.length ? 0 : st + 1 })
    };
  }
}'''
screen('AppStatusRemedio.dc.html', 'App — Situação do pedido de remédio', st_body, header=topo('Meu pedido', 'AppMeusPedidos.dc.html'), script=st_script, gap=12)

# ---------- R06 MEUS PEDIDOS ----------
peds = [('4821', 'Losartana, Metformina', 'Verificando receita', AMBERBG, AMBER, 'AppStatusRemedio.dc.html'),
        ('4790', 'Omeprazol 20 mg', 'Aguardando retirada', LIGHT, NAVY, 'AppStatusRemedio.dc.html'),
        ('4755', 'Insulina NPH', 'Aguardando coleta', LIGHT, NAVY, 'AppStatusRemedio.dc.html'),
        ('4702', 'Losartana, Metformina', 'Entregue em 28/10', GREENBG, '#17663A', 'AppStatusRemedio.dc.html'),
        ('4688', 'Amoxicilina 500 mg', 'Receita recusada', REDBG, RED, 'AppReceitaRecusada.dc.html')]
pl = ''.join(f'<a href="{h}" style="display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none"><span style="flex: 1; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 16px; color: {MUTED}">Pedido nº {n}</span><span style="font-weight: 700; font-size: 19px">{m}</span>{badge(s, bg, fg)}</span>{ic("chev", 24, MUTED)}</a>' for n, m, s, bg, fg, h in peds)
screen('AppMeusPedidos.dc.html', 'App — Meus remédios', f'''<h1 style="margin: 0; font-family: Poppins; font-size: 26px">Meus remédios</h1>
<a href="AppRemedioReceita.dc.html" style="display: flex; align-items: center; justify-content: center; min-height: 58px; border-radius: 18px; background: {B}; color: #FFFFFF; font-size: 19px; font-weight: 700; text-decoration: none">+ Novo pedido de remédio</a>{pl}''', tab='remedios', gap=12)

# ---------- R07 RECUSADA ----------
screen('AppReceitaRecusada.dc.html', 'App — Receita recusada', f'''
<div style="padding: 18px; border-radius: 22px; background: {REDBG}; color: {RED}; display: flex; flex-direction: column; gap: 6px; border: 2px solid #F0B8B3">
<span style="display: flex; gap: 8px; align-items: center; font-family: Poppins; font-weight: 700; font-size: 22px">{ic('x', 26, RED, 2.5)}Receita não aprovada</span>
<span style="font-size: 18px; line-height: 1.45; color: #5C1A14">Pedido nº 4688 · Amoxicilina 500 mg</span></div>''' +
    card(f'<span style="font-size: 16px; color: {MUTED}">O que a Farmácia Municipal disse</span>' + p('“A foto está escura e não dá para ler o nome do remédio nem a assinatura do médico. Mande uma foto nova, com mais luz.”', 19, NAVY) +
         f'<span style="font-size: 15px; color: {MUTED}">Farmácia Municipal · 24/11 às 15:20</span>') +
    p('Não se preocupe: é só mandar de novo. Seu pedido continua na fila.', 18) +
    btn('Mandar nova foto da receita', 'AppRemedioReceita.dc.html') + btn('Falar com a farmácia', 'AppAjuda.dc.html', 'ghost'),
    header=topo('Meu pedido', 'AppMeusPedidos.dc.html'))

# ---------- NOTIFICACOES ----------
nots = [('clock', AMBERBG, '#8A6100', 'Farmácia verificando sua receita', 'Pedido nº 4821 · agora'),
        ('cal', LIGHT, B, 'Lembrete: consulta quarta, 02/12 às 08:30', 'UBS Unidade 1 · há 1 hora'),
        ('truck', LIGHT, B, 'Insulina aguardando coleta', 'O motorista da Saúde vai buscar · ontem'),
        ('x', REDBG, RED, 'Receita do pedido 4688 precisa de nova foto', 'Toque para ver o motivo · 24/11'),
        ('check', GREENBG, GREEN, 'Remédio entregue', 'Pedido nº 4702 · 28/10')]
nl = ''.join(f'<div style="display: flex; gap: 12px; padding: 14px; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}"><span style="width: 46px; height: 46px; border-radius: 14px; background: {bg}; display: flex; align-items: center; justify-content: center; flex: none">{ic(i, 24, fg)}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 700; font-size: 18px; line-height: 1.3">{t}</span><span style="font-size: 15px; color: {MUTED}">{s}</span></span></div>' for i, bg, fg, t, s in nots)
screen('AppNotificacoes.dc.html', 'App — Notificações', nl + p('Os mesmos avisos também chegam no seu WhatsApp.', 16, MUTED, 'text-align: center'), header=topo('Avisos', 'AppInicio.dc.html'), gap=10)

# ---------- PERFIL ----------
def tog(label, on, icon):
    track = GREEN if on else '#B8C4CE'
    knob = 'flex-end' if on else 'flex-start'
    return f'<div style="display: flex; align-items: center; gap: 12px; min-height: 60px">{ic(icon, 26, NAVY)}<span style="flex: 1; font-size: 19px; font-weight: 700">{label}</span><span role="switch" aria-checked="{"true" if on else "false"}" style="width: 60px; height: 34px; border-radius: 17px; background: {track}; display: flex; justify-content: {knob}; align-items: center; padding: 3px; box-sizing: border-box"><span style="width: 28px; height: 28px; border-radius: 50%; background: #FFFFFF"></span></span></div>'
screen('AppPerfil.dc.html', 'App — Perfil e acessibilidade', f'''
<div style="display: flex; gap: 14px; align-items: center"><span style="width: 70px; height: 70px; border-radius: 50%; background: {B}; color: #FFFFFF; font-family: Poppins; font-weight: 700; font-size: 26px; display: flex; align-items: center; justify-content: center">JQ</span>
<span style="display: flex; flex-direction: column"><span style="font-family: Poppins; font-weight: 700; font-size: 21px">Jhiuliano Quinta de Lucia</span><span style="font-size: 16px; color: {GREEN}; font-weight: 700">Conta gov.br verificada</span></span></div>
<a href="AppCadastro.dc.html" style="display: flex; align-items: center; gap: 12px; min-height: 60px; padding: 0 16px; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; font-size: 19px; font-weight: 700; text-decoration: none">{ic('user', 26, NAVY)}<span style="flex: 1">Meus dados e endereço</span>{ic('chev', 24, MUTED)}</a>
<a href="#" style="display: flex; align-items: center; gap: 12px; min-height: 60px; padding: 0 16px; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; font-size: 19px; font-weight: 700; text-decoration: none">{ic('child', 26, NAVY)}<span style="flex: 1">Família e dependentes</span>{ic('chev', 24, MUTED)}</a>
<p style="margin: 6px 0 0; font-weight: 700; font-size: 20px">Facilitar o uso</p>
<div style="padding: 14px 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; display: flex; flex-direction: column; gap: 10px">
<span style="display: flex; gap: 12px; align-items: center; font-size: 19px; font-weight: 700">{ic('type', 26, NAVY)}Tamanho da letra</span>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">
<a href="#" style="display: flex; align-items: center; justify-content: center; min-height: 54px; border-radius: 14px; border: 2px solid {LINE}; color: {NAVY}; font-size: 18px; font-weight: 700; text-decoration: none">A</a>
<a href="#" style="display: flex; align-items: center; justify-content: center; min-height: 54px; border-radius: 14px; background: {B}; color: #FFFFFF; font-size: 24px; font-weight: 700; text-decoration: none">A</a>
<a href="#" style="display: flex; align-items: center; justify-content: center; min-height: 54px; border-radius: 14px; border: 2px solid {LINE}; color: {NAVY}; font-size: 30px; font-weight: 700; text-decoration: none">A</a></div>
{tog('Alto contraste', False, 'sun')}{tog('Ler a tela em voz alta', True, 'volume')}{tog('Avisos no WhatsApp', True, 'msg')}</div>
<a href="AppAjuda.dc.html" style="display: flex; align-items: center; gap: 12px; min-height: 60px; padding: 0 16px; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; font-size: 19px; font-weight: 700; text-decoration: none">{ic('help', 26, NAVY)}<span style="flex: 1">Ajuda</span>{ic('chev', 24, MUTED)}</a>
<a href="AppAbertura.dc.html" style="display: flex; align-items: center; gap: 12px; min-height: 60px; padding: 0 16px; border-radius: 18px; color: {RED}; font-size: 19px; font-weight: 700; text-decoration: none">{ic('logout', 26, RED)}Sair do aplicativo</a>
''', tab='perfil', gap=12)

# ---------- AJUDA ----------
faq = ['Como marcar uma consulta?', 'Quanto tempo a farmácia leva para conferir a receita?', 'Outra pessoa pode buscar meu remédio?', 'Como desmarcar uma consulta?']
fl = ''.join(f'<a href="#" style="display: flex; align-items: center; gap: 10px; min-height: 60px; padding: 8px 16px; box-sizing: border-box; border-radius: 16px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; font-size: 18px; font-weight: 700; text-decoration: none"><span style="flex: 1">{q}</span>{ic("chev", 22, MUTED)}</a>' for q in faq)
screen('AppAjuda.dc.html', 'App — Ajuda', h2('Como podemos ajudar?') + p('Um atendente da Prefeitura faz o pedido junto com você.') +
    f'<a href="#" style="display: flex; align-items: center; justify-content: center; gap: 10px; min-height: 64px; border-radius: 18px; background: {GREEN}; color: #FFFFFF; font-size: 20px; font-weight: 700; text-decoration: none">{ic("msg", 28, "#FFFFFF")}Falar no WhatsApp</a>' +
    f'<a href="#" style="display: flex; align-items: center; justify-content: center; gap: 10px; min-height: 64px; border-radius: 18px; background: #FFFFFF; border: 2px solid {NAVY}; color: {NAVY}; font-size: 20px; font-weight: 700; text-decoration: none">{ic("phone", 26, NAVY)}Ligar (62) 99348-0641</a>' +
    card(f'<b style="font-size: 19px">Atendimento presencial</b>' + p('Av. Francisco Paiva da Silva, Jardim Nova Abadia<br>Seg a sex, 7h30–11h30 e 13h–17h', 17)) +
    '<p style="margin: 6px 0 0; font-weight: 700; font-size: 20px">Perguntas frequentes</p>' + fl,
    header=topo('Ajuda', 'AppInicio.dc.html'), gap=12)
print('ok s3')

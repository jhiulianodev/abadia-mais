from base import *

# ---------- CONSULTA: CALENDARIO (interativo) ----------
cal_body = f'''
<div style="display: flex; gap: 12px; align-items: center; padding: 12px; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}">
<span style="width: 50px; height: 50px; border-radius: 50%; background: {LIGHT}; color: {B}; font-family: Poppins; font-weight: 700; font-size: 18px; display: flex; align-items: center; justify-content: center; flex: none">AR</span>
<span style="display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 18px">Dra. Ana Paula Ribeiro</span><span style="font-size: 16px; color: {MUTED}">Clínica geral · UBS Unidade 1</span></span></div>
<div style="padding: 14px 12px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; justify-content: space-between; align-items: center">
<button type="button" onClick="{{{{ prevMonth }}}}" aria-label="Mês anterior" style="width: 48px; height: 48px; border-radius: 12px; border: 2px solid {LINE}; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('back', 24, NAVY, 2.5)}</button>
<span style="font-family: Poppins; font-weight: 700; font-size: 21px">{{{{ monthLabel }}}}</span>
<button type="button" onClick="{{{{ nextMonth }}}}" aria-label="Próximo mês" style="width: 48px; height: 48px; border-radius: 12px; border: 2px solid {LINE}; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ic('chev', 24, NAVY, 2.5)}</button></div>
<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 4px; text-align: center; font-size: 15px; font-weight: 700; color: {MUTED}"><span>D</span><span>S</span><span>T</span><span>Q</span><span>Q</span><span>S</span><span>S</span></div>
<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 4px">
<sc-for list="{{{{ cells }}}}" as="c" hint-placeholder-count="35">
<button type="button" onClick="{{{{ c.pick }}}}" aria-label="{{{{ c.aria }}}}" style="height: 44px; border-radius: 12px; border: {{{{ c.border }}}}; background: {{{{ c.bg }}}}; color: {{{{ c.fg }}}}; font-size: 18px; font-weight: 700; text-decoration: {{{{ c.deco }}}}; padding: 0">{{{{ c.label }}}}</button>
</sc-for></div>
<div style="display: flex; flex-wrap: wrap; gap: 8px 14px; font-size: 15px; color: {MUTED}">
<span style="display: flex; align-items: center; gap: 6px"><span style="width: 16px; height: 16px; border-radius: 5px; background: {LIGHT}; border: 2px solid {B}"></span>Tem vaga</span>
<span style="display: flex; align-items: center; gap: 6px"><span style="width: 16px; height: 16px; border-radius: 5px; background: {AMBERBG}; border: 2px solid #E0B44A"></span>Poucas vagas</span>
<span style="display: flex; align-items: center; gap: 6px"><span style="width: 16px; height: 16px; border-radius: 5px; background: #ECEFF2"></span>Sem vaga</span></div>
</div>
<p style="margin: 4px 0 0; font-weight: 700; font-size: 19px">Horários de {{{{ dayLabel }}}}</p>
<sc-if value="{{{{ hasTimes }}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">
<sc-for list="{{{{ times }}}}" as="t" hint-placeholder-count="9">
<button type="button" onClick="{{{{ t.pick }}}}" aria-label="{{{{ t.aria }}}}" style="min-height: 54px; border-radius: 14px; border: {{{{ t.border }}}}; background: {{{{ t.bg }}}}; color: {{{{ t.fg }}}}; font-size: 19px; font-weight: 700; text-decoration: {{{{ t.deco }}}}">{{{{ t.time }}}}</button>
</sc-for></div>
</sc-if>
<sc-if value="{{{{ noTimes }}}}" hint-placeholder-val="{{{{ false }}}}">{p('Escolha um dia com vaga no calendário.', 17)}</sc-if>
<div style="padding: 14px; border-radius: 18px; background: {LIGHT}; font-size: 18px; line-height: 1.4">Você escolheu: <b>{{{{ summary }}}}</b></div>
{btn('Continuar', 'AppConsultaConfirmar.dc.html')}
'''
cal_script = r'''class Component extends DCLogic {
  constructor(p) { super(p); this.state = { m: 0, day: 2, time: 2 }; }
  renderVals() {
    const S = this.state;
    const M = [{ name: 'Dezembro de 2026', first: 2, len: 31, full: [4, 16], few: [9, 18], off: [25], minDay: 2 },
               { name: 'Janeiro de 2027', first: 5, len: 31, full: [], few: [6, 8], off: [1], minDay: 1 }][S.m];
    const docDays = [1, 3, 5];
    const W = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];
    const cells = [];
    for (let i = 0; i < M.first; i++) cells.push({ label: '', aria: '', border: '0', bg: 'transparent', fg: 'transparent', deco: 'none', pick: () => {} });
    for (let d = 1; d <= M.len; d++) {
      const wd = (M.first + d - 1) % 7;
      const works = docDays.includes(wd) && d >= M.minDay && !M.off.includes(d);
      const full = works && M.full.includes(d);
      const few = works && M.few.includes(d);
      const ok = works && !full;
      const sel = ok && d === S.day;
      let c = { border: '0', bg: '#FFFFFF', fg: '#9AA6B2', deco: 'none' };
      if (full) c = { border: '0', bg: '#ECEFF2', fg: '#7A8794', deco: 'line-through' };
      else if (sel) c = { border: '3px solid #0B2540', bg: '#005A8E', fg: '#FFFFFF', deco: 'none' };
      else if (few) c = { border: '2px solid #E0B44A', bg: '#FFF6DC', fg: '#0B2540', deco: 'none' };
      else if (ok) c = { border: '2px solid #005A8E', bg: '#EEF5FA', fg: '#0B2540', deco: 'none' };
      cells.push({ label: String(d), aria: d + (ok ? ' com vaga' : ' sem vaga'), ...c, pick: () => { if (ok) this.setState({ day: d, time: -1 }); } });
    }
    const wdSel = (M.first + S.day - 1) % 7;
    const validDay = docDays.includes(wdSel) && S.day >= M.minDay && !M.off.includes(S.day) && !M.full.includes(S.day);
    const T = ['07:30', '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30'];
    const taken = M.few.includes(S.day) ? [0, 1, 2, 4, 5, 7] : [1, 5];
    const times = T.map((t, i) => {
      const busy = taken.includes(i), sel = i === S.time;
      const c = busy ? { border: '0', bg: '#ECEFF2', fg: '#7A8794', deco: 'line-through' } : sel ? { border: '3px solid #0B2540', bg: '#005A8E', fg: '#FFFFFF', deco: 'none' } : { border: '2px solid #D3E2EC', bg: '#FFFFFF', fg: '#0B2540', deco: 'none' };
      return { time: t, aria: t + (busy ? ' ocupado' : ' livre'), ...c, pick: () => { if (!busy) this.setState({ time: i }); } };
    });
    const mon = S.m === 0 ? '12' : '01';
    const dd = String(S.day).padStart(2, '0') + '/' + mon;
    return {
      monthLabel: M.name, cells, times, hasTimes: validDay, noTimes: !validDay,
      dayLabel: validDay ? W[wdSel].toLowerCase() + ', ' + dd : 'um dia',
      summary: validDay && S.time >= 0 ? W[wdSel] + ', ' + dd + ' às ' + T[S.time] : 'escolha dia e horário',
      prevMonth: () => this.setState({ m: 0, day: 2, time: -1 }),
      nextMonth: () => this.setState({ m: 1, day: 6, time: -1 })
    };
  }
}'''
screen('AppConsultaCalendario.dc.html', 'App — Dia e horário', cal_body,
       header=topo('Marcar consulta', 'AppConsultaMedico.dc.html', 'Passo 4 de 5 · Dia e horário', 80), script=cal_script, gap=12)

# ---------- CONSULTA: CONFIRMAR ----------
def linha(lbl, val):
    return f'<div><span style="display: block; font-size: 16px; color: {MUTED}">{lbl}</span><b style="font-size: 19px">{val}</b></div>'
screen('AppConsultaConfirmar.dc.html', 'App — Confirmar consulta', h2('Confira antes de confirmar') + card(
    linha('Consulta', 'Clínico geral') + linha('Médico', 'Dra. Ana Paula Ribeiro') + linha('Local', 'UBS Unidade 1 · [endereço]') +
    linha('Dia e hora', 'Quarta, 02/12 às 08:30') + linha('Paciente', 'Jhiuliano Quinta de Lucia') +
    '<a href="AppConsultaCalendario.dc.html" style="font-size: 17px; font-weight: 700">Mudar dia ou horário</a>') +
    f'''<label style="display: flex; flex-direction: column; gap: 6px; font-weight: 700; font-size: 17px">Motivo da consulta (opcional)<textarea rows="3" style="padding: 12px 14px; border-radius: 14px; border: 2px solid #8FB3CC; font-size: 18px; color: {NAVY}; resize: none">Dor nas costas há uma semana</textarea></label>
<label style="display: flex; gap: 12px; align-items: center; font-size: 18px; padding: 6px 0"><input type="checkbox" checked style="width: 26px; height: 26px; flex: none">Me lembrar no WhatsApp 1 dia antes</label>
<div style="padding: 14px; border-radius: 16px; background: {AMBERBG}; color: #3D2B00; font-size: 17px; line-height: 1.45"><b>Leve no dia:</b> documento com foto e Cartão do SUS. Chegue 15 minutos antes.</div>''' +
    btn('Confirmar consulta', 'AppConsultaPronto.dc.html', 'green'),
    header=topo('Marcar consulta', 'AppConsultaCalendario.dc.html', 'Passo 5 de 5 · Confirmar', 100))

# ---------- CONSULTA: PRONTO ----------
screen('AppConsultaPronto.dc.html', 'App — Consulta marcada', f'''
<div style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; padding-top: 16px">
<span style="width: 100px; height: 100px; border-radius: 50%; background: {GREENBG}; display: flex; align-items: center; justify-content: center">{ic('check', 54, GREEN, 2.5)}</span>
<h1 style="margin: 0; font-family: Poppins; font-size: 28px">Consulta marcada!</h1>
{p('<b style="color: #0B2540">Quarta, 02/12 às 08:30</b><br>Dra. Ana Paula Ribeiro · Clínico geral<br>UBS Unidade 1', 19)}
<span style="padding: 10px 16px; border-radius: 14px; background: #FFFFFF; border: 2px solid {LINE}; font-family: Poppins; font-weight: 700; font-size: 18px">Protocolo AGD-2026-004817</span>
{p('Enviamos o comprovante no seu WhatsApp.', 17)}
</div>
{btn('Adicionar na agenda do celular', '#', 'ghost')}
{btn('Como chegar na UBS', '#', 'ghost')}
{btn('Voltar ao início', 'AppInicio.dc.html')}
''', bg='#FFFFFF')

# ---------- MEUS AGENDAMENTOS ----------
ag = [('Quarta, 02/12 · 08:30', 'Clínico geral · Dra. Ana Paula Ribeiro', 'UBS Unidade 1', 'Confirmada', GREENBG, '#17663A', 'AppAgendamentoDetalhe.dc.html'),
      ('Segunda, 07/12 · 09:00', 'Carteira de Identidade (2ª via)', 'Posto de Identificação', 'Confirmada', GREENBG, '#17663A', 'AppAgendamentoDetalhe.dc.html'),
      ('Quinta, 10/12 · 14:00', 'Dentista · Dr. Rafael Nunes', 'UBS Unidade 2', 'Aguardando confirmação', AMBERBG, AMBER, 'AppAgendamentoDetalhe.dc.html')]
old = [('10/11 · Enfermagem', 'Realizada', '#ECEFF2', '#3D4A57'), ('28/10 · Clínico geral', 'Faltou', REDBG, RED)]
items = ''
for w, s, l, st, bg, fg, href in ag:
    items += f'<a href="{href}" style="display: flex; flex-direction: column; gap: 6px; padding: 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none">{badge(st, bg, fg)}<span style="font-family: Poppins; font-weight: 700; font-size: 20px">{w}</span><span style="font-size: 18px">{s}</span><span style="font-size: 16px; color: {MUTED}">{l}</span></a>'
olds = ''.join(f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 14px 16px; border-radius: 16px; background: #FFFFFF; border: 1px solid {LINE}"><span style="font-size: 18px">{a}</span>{badge(b, c, d)}</div>' for a, b, c, d in old)
screen('AppMeusAgendamentos.dc.html', 'App — Meus agendamentos', f'''
<h1 style="margin: 0; font-family: Poppins; font-size: 26px">Meus agendamentos</h1>
<a href="AppConsultaTipo.dc.html" style="display: flex; align-items: center; justify-content: center; gap: 8px; min-height: 58px; border-radius: 18px; background: {B}; color: #FFFFFF; font-size: 19px; font-weight: 700; text-decoration: none">+ Novo agendamento</a>
<p style="margin: 6px 0 0; font-weight: 700; font-size: 19px">Próximos</p>{items}
<p style="margin: 6px 0 0; font-weight: 700; font-size: 19px">Anteriores</p>{olds}
''', tab='agenda')

# ---------- DETALHE AGENDAMENTO ----------
screen('AppAgendamentoDetalhe.dc.html', 'App — Detalhe do agendamento', badge('Confirmada', GREENBG, '#17663A') + f'''
<h2 style="margin: 0; font-family: Poppins; font-size: 26px">Quarta, 02/12 às 08:30</h2>''' + card(
    linha('Consulta', 'Clínico geral') + linha('Médico', 'Dra. Ana Paula Ribeiro') + linha('Local', 'UBS Unidade 1 · [endereço]') + linha('Protocolo', 'AGD-2026-004817')) +
    f'''<div style="display: flex; gap: 14px; align-items: center; padding: 16px; border-radius: 20px; background: {B}; color: #FFFFFF">
<span style="width: 92px; height: 92px; border-radius: 14px; background: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none">{ic('qr', 64, NAVY, 1.6)}</span>
<span style="font-size: 17px; line-height: 1.45">Na recepção da UBS, mostre este código. Sua chegada é registrada na hora.</span></div>''' +
    btn('Como chegar', '#', 'ghost') + btn('Remarcar', 'AppConsultaCalendario.dc.html', 'ghost') + btn('Cancelar consulta', '#', 'danger') +
    p('Se não puder ir, cancele: a vaga fica para outra pessoa.', 16, MUTED, 'text-align: center'),
    header=topo('Agendamento', 'AppMeusAgendamentos.dc.html'))

# ---------- OUTROS AGENDAMENTOS ----------
outs = [('Carteira de Identidade', '1ª e 2ª via da nova CIN', 'id'), ('Vapt Vupt', 'CNH, Detran, Saneago e outros', 'bldg'),
        ('Junta Militar', 'Alistamento e certificado', 'shield'), ('CRAS e CadÚnico', 'Atendimento social', 'user'),
        ('Sala do Empreendedor', 'MEI e alvará', 'store')]
o = ''.join(f'<a href="AppConsultaCalendario.dc.html" style="display: flex; align-items: center; gap: 14px; min-height: 80px; padding: 12px 16px; box-sizing: border-box; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none"><span style="width: 50px; height: 50px; border-radius: 14px; background: {LIGHT}; display: flex; align-items: center; justify-content: center; flex: none">{ic(i, 28)}</span><span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">{n}</span><span style="font-size: 16px; color: {MUTED}">{s}</span></span>{ic("chev", 24, MUTED)}</a>' for n, s, i in outs)
screen('AppOutrosAgendamentos.dc.html', 'App — Outros agendamentos', h2('O que você quer agendar?') + o +
       p('Documentos necessários aparecem antes de confirmar.', 16), header=topo('Agendar atendimento', 'AppInicio.dc.html'))
print('ok s2')

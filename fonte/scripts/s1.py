from base import *

NOME = 'Jhiuliano Quinta de Lucia'

# ---------- LOGIN ----------
screen('AppLogin.dc.html', 'App — Entrar', f'''
<div style="display: flex; flex-direction: column; align-items: center; gap: 10px; padding: 16px 0 6px; text-align: center">
<img src="/_blob/89c9c1171164a74020320258c2870c70" alt="Ícone Abadia Mais" style="width: 92px; height: 92px; border-radius: 22px; box-shadow: 0 0 0 1px {LINE}">
<h1 style="margin: 6px 0 0; font-family: Poppins; font-size: 28px; color: {NAVY}">Entrar no Abadia Mais</h1>
{p('Escolha como você quer entrar.')}
</div>
<a href="AppCadastro.dc.html" style="display: flex; align-items: center; justify-content: center; gap: 10px; min-height: 64px; border-radius: 18px; background: {B}; color: #FFFFFF; font-size: 21px; font-weight: 700; text-decoration: none">Entrar com gov.br</a>
{p('Mais rápido: seus dados são preenchidos sozinhos.', 16, MUTED, 'text-align: center')}
<div style="display: flex; align-items: center; gap: 10px; color: {MUTED}; font-size: 16px"><span style="flex: 1; height: 1px; background: {LINE}"></span>ou<span style="flex: 1; height: 1px; background: {LINE}"></span></div>
{field('Seu CPF', '000.000.000-00')}
{field('Celular para receber o código', '(62) 9 0000-0000')}
{btn('Receber código por SMS', 'AppCadastro.dc.html', 'ghost')}
<a href="AppAjuda.dc.html" style="text-align: center; font-size: 18px; font-weight: 700; padding: 10px">Preciso de ajuda para entrar</a>
''', header='', bg='#FFFFFF')

# ---------- CADASTRO ----------
screen('AppCadastro.dc.html', 'App — Confirmar dados', f'''
<div style="display: flex; gap: 12px; align-items: center; padding: 14px; border-radius: 18px; background: {GREENBG}; color: #17663A">{ic('check', 28, GREEN, 2.5)}<span style="font-size: 17px; line-height: 1.4"><b>Dados preenchidos pelo gov.br.</b> Confira e corrija se precisar.</span></div>
{field('Nome completo', NOME)}
<div style="display: flex; gap: 10px">{field('CPF', '000.000.000-00', False)}{field('Nascimento', '00/00/0000', False)}</div>
{field('Cartão do SUS', '000 0000 0000 0000')}
{field('Celular (WhatsApp)', '(62) 9 0000-0000')}
<p style="margin: 6px 0 0; font-weight: 700; font-size: 19px">Endereço</p>
{field('Rua', 'Rua [nome]')}
<div style="display: flex; gap: 10px">{field('Número', 'Qd. 00 Lt. 00', False)}{field('Bairro', 'Jardim Nova Abadia', False)}</div>
{field('Ponto de referência', 'Perto da praça')}
<a href="#" style="display: flex; align-items: center; gap: 8px; font-size: 18px; font-weight: 700; padding: 6px 0">{ic('edit', 22)}Prefiro preencher tudo manualmente</a>
{btn('Está tudo certo', 'AppInicio.dc.html', 'green')}
''', header=topo('Seus dados', 'AppLogin.dc.html', 'Passo 2 de 2 · Confirme seus dados', 100))

# ---------- INICIO ----------
tiles = [('Marcar consulta', 'AppConsultaTipo.dc.html', 'heart', True), ('Pedir remédio', 'AppRemedioReceita.dc.html', 'pill', True),
         ('Meus agendamentos', 'AppMeusAgendamentos.dc.html', 'cal', False), ('Meus remédios', 'AppMeusPedidos.dc.html', 'file', False),
         ('Identidade, Vapt Vupt e Junta', 'AppOutrosAgendamentos.dc.html', 'id', False), ('Mais serviços', 'AppOutrosAgendamentos.dc.html', 'grid', False)]
tl = ''
for label, href, icon, main in tiles:
    bg, fg = (B, '#FFFFFF') if main else (LIGHT, B)
    tl += f'<a href="{href}" style="display: flex; flex-direction: column; gap: 10px; padding: 16px; min-height: 124px; box-sizing: border-box; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none"><span style="width: 50px; height: 50px; border-radius: 14px; background: {bg}; display: flex; align-items: center; justify-content: center">{ic(icon, 28, fg)}</span><span style="font-weight: 700; font-size: 19px; line-height: 1.2">{label}</span></a>'
screen('AppInicio.dc.html', 'App — Início', f'''
<div style="display: flex; justify-content: space-between; align-items: center; gap: 10px">
<div><p style="margin: 0; font-size: 17px; color: {MUTED}">Boa noite,</p><p style="margin: 0; font-family: Poppins; font-weight: 700; font-size: 28px">Jhiuliano</p></div>
<div style="display: flex; gap: 8px">
<a href="AppPerfil.dc.html" aria-label="Aumentar a letra" style="display: flex; align-items: center; justify-content: center; width: 54px; height: 54px; box-sizing: border-box; border-radius: 16px; background: #FFFFFF; border: 2px solid {LINE}; font-family: Poppins; font-weight: 700; font-size: 19px; color: {NAVY}; text-decoration: none">A+</a>
<a href="AppNotificacoes.dc.html" aria-label="Notificações, 2 novas" style="position: relative; display: flex; align-items: center; justify-content: center; width: 54px; height: 54px; box-sizing: border-box; border-radius: 16px; background: #FFFFFF; border: 2px solid {LINE}">{ic('bell', 26, NAVY)}<span style="position: absolute; top: -6px; right: -6px; min-width: 24px; height: 24px; border-radius: 12px; background: {RED}; color: #FFFFFF; font-size: 14px; font-weight: 700; display: flex; align-items: center; justify-content: center">2</span></a>
</div></div>
<a href="AppAgendamentoDetalhe.dc.html" style="padding: 18px; border-radius: 20px; background: {B}; color: #FFFFFF; display: flex; flex-direction: column; gap: 4px; text-decoration: none">
<span style="font-size: 16px; color: #D9ECF7">Sua próxima consulta</span>
<span style="font-family: Poppins; font-weight: 700; font-size: 21px">Quarta, 02/12 às 08:30</span>
<span style="font-size: 17px">Clínico geral · Dra. Ana Paula Ribeiro</span>
<span style="font-size: 16px; color: #D9ECF7">UBS Unidade 1</span></a>
<a href="AppStatusRemedio.dc.html" style="display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none">
<span style="width: 46px; height: 46px; border-radius: 14px; background: {AMBERBG}; display: flex; align-items: center; justify-content: center; flex: none">{ic('clock', 26, '#8A6100')}</span>
<span style="flex: 1; display: flex; flex-direction: column"><span style="font-size: 16px; color: {MUTED}">Seu pedido de remédio nº 4821</span><span style="font-weight: 700; font-size: 19px">Farmácia verificando a receita</span></span>{ic('chev', 24, MUTED)}</a>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">{tl}</div>
<a href="AppAjuda.dc.html" style="display: flex; align-items: center; gap: 12px; padding: 16px; border-radius: 20px; background: {AMBERBG}; border: 2px solid #F2D27A; color: #3D2B00; text-decoration: none">{ic('msg', 28, '#6B4A00')}<span style="font-size: 18px; line-height: 1.35"><b>Precisa de ajuda?</b><br>Fale com um atendente</span></a>
''', tab='inicio', gap=14)

# ---------- CONSULTA: TIPO ----------
specs = [('Clínico geral', 'Consulta de rotina, adultos', 'heart'), ('Pediatria', 'Para crianças e adolescentes', 'child'),
         ('Dentista', 'Saúde bucal', 'tooth'), ('Ginecologia', 'Saúde da mulher, pré-natal', 'woman'),
         ('Enfermagem', 'Curativo, vacina, pressão', 'pulse'), ('Psicologia', 'Encaminhamento da UBS', 'user')]
sp = ''
for n, s, i in specs:
    sp += f'<a href="AppConsultaUBS.dc.html" style="display: flex; align-items: center; gap: 14px; min-height: 80px; padding: 12px 16px; box-sizing: border-box; border-radius: 18px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none"><span style="width: 50px; height: 50px; border-radius: 14px; background: {LIGHT}; display: flex; align-items: center; justify-content: center; flex: none">{ic(i, 28)}</span><span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 700; font-size: 20px">{n}</span><span style="font-size: 16px; color: {MUTED}">{s}</span></span>{ic("chev", 24, MUTED)}</a>'
screen('AppConsultaTipo.dc.html', 'App — Tipo de consulta', h2('Com quem você quer consultar?') + sp,
       header=topo('Marcar consulta', 'AppInicio.dc.html', 'Passo 1 de 5 · Tipo de consulta', 20))

# ---------- CONSULTA: UBS ----------
ubs = [('UBS Unidade 1', '1,2 km de você', 'Seg a sex · 7h às 17h', '3 médicos · vagas esta semana', True),
       ('UBS Unidade 2', '2,8 km de você', 'Seg a sex · 7h às 17h', '2 médicos · vagas esta semana', False),
       ('UBS Unidade 3', '4,5 km de você', 'Seg a sex · 7h às 13h', '1 médico · vagas a partir de 07/12', False)]
ub = ''
for n, d, h, m, sel in ubs:
    border = f'3px solid {B}' if sel else f'2px solid {LINE}'
    bg = LIGHT if sel else '#FFFFFF'
    ub += f'''<a href="AppConsultaMedico.dc.html" style="display: flex; flex-direction: column; gap: 6px; padding: 16px; border-radius: 20px; background: {bg}; border: {border}; color: {NAVY}; text-decoration: none">
<span style="display: flex; justify-content: space-between; gap: 8px; align-items: center"><span style="font-weight: 700; font-size: 21px">{n}</span><span style="font-size: 16px; color: {MUTED}">{d}</span></span>
<span style="display: flex; gap: 8px; align-items: center; font-size: 17px">{ic('pin', 20, MUTED)}[Endereço da unidade]</span>
<span style="display: flex; gap: 8px; align-items: center; font-size: 17px">{ic('clock', 20, MUTED)}{h}</span>
<span style="display: flex; gap: 8px; align-items: center; font-size: 17px; font-weight: 700; color: {GREEN}">{ic('check', 20, GREEN, 2.5)}{m}</span></a>'''
screen('AppConsultaUBS.dc.html', 'App — Escolher posto de saúde', h2('Em qual posto de saúde?') + p('Clínico geral · mostrando os mais perto de você') + ub,
       header=topo('Marcar consulta', 'AppConsultaTipo.dc.html', 'Passo 2 de 5 · Posto de saúde', 40))

# ---------- CONSULTA: MEDICO ----------
docs = [('AR', 'Dra. Ana Paula Ribeiro', 'Clínica geral', 'Seg, Qua e Sex · manhã', 'Próxima vaga: Qua, 02/12', GREEN, GREENBG, '12 vagas nas próximas 2 semanas'),
        ('CM', 'Dr. Carlos Eduardo Moura', 'Clínico geral', 'Ter e Qui · manhã e tarde', 'Próxima vaga: Ter, 01/12', GREEN, GREENBG, '8 vagas nas próximas 2 semanas'),
        ('FL', 'Dra. Fernanda Lima', 'Médica da família', 'Seg a Sex · tarde', 'Agenda cheia esta semana', AMBER, AMBERBG, 'Próxima vaga: Seg, 07/12')]
dc = ''
for ini, n, e, dias, prox, fg, bgc, extra in docs:
    dc += f'''<a href="AppConsultaCalendario.dc.html" style="display: flex; gap: 14px; padding: 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; color: {NAVY}; text-decoration: none">
<span style="width: 60px; height: 60px; border-radius: 50%; background: {LIGHT}; color: {B}; font-family: Poppins; font-weight: 700; font-size: 21px; display: flex; align-items: center; justify-content: center; flex: none">{ini}</span>
<span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px"><span style="font-weight: 700; font-size: 20px">{n}</span><span style="font-size: 16px; color: {MUTED}">{e}</span>
<span style="display: flex; gap: 6px; align-items: center; font-size: 17px">{ic('cal', 18, MUTED)}{dias}</span>
<span style="align-self: flex-start; padding: 4px 10px; border-radius: 999px; background: {bgc}; color: {fg}; font-size: 16px; font-weight: 700">{prox}</span><span style="font-size: 15px; color: {MUTED}">{extra}</span></span></a>'''
screen('AppConsultaMedico.dc.html', 'App — Escolher médico', h2('Escolha o médico') + p('UBS Unidade 1 · Clínico geral') + dc +
       f'<a href="AppConsultaCalendario.dc.html" style="text-align: center; font-size: 18px; font-weight: 700; padding: 8px">Tanto faz — quero a primeira vaga</a>',
       header=topo('Marcar consulta', 'AppConsultaUBS.dc.html', 'Passo 3 de 5 · Médico', 60))
print('ok s1')

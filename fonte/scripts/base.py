import os, json
OUT = '/home/claude/canvas/project'
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">'
CSS = """<style>
body{margin:0}
a{color:#005A8E}a:hover{color:#00476F}
button{font-family:inherit;cursor:pointer}
input,textarea,select{font-family:inherit}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{outline:4px solid #FFC83D;outline-offset:2px}
</style>"""

# tokens
B = '#005A8E'; NAVY = '#0B2540'; LIGHT = '#EEF5FA'; LINE = '#D3E2EC'; MUTED = '#4A5B6C'; BG = '#F5F8FA'
GREEN = '#1B7A43'; GREENBG = '#E3F5EA'; AMBERBG = '#FFF6DC'; AMBER = '#5A3E00'; REDBG = '#FDECEC'; RED = '#B42318'

ICON = {
 'heart': 'M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z',
 'pill': 'M10.5 20.5a5 5 0 0 1-7-7l7-7a5 5 0 0 1 7 7zM8.5 8.5l7 7',
 'id': 'M3 5h18v14H3zM7 15h4M7 11h4M16 13a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
 'bldg': 'M4 21V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v16M2 21h20M9 7h2M13 7h2M9 11h2M13 11h2M10 21v-4h4v4',
 'shield': 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z',
 'grid': 'M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z',
 'cal': 'M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z',
 'home': 'M3 10l9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM9 22V12h6v10',
 'user': 'M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z',
 'bell': 'M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 0 1-3.4 0',
 'help': 'M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01',
 'msg': 'M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z',
 'phone': 'M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z',
 'camera': 'M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2zM12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z',
 'file': 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6M8 13h8M8 17h5',
 'truck': 'M1 4h14v12H1zM15 9h4l3 3v4h-7M5.5 21a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM18.5 21a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
 'store': 'M4 21V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v16M2 21h20M10 21v-4h4v4M12 7v6M9 10h6',
 'pin': 'M12 22s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
 'check': 'M20 6L9 17l-5-5',
 'x': 'M18 6L6 18M6 6l12 12',
 'clock': 'M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6v6l4 2',
 'search': 'M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.3-4.3',
 'chev': 'M9 18l6-6-6-6',
 'back': 'M15 18l-6-6 6-6',
 'eye': 'M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z',
 'child': 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM6 21v-2a6 6 0 0 1 12 0v2',
 'tooth': 'M7 3c-2 0-4 2-4 5 0 4 2 5 2 9 0 2 1 4 2 4s2-3 3-6h4c1 3 2 6 3 6s2-2 2-4c0-4 2-5 2-9 0-3-2-5-4-5-2 0-3 1-5 1S9 3 7 3z',
 'woman': 'M12 15a6 6 0 1 0 0-12 6 6 0 0 0 0 12zM12 15v7M9 19h6',
 'pulse': 'M22 12h-4l-3 9L9 3l-3 9H2',
 'qr': 'M3 3h7v7H3zM14 3h7v7h-7zM3 14h7v7H3zM14 14h3v3h-3zM18 18h3v3h-3zM14 19h2M19 14h2',
 'type': 'M4 7V4h16v3M9 20h6M12 4v16',
 'sun': 'M12 17a5 5 0 1 0 0-10 5 5 0 0 0 0 10zM12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2',
 'volume': 'M11 5L6 9H2v6h4l5 4zM15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14',
 'logout': 'M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9',
 'edit': 'M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z',
}

def ic(name, size=26, color=B, sw=2):
    return f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"><path d="{ICON[name]}"></path></svg>'

def badge(text, bg, fg):
    return f'<span style="align-self: flex-start; display: inline-flex; padding: 5px 12px; border-radius: 999px; background: {bg}; color: {fg}; font-size: 16px; font-weight: 700">{text}</span>'

def btn(text, href='#', kind='primary'):
    st = {'primary': f'background: {B}; color: #FFFFFF;', 'green': f'background: {GREEN}; color: #FFFFFF;',
          'ghost': f'background: #FFFFFF; color: {NAVY}; border: 2px solid {LINE};', 'danger': f'background: #FFFFFF; color: {RED}; border: 2px solid #F0B8B3;'}[kind]
    return f'<a href="{href}" style="display: flex; align-items: center; justify-content: center; min-height: 60px; border-radius: 18px; {st} font-size: 20px; font-weight: 700; text-decoration: none; box-sizing: border-box">{text}</a>'

def field(label, value, wide=True):
    return f'<label style="display: flex; flex-direction: column; gap: 6px; font-weight: 700; font-size: 17px; {"" if wide else "flex: 1; min-width: 0"}">{label}<input value="{value}" style="min-height: 56px; width: 100%; box-sizing: border-box; padding: 0 14px; border-radius: 14px; border: 2px solid #8FB3CC; font-size: 19px; color: {NAVY}; background: #FFFFFF"></label>'

def card(inner, extra=''):
    return f'<div style="padding: 16px; border-radius: 20px; background: #FFFFFF; border: 2px solid {LINE}; display: flex; flex-direction: column; gap: 10px; {extra}">{inner}</div>'

def h2(t):
    return f'<h2 style="margin: 0; font-family: Poppins; font-size: 22px; line-height: 1.25; color: {NAVY}">{t}</h2>'

def p(t, size=18, color=MUTED, extra=''):
    return f'<p style="margin: 0; font-size: {size}px; line-height: 1.45; color: {color}; {extra}">{t}</p>'

def topo(titulo, voltar='AppInicio.dc.html', passo='', pct=0):
    bar = ''
    if passo:
        bar = f'''<div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 16px; font-weight: 700; color: {MUTED}">{passo}</span><div style="height: 8px; border-radius: 4px; background: {LINE}"><div style="height: 8px; border-radius: 4px; background: {B}; width: {pct}%"></div></div></div>'''
    return f'''<div style="background: #FFFFFF; border-bottom: 1px solid #DDE6EE; padding: 18px 16px 14px; display: flex; flex-direction: column; gap: 12px; flex: none">
<div style="display: flex; align-items: center; gap: 12px"><a href="{voltar}" aria-label="Voltar" style="width: 52px; height: 52px; box-sizing: border-box; border-radius: 14px; border: 2px solid {LINE}; display: flex; align-items: center; justify-content: center; flex: none">{ic('back', 26, NAVY, 2.5)}</a><h1 style="margin: 0; font-family: Poppins; font-size: 22px; font-weight: 700; color: {NAVY}">{titulo}</h1></div>{bar}</div>'''

TABS = [('Início', 'AppInicio.dc.html', 'home', 'inicio'), ('Agenda', 'AppMeusAgendamentos.dc.html', 'cal', 'agenda'),
        ('Remédios', 'AppMeusPedidos.dc.html', 'pill', 'remedios'), ('Perfil', 'AppPerfil.dc.html', 'user', 'perfil')]

def menu(ativo):
    items = ''
    for label, href, icon, key in TABS:
        c = B if key == ativo else MUTED
        items += f'<a href="{href}" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; min-height: 58px; color: {c}; font-size: 15px; font-weight: 700; text-decoration: none">{ic(icon, 26, c)}{label}</a>'
    return f'<nav aria-label="Menu do aplicativo" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); background: #FFFFFF; border-top: 1px solid #DDE6EE; padding: 6px 6px 12px; flex: none">{items}</nav>'

def screen(fname, title, body, header='', tab=None, script=None, bg=BG, gap=14):
    nav = menu(tab) if tab else ''
    sc = script or "class Component extends DCLogic {\n  renderVals() { return {}; }\n}"
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
{CSS}
</helmet>
<div style="width: 390px; height: 844px; box-sizing: border-box; background: {bg}; color: {NAVY}; font-family: 'Atkinson Hyperlegible', system-ui, sans-serif; font-size: 18px; display: flex; flex-direction: column; overflow: hidden">
{header}
<div style="flex: 1; overflow-y: auto; padding: 20px 16px; display: flex; flex-direction: column; gap: {gap}px">
{body}
</div>
{nav}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":390,"height":844}}}}'>
{sc}
</script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), 'w').write(html)
    return fname

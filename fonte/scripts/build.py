import re, json, base64, os, sys
P = '/home/claude/canvas/project'
L = '/home/claude/logo'
blobs = {}
for f in os.listdir(L):
    if f.endswith('.png') and len(f) > 30:
        blobs[f[:-4]] = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(L, f), 'rb').read()).decode()
icon180 = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(L, 'apple-icon.png'), 'rb').read()).decode()

def load(name):
    s = open(os.path.join(P, name)).read()
    s = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: blobs[m.group(1)], s)
    s = s.replace("'Atkinson Hyperlegible', system-ui", "'Atkinson Hyperlegible', Inter, system-ui")
    xdc = re.search(r'<x-dc>(.*)</x-dc>', s, re.S).group(1)
    helmet = re.search(r'<helmet>(.*?)</helmet>', xdc, re.S)
    css = ''.join(re.findall(r'<style>(.*?)</style>', helmet.group(1), re.S)) if helmet else ''
    tpl = re.sub(r'<helmet>.*?</helmet>', '', xdc, flags=re.S)
    script = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', s, re.S).group(1)
    return {'t': tpl, 's': script}, css

def build(names, start, out, title, mode):
    screens, csss = {}, set()
    for n in names:
        d, c = load(n)
        screens[n[:-8]] = d
        csss.add(re.sub(r'a\{color:[^}]*\}a:hover\{color:[^}]*\}','',c))
    data = json.dumps(screens, ensure_ascii=False).replace('</', '<\\/')
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="theme-color" content="#005A8E">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Abadia Mais">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="apple-touch-icon" href="{icon180}">
<link rel="icon" href="{icon180}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<style>
/* VOICE: serviço público acessível. IDEA: o próprio app da Prefeitura. PICTURE: a tela do app. COLOUR: azul da Prefeitura. TYPE: Atkinson Hyperlegible. LAYOUT: tela cheia no celular, moldura no computador. */
{''.join(csss)}
a{{color:#005A8E}}
html,body{{margin:0;height:100%}}
body{{background:#0B2540;}}
#stage{{min-height:100%;display:flex;align-items:center;justify-content:center}}
#root{{position:relative}}
body.app #root{{border-radius:44px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.45),0 0 0 10px #1c3550}}
body.phone{{background:#F5F8FA}}
body.phone #stage{{display:block;height:100%}}
body.phone #root{{width:100%;height:100%;border-radius:0;box-shadow:none}}
body.phone #root>div{{width:100%!important;height:100%!important;padding-top:max(env(safe-area-inset-top),0px)}}
body.shot{{background:#FFFFFF}}
body.shot #stage{{display:block}}
body.shot #root{{border-radius:0;box-shadow:none}}
body.tall #root>div{{height:auto!important;min-height:844px}}
body.tall #root>div>div{{overflow:visible!important;flex:none!important}}
</style>
</head>
<body class="{mode}">
<div id="stage"><div id="root"></div></div>
<script>
{{
const S = {data};
const START = "{start}";
class DCLogic {{ constructor(p) {{ this.props = p || {{}}; this.state = {{}}; }} setState(o) {{ Object.assign(this.state, typeof o === 'function' ? o(this.state) : o); render(); }} forceUpdate() {{ render(); }} }}
const inst = {{}};
let cur = START;
const HOLE = /\\{{\\{{\\s*([^}}]+?)\\s*\\}}\\}}/g, EXACT = /^\\{{\\{{\\s*([^}}]+?)\\s*\\}}\\}}$/;
function get(sc, p) {{ p = p.trim(); if (p === 'true') return true; if (p === 'false') return false; if (/^-?\\d+(\\.\\d+)?$/.test(p)) return +p; return p.split('.').reduce((o, k) => o == null ? undefined : o[k], sc); }}
function interp(s, sc) {{ return s.replace(HOLE, (m, p) => {{ const v = get(sc, p); return v == null ? '' : String(v); }}); }}
function proc(node, sc) {{
  for (const ch of [...node.childNodes]) {{
    if (ch.nodeType === 3) {{ if (ch.nodeValue.indexOf('{{{{') >= 0) ch.nodeValue = interp(ch.nodeValue, sc); continue; }}
    if (ch.nodeType !== 1) continue;
    const tag = ch.tagName.toLowerCase();
    if (tag === 'sc-for') {{
      const m = EXACT.exec(ch.getAttribute('list') || ''); const list = (m && get(sc, m[1])) || []; const as = ch.getAttribute('as') || 'item';
      const frag = document.createDocumentFragment();
      list.forEach((it, i) => {{ const c = ch.cloneNode(true); proc(c, Object.assign({{}}, sc, {{ [as]: it, $index: i }})); frag.append(...c.childNodes); }});
      ch.replaceWith(frag); continue;
    }}
    if (tag === 'sc-if') {{
      const m = EXACT.exec(ch.getAttribute('value') || ''); const v = m ? get(sc, m[1]) : false;
      if (v) {{ proc(ch, sc); ch.replaceWith(...ch.childNodes); }} else ch.remove();
      continue;
    }}
    for (const a of [...ch.attributes]) {{
      if (a.name.indexOf('hint-') === 0) {{ ch.removeAttribute(a.name); continue; }}
      if (a.value.indexOf('{{{{') < 0) continue;
      const m = EXACT.exec(a.value);
      if (a.name.indexOf('on') === 0) {{ ch.removeAttribute(a.name); const fn = m ? get(sc, m[1]) : null; if (typeof fn === 'function') ch.addEventListener(a.name.slice(2), e => {{ e.preventDefault(); fn(e); }}); continue; }}
      if (m) {{ const v = get(sc, m[1]); if (v === false || v == null) ch.removeAttribute(a.name); else ch.setAttribute(a.name, v === true ? '' : String(v)); }}
      else ch.setAttribute(a.name, interp(a.value, sc));
    }}
    proc(ch, sc);
  }}
}}
function comp(n) {{
  if (!inst[n]) {{ const C = new Function('DCLogic', S[n].s + '\\nreturn Component;')(DCLogic); inst[n] = new C({{}}); if (!inst[n].state) inst[n].state = {{}}; }}
  return inst[n];
}}
const root = document.getElementById('root');
function render() {{
  const c = comp(cur); const vals = c.renderVals();
  const t = document.createElement('template'); t.innerHTML = S[cur].t; proc(t.content, vals);
  root.replaceChildren(t.content);
  document.title = cur.indexOf('App') === 0 ? 'Abadia Mais' : '{title}';
}}
function go(n, push) {{ if (!S[n]) return; cur = n; render(); window.scrollTo(0, 0); if (push && location.hash !== '#' + n) history.pushState(null, '', '#' + n); }}
window.__go = (n, st) => {{ cur = n; const c = comp(n); if (st) Object.assign(c.state, st); render(); }};
document.addEventListener('click', e => {{
  const a = e.target.closest('a'); if (!a) return;
  const h = a.getAttribute('href') || '';
  const m = /^(\\w+)\\.dc\\.html$/.exec(h);
  if (m) {{ e.preventDefault(); go(m[1], true); }}
  else if (h === '#' || h === '') e.preventDefault();
  else if (h[0] === '#') {{ e.preventDefault(); const el = document.getElementById(h.slice(1)); if (el) el.scrollIntoView({{ behavior: 'smooth' }}); }}
}});
document.addEventListener('submit', e => e.preventDefault());
window.addEventListener('hashchange', () => {{ const n = location.hash.slice(1); if (S[n] && n !== cur) go(n, false); }});
if (document.body.classList.contains('app') && window.innerWidth < 560) {{ document.body.classList.remove('app'); document.body.classList.add('phone'); }}
const h0 = location.hash.slice(1); cur = S[h0] ? h0 : START; render();
}}
</script>
</body>
</html>
'''
    open(out, 'w').write(html)
    print(out, len(html))

APP = ['AppAbertura', 'AppLogin', 'AppCadastro', 'AppInicio', 'AppNotificacoes', 'AppPerfil', 'AppAjuda',
       'AppConsultaTipo', 'AppConsultaUBS', 'AppConsultaMedico', 'AppConsultaCalendario', 'AppConsultaConfirmar', 'AppConsultaPronto',
       'AppMeusAgendamentos', 'AppAgendamentoDetalhe', 'AppOutrosAgendamentos', 'AppRemedioReceita', 'AppRemedioPaciente',
       'AppRemedioEntrega', 'AppRemedioConfirmar', 'AppStatusRemedio', 'AppMeusPedidos', 'AppReceitaRecusada']
os.makedirs('/home/claude/out', exist_ok=True)
build([a + '.dc.html' for a in APP], 'AppAbertura', '/home/claude/out/app.html', 'Abadia Mais', 'app')
build([a + '.dc.html' for a in APP] + ['FarmaciaPainel.dc.html', 'SiteHome.dc.html', 'SiteAgendar.dc.html', 'SiteMedicamentos.dc.html'], 'SiteHome', '/home/claude/out/all.html', 'Abadia Mais', 'shot')

"""Monta o site multipáginas da Sala Lume.

Saídas:
  docs/      site estático pronto para hospedar (GitHub Pages: branch main, pasta /docs)
  artifact/  mesma navegação, com CSS e JS embutidos em cada página (não versionado)
"""
import re, pathlib, shutil

R = pathlib.Path(__file__).resolve().parent.parent
S = R / 'src'

logo = (R / 'assets/logo.svg').read_text()
sym = (R / 'assets/simbolo.svg').read_text()
VB = re.search(r'viewBox="([^"]+)"', logo).group(1)
SVB = re.search(r'viewBox="([^"]+)"', sym).group(1)
SALA, LUME = re.findall(r' d="([^"]+)"', logo)
SYM = re.search(r' d="([^"]+)"', sym).group(1)
CSS = (S / 'styles.css').read_text()
JS = (S / 'app.js').read_text()
ICONS = (S / 'icons.svg.part').read_text()

PAGES = [
    # arquivo, rótulo no menu, <title>, descrição
    ('index.html', 'Início', 'Sala Lume', 'Sala de aula inteligente com tela interativa, dispositivos 1:1, agente de IA e correção de provas manuscritas.'),
    ('como-funciona.html', 'Como funciona', 'Como funciona | Sala Lume', 'Ambiente da sala, princípios pedagógicos e o ciclo de aprendizagem da Sala Lume.'),
    ('agente-ia.html', 'Agente de IA', 'Agente de IA | Sala Lume', 'O agente de IA da Sala Lume para alunos, professores e gestão.'),
    ('escrita-a-mao.html', 'Escrita à mão', 'Escrita à mão | Sala Lume', 'Digitalização e diagnóstico de provas e tarefas manuscritas.'),
    ('conteudos.html', 'Conteúdos', 'Conteúdos | Sala Lume', 'Recursos do MEC e acervos educacionais abertos organizados por habilidade.'),
    ('na-escola.html', 'Na escola', 'Na escola | Sala Lume', 'Organização pedagógica, ciclos de revisão e formação docente.'),
    ('contato.html', None, 'Agendar apresentação | Sala Lume', 'Agende uma apresentação da Sala Lume para a sua escola.'),
]

LOGO_SVG = f'<svg viewBox="{VB}" aria-hidden="true"><path fill="var(--logo-sala)" d="{SALA}"/><path fill="#FEAA03" d="{LUME}"/></svg>'


def href(name, mode):
    if name == 'index.html' and mode == 'artifact':
        return './'
    return name


def header(cur, mode):
    links = ''.join(
        f'<a href="{href(f, mode)}"{" aria-current=page" if f == cur else ""}>{label}</a>'
        for f, label, *_ in PAGES if label and f != 'index.html')
    return f'''<header class="top" id="top">
  <div class="wrap">
    <a class="brand" href="{href('index.html', mode)}" aria-label="Sala Lume, página inicial">{LOGO_SVG}</a>
    <button class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Abrir menu"><svg width="22" height="22"><use href="#i-menu"/></svg></button>
    <nav class="nav" id="nav" aria-label="Páginas">{links}</nav>
    <a class="btn btn-cta" href="contato.html">Agendar apresentação</a>
  </div>
</header>'''


def footer(mode):
    links = ''.join(f'<a href="{href(f, mode)}">{label or "Agendar apresentação"}</a>' for f, label, *_ in PAGES)
    return f'''<footer>
  <div class="wrap">
    <a href="{href('index.html', mode)}" class="brand" aria-label="Sala Lume, página inicial">{LOGO_SVG.replace('<svg ', '<svg class="logo" ', 1)}</a>
    <nav aria-label="Rodapé">{links}</nav>
    <small>Sala Lume. Sala de aula inteligente, com o professor no comando.</small>
  </div>
</footer>'''


SUN = '''<svg class="ph-sun" viewBox="0 0 300 170" fill="none" aria-hidden="true">
  <path d="M40 170 A110 110 0 0 1 260 170" stroke="currentColor" stroke-width="16"/>
  <path d="M150 35V15M58 73 44 59M242 73l14-14M24 131l-19-5M276 131l19-5" stroke="currentColor" stroke-width="14" stroke-linecap="round"/>
</svg>'''


def hero(m, mode):
    crumb, h1, lead = m.group(1).split('|')
    return f'''<section class="page-hero" aria-labelledby="ph-t">
  <div class="wrap">
    <p class="crumbs"><a href="{href('index.html', mode)}">Início</a><svg><use href="#i-arrow"/></svg><span aria-current="page">{crumb}</span></p>
    <h1 id="ph-t">{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>'''



CTA = '''<section class="section tight" aria-labelledby="cta-t">
  <div class="wrap">
    <div class="cta-strip">
      <div><h2 id="cta-t">Quer ver a Sala Lume funcionando?</h2><p>Agende uma apresentação para a equipe da sua escola.</p></div>
      <a class="btn btn-cta" href="contato.html">Agendar apresentação</a>
    </div>
  </div>
</section>'''

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600&family=Source+Sans+3:wght@400;600;700&family=Caveat:wght@500&display=swap">'''


def render(f, title, desc, mode, fragment_only):
    body = (S / 'pages' / f).read_text()
    body = re.sub(r'\{\{HERO:(.+?)\}\}', lambda m: hero(m, mode), body)
    body = body.replace('{{CTA}}', CTA)
    icons = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="sol" viewBox="{SVB}"><path fill="currentColor" d="{SYM}"/></symbol>
{ICONS}</defs></svg>'''
    inner = f'{icons}\n{header(f, mode)}\n<main>\n{body}\n</main>\n{footer(mode)}\n'
    if mode == 'site':
        style, script = '<link rel="stylesheet" href="styles.css">', '<script src="app.js"></script>'
    else:
        style, script = f'<style>{CSS}</style>', f'<script>{JS}</script>'
    head = f'<title>{title}</title>\n<meta name="description" content="{desc}">\n'
    if fragment_only:  # página principal do Artifact: o esqueleto é adicionado na publicação
        return f'{head}<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n{style}\n{inner}{script}\n'
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
{head}<link rel="icon" href="{'assets/' if mode == 'site' else ''}simbolo.svg" type="image/svg+xml">
{FONTS}
{style}
</head>
<body>
{inner}{script}
</body>
</html>
'''


for mode in ('site', 'artifact'):
    out = R / ('docs' if mode == 'site' else mode)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir()
    for f, _, title, desc in PAGES:
        (out / f).write_text(render(f, title, desc, mode, mode == 'artifact' and f == 'index.html'))
    if mode == 'site':
        (out / 'styles.css').write_text(CSS)
        (out / 'app.js').write_text(JS)
        shutil.copytree(R / 'assets', out / 'assets')
    else:
        shutil.copy(R / 'assets/simbolo.svg', out / 'simbolo.svg')
print('ok')

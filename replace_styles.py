import re

with open('backend/app/static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Body class update
html = re.sub(
    r'<body class="([^"]*)"',
    r'<body class="\1 dark font-light tabular-nums"',
    html
)

# Colors
html = html.replace('bg-navy-950', 'bg-bg')
html = re.sub(r'bg-navy-(900|850)(/[0-9]+)?', 'bg-surface', html)
html = re.sub(r'bg-navy-(800|700)(/[0-9]+)?', 'bg-surface-2', html)
html = html.replace('bg-ocean-600', 'bg-accent text-accent-ink')
html = html.replace('bg-cyan-500', 'bg-accent text-accent-ink')
html = html.replace('bg-cyan-600', 'bg-accent text-accent-ink')
html = html.replace('border-cyan-400/60', 'border-hairline')
html = html.replace('border-cyan-500/30', 'border-hairline')

html = re.sub(r'text-slate-[12]00', 'text-ink', html)
html = re.sub(r'text-slate-300', 'text-muted', html)
html = re.sub(r'text-slate-[456]00', 'text-muted-2', html)

html = re.sub(r'text-cyan-[345]00', 'text-accent', html)

html = re.sub(r'border-navy-[78]00(/[0-9]+)?', 'border-hairline', html)
html = re.sub(r'border-navy-[56]00', 'border-hairline-strong', html)

# Gradients
html = re.sub(r'bg-gradient-to-[a-z]+', 'bg-accent', html)
html = re.sub(r'from-[a-z]+-[0-9]+', '', html)
html = re.sub(r'to-[a-z]+-[0-9]+', '', html)
html = html.replace('text-transparent bg-clip-text', '')

# Fonts
html = html.replace('font-semibold', 'font-bold')
html = html.replace('font-medium', 'font-bold')
html = html.replace('font-black', 'font-bold')
html = html.replace('font-mono', 'font-pixel')

# Specific typography for POLARIS wordmark, simulation mode badge, and primary CTAs
html = html.replace('>POLARIS</span>', ' class="font-pixel text-[14px] tracking-tight">POLARIS</span>')
html = html.replace('>Simulation Mode</span>', ' class="font-pixel text-[9px]">Simulation Mode</span>')
html = html.replace('>APPLY FILTERS</button>', ' class="font-pixel text-[10px]">APPLY FILTERS</button>')

with open('backend/app/static/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import os, re

files = ['index.html', 'termos.html', 'privacidade.html', 'beneficios.html', 'planos.html', 'contato.html']
brand_text = '<span class="ml-3 text-xl font-bold text-white uppercase tracking-tight font-display">Ronda<span class="text-primary">Track</span></span>'

logo_pattern = re.compile(r'(<a href="index\.html"[^>]*>\s*<img[^>]*>)')

for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if brand text is already there to avoid duplicate insertions
        if 'Ronda<span class="text-primary">Track</span>' in content:
            print(f'Skipping {fn}, already updated.')
            continue

        new_content = logo_pattern.sub(r'\1' + brand_text, content)
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {fn}')

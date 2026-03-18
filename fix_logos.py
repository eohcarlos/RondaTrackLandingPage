import re

# Read index.html
with open('c:\\Users\\Carlos\\Documents\\Website\\index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find the logo src in index.html - it might be slightly different in format
match = re.search(r'<img alt="RondaTrack Logo" class="[^"]*" src="(data:image/[^"]+)"', index_content)
if match:
    src_val = match.group(1)
    
    files_to_update = [
        'c:\\Users\\Carlos\\Documents\\Website\\termos.html',
        'c:\\Users\\Carlos\\Documents\\Website\\privacidade.html',
        'c:\\Users\\Carlos\\Documents\\Website\\beneficios.html',
        'c:\\Users\\Carlos\\Documents\\Website\\planos.html',
        'c:\\Users\\Carlos\\Documents\\Website\\contato.html'
    ]
    for file in files_to_update:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the placeholder src="logo.jpeg" with the actual base64 string
        content = content.replace('src="logo.jpeg"', f'src="{src_val}"')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    print("Logos updated successfully.")
else:
    print("Logo base64 string not found in index.html.")

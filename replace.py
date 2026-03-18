import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Navbar logo link
html = html.replace('<div class="flex items-center cursor-pointer h-full">', '<a href="index.html" class="flex items-center cursor-pointer h-full">')
# 2. Navbar links
html = html.replace('href="#inicio"', 'href="index.html"')
html = html.replace('href="#beneficios"', 'href="beneficios.html"')
html = html.replace('href="#planos"', 'href="planos.html"')
html = html.replace('href="#contato"', 'href="contato.html"')
# 3. Navbar Começar Agora button
html = html.replace('''<button class="px-6 py-2.5 bg-primary hover:bg-primary/90 text-white text-sm font-bold rounded-lg transition-all neon-glow">
                    Começar Agora
                </button>''', '''<a href="http://wa.me/5511941628487" target="_blank" class="px-6 py-2.5 bg-primary hover:bg-primary/90 text-white text-sm font-bold rounded-lg transition-all neon-glow inline-flex items-center justify-center">
                    Começar Agora
                </a>''')
# 4. Hero buttons
html = html.replace('''<button class="px-8 py-4 bg-primary text-white font-bold rounded-xl hover:scale-105 transition-all neon-glow flex items-center justify-center gap-2">
                Começar Agora <span class="material-symbols-outlined text-lg">arrow_forward</span>
</button>
<button class="px-8 py-4 bg-white/5 border border-white/10 text-white font-bold rounded-xl hover:bg-white/10 transition-colors flex items-center justify-center gap-2">
                Falar no WhatsApp
            </button>''', '''<a href="http://wa.me/5511941628487" target="_blank" class="px-8 py-4 bg-primary text-white font-bold rounded-xl hover:scale-105 transition-all neon-glow flex items-center justify-center gap-2">
                Começar Agora <span class="material-symbols-outlined text-lg">arrow_forward</span>
</a>
<a href="http://wa.me/5511941628487" target="_blank" class="px-8 py-4 bg-white/5 border border-white/10 text-white font-bold rounded-xl hover:bg-white/10 transition-colors flex items-center justify-center gap-2">
                Falar no WhatsApp
            </a>''')

# 5. Planos Assinar Agora buttons
html = html.replace('''<button class="w-full py-3 bg-white/5 border border-white/10 hover:bg-white/10 rounded-xl font-bold transition-all">Assinar Agora</button>''', '''<a href="http://wa.me/5511941628487" target="_blank" class="w-full py-3 bg-white/5 border border-white/10 hover:bg-white/10 rounded-xl font-bold transition-all block text-center">Assinar Agora</a>''')
html = html.replace('''<button class="w-full py-3 bg-primary text-white rounded-xl font-bold transition-all neon-glow">Assinar Agora</button>''', '''<a href="http://wa.me/5511941628487" target="_blank" class="w-full py-3 bg-primary text-white rounded-xl font-bold transition-all neon-glow block text-center">Assinar Agora</a>''')

# 6. CTA Final buttons
html = html.replace('''<button class="px-10 py-5 bg-primary text-white font-bold rounded-2xl hover:scale-105 transition-transform neon-glow text-lg">
                    Começar Agora
                </button>
<button class="px-10 py-5 bg-white/5 border border-white/10 text-white font-bold rounded-2xl hover:bg-white/10 transition-colors text-lg">
                    Falar no WhatsApp
                </button>''', '''<a href="http://wa.me/5511941628487" target="_blank" class="px-10 py-5 bg-primary text-white font-bold rounded-2xl hover:scale-105 transition-transform neon-glow text-lg inline-flex items-center justify-center">
                    Começar Agora
                </a>
<a href="http://wa.me/5511941628487" target="_blank" class="px-10 py-5 bg-white/5 border border-white/10 text-white font-bold rounded-2xl hover:bg-white/10 transition-colors text-lg inline-flex items-center justify-center">
                    Falar no WhatsApp
                </a>''')

# 7. Footer Logo link
html = html.replace('''<div class="flex items-center">
<img alt="RondaTrack Logo"''', '''<a href="index.html" class="flex items-center">
<img alt="RondaTrack Logo"''')

# Fix closing div for logo
html = html.replace('</div>\n<div class="hidden md:flex', '</a>\n<div class="hidden md:flex')
html = html.replace('</div>\n<p class="text-slate-400', '</a>\n<p class="text-slate-400')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")

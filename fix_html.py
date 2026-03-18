import sys

with open('C:/Users/Carlos/Documents/Website/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<!DOCTYPE', 10)
if idx != -1:
    content = content[:idx]

footer_addition = """<a class="hover:text-white" href="#">Termos de Uso</a>
<a class="hover:text-white" href="#">Privacidade</a>
</div>
</div>
</footer>
<script>
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuIcon = mobileMenuBtn.querySelector('.material-symbols-outlined');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    if(mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            if (mobileMenu.classList.contains('hidden')) {
                mobileMenuIcon.textContent = 'menu';
            } else {
                mobileMenuIcon.textContent = 'close';
            }
        });
    }

    if(mobileLinks) {
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenuIcon.textContent = 'menu';
            });
        });
    }
</script>
</body>
</html>"""

content += footer_addition
with open('C:/Users/Carlos/Documents/Website/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("HTML structure and script fixed successfully.")

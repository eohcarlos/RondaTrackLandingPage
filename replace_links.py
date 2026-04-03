
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('href="index.html"', 'href="#inicio"')
content = content.replace('href="contato.html"', 'href="#contato"')

# Note: The logo also has `<a ... href="index.html">`. Since that is a logo, linking to `#inicio` is fine.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Links updated")


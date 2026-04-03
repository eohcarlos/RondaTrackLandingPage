
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add AOS to headers (h2)
html = re.sub(r'<h2(\s+class=".*?")>', r'<h2 data-aos="fade-up" \1>', html)

# Add AOS to glass-cards (benefits and plans)
cards = re.finditer(r'<div(\s+class="[^"]*glass-card[^"]*")>', html)

new_html = ""
last_end = 0
delay = 0
last_section_index = 0

for match in cards:
    start = match.start()
    
    # Reset delay if it's a new section finding by distance
    if start - last_section_index > 1000:
        delay = 0
    else:
        delay += 100
    
    last_section_index = start
    
    new_html += html[last_end:start]
    
    if "data-aos" not in match.group(0):
        new_html += f'<div data-aos="fade-up" data-aos-delay="{delay}"{match.group(1)}>'
    else:
        new_html += match.group(0)
    
    last_end = match.end()

new_html += html[last_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("AOS added")


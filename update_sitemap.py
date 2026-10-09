import os
import datetime

base_dir = os.getcwd()
sitemap_path = os.path.join(base_dir, 'sitemap.xml')
new_urls = [
    ('konya-trabzon-cenaze-nakli.html', '2026-10-01'),
    ('konya-denizli-cenaze-nakli.html', '2026-10-01'),
]

with open(sitemap_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the index of the line containing '</urlset>'
# Assuming it's the last line or near last.
# We'll insert before that line.
new_lines = []
for line in lines:
    new_lines.append(line)
    if line.strip() == '</urlset>':
        # Actually we want to insert before this line, so we need to step back.
        # Better: we'll build a list and insert before the last occurrence.
        pass

# Simpler: read entire content, replace before </urlset>
with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert new url entries before the closing tag
insertion = ''
for url, date in new_urls:
    insertion += f'  <url><loc>https://www.konyacenazehizmetleri.com/blog/{url}</loc><lastmod>{date}</lastmod><priority>0.8</priority></url>\n'

# Replace the last occurrence of '</urlset>' with insertion + '</urlset>'
# We'll split at the last occurrence.
if content.endswith('</urlset>'):
    # Insert before the final closing tag
    content = content[:-len('</urlset>')] + insertion + '</urlset>'
else:
    # Find last occurrence
    pos = content.rfind('</urlset>')
    if pos != -1:
        content = content[:pos] + insertion + content[pos:]
    else:
        # fallback: append at end
        content = content + insertion

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Sitemap updated.')

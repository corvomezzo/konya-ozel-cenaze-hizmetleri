import os
import re

def normalize_turkish(s):
    mapping = str.maketrans({
        'Ç':'C','ç':'c',
        'Ğ':'G','ğ':'g',
        'İ':'I','ı':'i',
        'Ö':'O','ö':'o',
        'Ş':'S','ş':'s',
        'Ü':'U','ü':'u',
    })
    return s.translate(mapping).lower()

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

def generate_blog(template_content, city_name, slug):
    # Replace slug (lowercase)
    new_content = template_content.replace('ankara', slug)  # careful: might replace parts of other words? ankara is unique.
    # Replace city name (as appears in template: "Ankara")
    new_content = new_content.replace('Ankara', city_name)
    return new_content

def main():
    base_dir = os.getcwd()
    template_path = os.path.join(base_dir, 'blog', 'konya-ankara-cenaze-nakli.html')
    template = read_file(template_path)
    
    # Read done and sirada
    done_path = os.path.join(base_dir, 'blog', 'done.txt')
    sirada_path = os.path.join(base_dir, 'blog', 'sirada.txt')
    
    with open(done_path, 'r', encoding='utf-8') as f:
        done_set = set(line.strip() for line in f if line.strip())
    
    pending = []
    with open(sirada_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    for line in lines:
        city = line.strip()
        if not city:
            continue
        slug = normalize_turkish(city)
        if slug not in done_set:
            pending.append((city, slug))
        if len(pending) >= 2:
            break
    
    if not pending:
        print('No pending cities')
        return
    
    generated = []
    for city, slug in pending:
        new_filename = f'konya-{slug}-cenaze-nakli.html'
        new_path = os.path.join(base_dir, 'blog', new_filename)
        content = generate_blog(template, city, slug)
        write_file(new_path, content)
        generated.append((city, slug))
        print(f'Generated: {new_path}')
    
    # Update sirada.txt: remove the processed cities
    remaining = []
    for line in lines:
        city = line.strip()
        if not city:
            continue
        slug = normalize_turkish(city)
        if any(slug == p[1] for p in pending):
            # skip this city
            continue
        remaining.append(line)
    with open(sirada_path, 'w', encoding='utf-8') as f:
        f.writelines(remaining)
    
    # Append to done.txt
    with open(done_path, 'a', encoding='utf-8') as f:
        for city, slug in pending:
            f.write(slug + '\n')
    
    print('Done.')

if __name__ == '__main__':
    main()

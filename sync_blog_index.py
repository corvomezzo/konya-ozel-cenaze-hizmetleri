"""index.html + sitemap.xml blog linklerini diskteki HTML dosyalarindan turet.

Neden bu script var: cron job'i HTML uretiyor ama index/sitemap guncellemesi
manuel yapildigi icin yeni sayfalar Google'a hic bildirilmiyordu. Bu script
sifir hardcode ile calisir: sehir listesini blog/ klasorunden okur.

Kullanim:  python sync_blog_index.py [--dry-run]
"""
import os
import re
import sys
import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
BLOG_DIR = os.path.join(BASE, "blog")
SITE = "https://www.konyacenazehizmetleri.com"


def slug_to_display(slug):
    """konya-canakkale-cenaze-nakli -> Canakkale"""
    return slug.replace("konya-", "").replace("-cenaze-nakli", "").title()


def collect_blogs():
    """Diskteki blog HTML'lerinden slug + gecerli tarih topla."""
    rows = []
    for name in sorted(os.listdir(BLOG_DIR)):
        if not (name.startswith("konya-") and name.endswith("-cenaze-nakli.html")):
            continue
        slug = name.replace("konya-", "").replace("-cenaze-nakli.html", "")
        path = os.path.join(BLOG_DIR, name)
        with open(path, "r", encoding="utf-8") as f:
            head = f.read(3000)
        m = re.search(r"<title>Konya\s*[–-]\s*(.+?)\s*(Arası Cenaze Nakli|Cenaze Nakli)", head)
        city = slug_to_display(slug) if not m else m.group(1).strip()
        date = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
        rows.append((name, city, date))
    return rows


def sync_index(blogs):
    """Eksik blog linklerini index.html'in city-grid listesine ekle."""
    path = os.path.join(BASE, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    existing = set(re.findall(r"konya-[a-z]+-cenaze-nakli\.html", html))
    missing = [b for b in blogs if b[0] not in existing]
    if not missing:
        return 0

    new_items = "".join(
        f'<li><a href="blog/{name}">Konya – {city} Arası Cenaze Nakli</a></li>'
        for name, city, _ in missing
    )
    html = html.replace("</ul><p class=\"city-note\"", new_items + "</ul><p class=\"city-note\"", 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return len(missing)


def sync_sitemap(blogs):
    """Eksik blog URL'lerini sitemap.xml'e ekle."""
    path = os.path.join(BASE, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()

    have = set(re.findall(r"blog/(konya-[a-z]+-cenaze-nakli\.html)", xml))
    missing = [b for b in blogs if b[0] not in have]
    if not missing:
        return 0

    block = "".join(
        f'  <url><loc>{SITE}/blog/{name}</loc><lastmod>{date}</lastmod>'
        f'<priority>0.8</priority></url>\n'
        for name, _, date in missing
    )
    pos = xml.rfind("</urlset>")
    xml = xml[:pos] + block + xml[pos:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(xml)
    return len(missing)


def main():
    dry = "--dry-run" in sys.argv
    blogs = collect_blogs()
    print(f"Diskteki blog sayfasi: {len(blogs)}")

    i = sync_index(blogs)
    s = sync_sitemap(blogs)
    verb = "eklenecek" if dry else "eklendi"
    print(f"index.html: {i} link {verb}")
    print(f"sitemap.xml: {s} URL {verb}")


if __name__ == "__main__":
    main()
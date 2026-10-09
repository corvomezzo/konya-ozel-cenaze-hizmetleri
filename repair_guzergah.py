"""16 blog sayfasindaki kalan gecersiz gecis metnini hedef sehrin gercek
guzergah/suresiyle degistirir.

Iki hata turu var:
1) "X'in ilceleri" -> "..." parantez ici ilce listesi (16 dosyada birakmis Ankara listesi)
2) Ana metindeki "Turkiye'nin en kisa sehirler arasi hatlarindan biridir. X'a
   baglanti Konya-X karayolu (D-715) uzerinden saglanir; ortalama 3,5-4,5
   saatlik..." blogu -> hedef ilin gercek guzergahi ve suresi.

Kullanim: python repair_guzergah.py [--dry-run]
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(BASE, "blog")
ILCE = json.load(open(os.path.join(BLOG, "ilce_listeleri.json"), encoding="utf-8"))
CITY = __import__("city_data_fix").CITY

# Ana metindeki bozuk giris blogu (16 dosyada ayni kalmis)
BOZUK_GIRIS = re.compile(
    r"güzergâhı Türkiye'nin en kısa şehirler arası hatlarından biridir\. "
    r"(\w+)'?[a-z]* bağlantı Konya–[\wşŞğıİ]+(?:–\w+)* karayolu \(D-\d+\) "
    r"üzerinden sağlanır; ortalama [\d.,–\-]+ saatlik bir yolculuk planlanır\."
)

# Karsiligi: ilk cumlenin devami. "en kisa" iddiasi yanlis oldugu icin
# notr bir ifadeye cevrilir ve gercek sure yazilir.
def giris_metin(ad, guzergah, sure):
    return (f"güzergâhı Türkiye'nin ana ulaşım akslarından biridir. "
            f"Bağlantı {guzergah} üzerinden sağlanır; "
            f"ortalama {sure} saatlik bir yolculuk planlanır.")


def main():
    dry = "--dry-run" in sys.argv
    print(f"{'slug':16} {'n':>3}  giris")
    toplam = 0

    for slug, (ad, sure, guzergah, _mezarlik) in CITY.items():
        path = os.path.join(BLOG, f"konya-{slug}-cenaze-nakli.html")
        if not os.path.exists(path):
            continue
        html = open(path, encoding="utf-8").read()
        orig = html
        ilceler = ILCE.get(ad, [])

        # 1) Ana metindeki bozuk giris blogu
        def sub(m):
            return giris_metin(ad, guzergah, sure)
        yeni = BOZUK_GIRIS.sub(sub, html)
        giris_ok = yeni != html
        html = yeni

        # 2) Parantez ici ilce listesi ("(Ilce1, Ilce2, ...) Ko..." kalibi)
        def parantez(m):
            return "(" + ", ".join(ilceler[:8]) + ")"
        yeni = re.sub(
            r"\((?:Çankaya|[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)(?:,\s*[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)*"
            r"(?:\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)?\)\s*(?=Konya'ya|Konya’dan|Konya'dan)",
            parantez, html)
        par_ok = yeni != html
        html = yeni

        # 3) FAQ'da ayni surenin karsiligi ("3,5-4,5 saatlik") kontrol
        yeni = re.sub(r"ortalama 3,5–4,5 saatlik", f"ortalama {sure} saatlik", html)
        sure_ok = yeni != html
        html = yeni

        if html != orig:
            if not dry:
                open(path, "w", encoding="utf-8").write(html)
            toplam += 1

        isaretler = ",".join(x for x, ok in
                             (("giris", giris_ok), ("parantez", par_ok), ("sure", sure_ok)) if ok)
        print(f"{slug:16} {len(ilceler):>3}  {isaretler or '-'}")

    print(f"\n{'DRY-RUN: ' if dry else ''}{toplam}/16 dosya guncellendi")

    # Bagimsiz kontrol: hicbir dosyada "en kisa" veya "D-715" kalmamali
    kalan = []
    for slug in CITY:
        p = os.path.join(BLOG, f"konya-{slug}-cenaze-nakli.html")
        t = open(p, encoding="utf-8").read()
        if "en kısa şehirler arası" in t or "D-715" in t or "3,5–4,5" in t:
            kalan.append(slug)
    print(f"Bozuk giris kalinti: {len(kalan)} {kalan}")


if __name__ == "__main__":
    main()
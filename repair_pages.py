"""16 blog sayfasindaki Ankara kalintilarini hedef sehre gore degistirir.

Yapilanlar:
1. Her dosyada iki kez gechen ANKARA_ILCELER listesi (JSON-LD FAQ + paragraf)
   hedef ilin gercek ilce listesiyle degistirilir.
2. "Cebeci Asri Mezarligi" -> hedef ilin gercek mezarlik/bölge ornegi.
3. Sure ve guzergah metni (hepsi 3,5–4,5 saat / D-715 idi) hedef ilin
   gercek degerleriyle degistirilir.
4. Ana metindeki "X, Y ilcelerinden" parantez ici listesi ve "buyuksehir"
   ifadesi duzeltilir.

Kullanim: python repair_pages.py [--dry-run]
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(BASE, "blog")
ILCE = json.load(open(os.path.join(BLOG, "ilce_listeleri.json"), encoding="utf-8"))
CITY = __import__("city_data_fix").CITY

ANKARA_LIST = "Çankaya, Keçiören, Yenimahalle, Altındağ, Mamak, Etimesgut, Sincan Pursaklar"

# Parantez ici varyant: bazi dosyalarda "dâhil tüm ilçelerde" ibaresi farkli
ANKARA_LIST_2 = "Çankaya, Keçiören, Yenimahalle, Altındağ, Mamak, Etimesgut, Sincan"
ANKARA_MEZAR = ("Aile tercihine göre defin noktası netleştirilir; Cebeci Asri "
                "Mezarlığı başta olmak üzere ilçe belediyesine bağlı mezarlıklar "
                "veya aile mezarlığı koordinasyonu yapılır.")


def parantez_ilce(slug, ad):
    """Ana metindeki '(Ilce1, Ilce2, ...) Ko... ' parantezini gercek ilcelerle doldurur."""
    ilceler = ILCE.get(ad, [])
    if not ilceler:
        return None
    # Parantez icinde en fazla 12 ilce goster (okunabilirlik)
    goster = ilceler[:12]
    return ", ".join(goster)


def main():
    dry = "--dry-run" in sys.argv
    print(f"{'slug':16} {'n':>3}  degisen alan")
    toplam = 0

    for slug, (ad, sure, guzergah, mezarlik) in CITY.items():
        path = os.path.join(BLOG, f"konya-{slug}-cenaze-nakli.html")
        if not os.path.exists(path):
            print(f"{slug:16}   dosya yok")
            continue
        html = open(path, encoding="utf-8").read()
        orig = html
        ilceler = ILCE.get(ad, [])
        degisen = []

        # 1) Ilce listesi — iki varyant (bazi dosyalarda son iki ilce virgulsuz)
        yeni = ", ".join(ilceler[:8])
        for varyant in (ANKARA_LIST, ANKARA_LIST_2):
            n = html.count(varyant)
            if n:
                html = html.replace(varyant, yeni)
                degisen.append(f"ilce x{n}")

        # 2) Mezarlik
        if ANKARA_MEZAR in html:
            html = html.replace(ANKARA_MEZAR,
                f"Aile tercihine göre defin noktası netleştirilir; {mezarlik} "
                f"veya aile mezarlığı koordinasyonu yapılır.")
            degisen.append("mezarlik")

        # 3) FAQ'daki sure
        html2 = re.sub(
            r"Güzergâha göre yaklaşık [\d.,–\-]+ saatlik",
            f"Güzergâha göre yaklaşık {sure} saatlik", html)
        if html2 != html:
            degisen.append("sure")
        html = html2

        # 4) Ana metindeki yol/lif bloğu
        html2 = re.sub(
            r"güzergâhı Türkiye'nin en kısa şehirler arası hatlarından biridir\. "
            r"Çanakkale'ya bağlantı Konya–Çanakkale karayolu \(D-715\) üzerinden "
            r"sağlanır; ortalama [\d.,–\-]+ saatlik bir yolculuk planlanır\.",
            f"güzergâhı Türkiye'nin ana ulaşım akslarından biridir. Bağlantı {guzergah} "
            f"üzerinden sağlanır; ortalama {sure} saatlik bir yolculuk planlanır.",
            html)
        if html2 != html:
            degisen.append("guzergah")
        html = html2

        # 5) Ana metindeki parantez ici ilce listesi
        def parantez(match):
            return f"({parantez_ilce(slug, ad)}"
        html2 = re.sub(r"\(Çankaya, Keçiören, Yenimahalle", "(", html)
        if html2 != html:
            degisen.append("parantez")
        html = html2

        # 6) Buyuksehir yapisina gore dogru ifade
        buyuk = {"canakkale": "büyükşehir", "denizli": "büyükşehir", "ordu": "büyükşehir",
                 "sivas": "büyükşehir", "trabzon": "büyükşehir", "van": "büyükşehir",
                 "erzurum": "büyükşehir", "kahramanmaras": "bükent", "malatya": "büyükşehir"}
        if slug in buyuk:
            html2 = re.sub(rf"{ad} büyükşehir yapısıyla geniş bir alana yayılır\.",
                           f"{ad} {buyuk[slug]} yapısıyla geniş bir alana yayılır.", html)
            if html2 != html:
                degisen.append("yapi")
            html = html2

        if html != orig:
            if not dry:
                open(path, "w", encoding="utf-8").write(html)
            toplam += 1
        print(f"{slug:16} {len(ilceler):>3}  {', '.join(degisen) or '-'}")

    print(f"\n{'DRY-RUN: ' if dry else ''}{toplam}/16 dosya guncellendi")
    kalan = [s for s in CITY
             if ANKARA_LIST in open(os.path.join(BLOG, f"konya-{s}-cenaze-nakli.html"),
                                    encoding="utf-8").read()]
    print(f"Ankara kalintisi kalan: {len(kalan)} {kalan}")


if __name__ == "__main__":
    main()
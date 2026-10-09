"""16 bozuk blog sayfasindaki Ankara kalintilarini dogru veriyle degistirir.

Koken neden: cron job'i referans dosyayi kopyalayip icindeki Ankara ilcelerini
(Cankaya, Kecioren, ...) ve "Cebeci Asri Mezarligi"ni hedef sehir disinda
birakmisti. Bu script o alanlari hedef sehre gore yeniden yazar.

Veri kaynagi: tr.wikipedia.org "Turkiye'nin ilceleri" sayfasindaki tablo
(ilce sayilari Icisleri Bakanligi ile uyumlu). Arti anahtarli sozluk,
tek seferlik onarim icin; blog sayfalari uretilirken kullanilmaz.
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(BASE, "blog")
WIKI = os.path.join(BASE, "iller.json")

# slug -> (gorunen ad, ortalama sure, guzergah metni, mezarlik ornegi)
# DIKKAT: "ad" alani Wikipedia anahtariyla BITBIT ayni olmali (ornek "Adıyaman" nokta i).
CITY = {
    "adiyaman":        ("Adıyaman", "8–9",    "Konya–Afyon–Eğirdir–Antalya–Adıyaman karayolu (D-650)", "Besni, Kahta, Gölbaşı bölgesi"),
    "afyonkarahisar":  ("Afyonkarahisar", "3–4", "Konya–Afyonkarahisar karayolu (D-300)", "Sandıklı, Dazkırı, İscehisar bölgesi"),
    "batman":         ("Batman", "11–12", "Konya–Aksaray–Niğde–Batman karayolu güzergâhı", "Beşiri, Hasuni bölgesi"),
    "canakkale":       ("Çanakkale", "5–6", "Konya–Eskişehir–Bursa–Çanakkale karayolu (D-200 / D-550)", "Bayramiç, Ezine, Biga bölgesi"),
    "denizli":        ("Denizli", "4–5", "Konya–Çivril–Denizli karayolu (D-585)", "Acıpayam, Babadağ, Çal bölgesi"),
    "elazig":         ("Elazığ", "10–11", "Konya–Sivas–Malatya–Elazığ karayolu güzergâhı", "Kovancılar, Karakoçan, Palu bölgesi"),
    "erzurum":        ("Erzurum", "13–14", "Konya–Sivas–Erzincan–Erzurum karayolu güzergâhı", "Pasinler, Oltu, Tortum bölgesi"),
    "eskisehir":      ("Eskişehir", "4–5", "Konya–Eskişehir karayolu (D-765)", "Sivrihisar, Çifteler, Mihalgazi bölgesi"),
    "kahramanmaras":  ("Kahramanmaraş", "9–10", "Konya–Kahramanmaraş karayolu güzergâhı", "Elbistan, Afşin, Göksun bölgesi"),
    "malatya":        ("Malatya", "8–9", "Konya–Kayseri–Malatya karayolu güzergâhı", "Darende, Hekimhan, Kuluncak bölgesi"),
    "mardin":         ("Mardin", "12–13", "Konya–Şanlıurfa–Mardin karayolu güzergâhı", "Kızıltepe, Nusaybin, Derik bölgesi"),
    "ordu":           ("Ordu", "9–10", "Konya–Sivas–Tokat–Ordu karayolu güzergâhı", "Akkuş, Ünye, Perşembe bölgesi"),
    "sivas":          ("Sivas", "5–6", "Konya–Sivas karayolu (D-850)", "Şarkışla, Hafik, Suşehri bölgesi"),
    "tokat":          ("Tokat", "6–7", "Konya–Sivas–Tokat karayolu güzergâhı", "Niksar, Erbaa, Turhal bölgesi"),
    "trabzon":        ("Trabzon", "12–13", "Konya–Sivas–Tokat–Trabzon karayolu güzergâhı", "Of, Vakfıkebir, Sürmene bölgesi"),
    "van":            ("Van", "12–13", "Konya–Bitlis–Van karayolu güzergâhı", "Erciş, Muradiye, Gevaş bölgesi"),
}

# Ankara'nin birakmis oldugu ilce listesi (JSON-LD + paragraf ayni metni kullanir)
ANKARA_ILCELER = "Çankaya, Keçiören, Yenimahalle, Altındağ, Mamak, Etimesgut, Sincan, Pursaklar"


def load_wiki():
    """Wikipedia wikitext'inden {il: [ilceler]} sozlugu kurar."""
    raw = json.load(open(WIKI, encoding="utf-8"))["parse"]["wikitext"]
    raw = raw[raw.find("İlçelerin listesi"):]

    cities, cur = {}, None
    for line in raw.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        # Ilce sutunu: kalin ve tek hucrede (bob ilk sutun, ilk veri satiri haric)
        if s.startswith("|'''") or s.startswith("| '''[["):
            body = re.sub(r"^['|\s]+", "", s).strip("' ")
            nm = re.match(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", body)
            if nm:
                name = (nm.group(2) or nm.group(1)).split(",")[0].strip()
                # Merkez ilce adi ille ayni olabilir (orn. Adiyaman, Batman) —
                # onceki il kaydi degistiyse yine de eklenmeli.
                if cur and name:
                    cities.setdefault(cur, [])
                    if name not in cities[cur]:
                        cities[cur].append(name)
            continue
        # Il sutunu: baglantili ([[Adana (il)|Adana]]) veya duz metin (|Adana)
        m = re.match(r"^\|(?:\[\[([^\]|]+)(?:\|([^\]]*))?\]\]|([^|]+))$", s)
        if m:
            name = (m.group(2) or m.group(1) or m.group(3) or "").split(",")[0].strip()
            if name and not name.startswith(("rowspan", "style")):
                cur = name
                cities.setdefault(cur, [])
    return cities


def main():
    data = load_wiki()
    print(f"Wikipedia'dan {len(data)} il okundu\n")
    print(f"{'slug':16} {'n':>3}  ilceler")
    for slug, (ad, *_r) in CITY.items():
        got = data.get(ad, [])
        mark = "" if got else "   <-- BOS"
        print(f"{slug:16} {len(got):>3}  {', '.join(got[:6])}{mark}")

    json.dump(data, open(os.path.join(BLOG, "ilce_listeleri.json"), "w",
                         encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nilce_listeleri.json yazildi")


if __name__ == "__main__":
    main()
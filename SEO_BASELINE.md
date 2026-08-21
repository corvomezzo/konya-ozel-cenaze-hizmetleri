# SEO BASELINE — Bellisoy Cenaze Hizmetleri

**Domain:** konyacenazehizmetleri.com  
**İşletme:** Bellisoy Cenaze Hizmetleri  
**Tarih:** 2026-08-21  
**Durum:** Değişiklik öncesi snapshot (Faz 1 tamamlandı)

---

## Özet

| Alan | Durum |
|------|-------|
| Toplam sayfa | 9 (index + 8 iç sayfa) |
| Indexability | ✅ Tüm sayfalar `index,follow` |
| Canonical | ✅ Tüm sayfalar self-referencing HTTPS |
| Sitemap | ✅ Geçerli XML, 9 URL, HTTPS absolute |
| Robots.txt | ✅ Tümüne izin veriyor, sitemap referanslı |
| Schema | ✅ Tüm sayfalarda JSON-LD mevcut |
| Open Graph | ⚠️ Yalnızca index sayfasında |
| Image optimizasyonu | ❌ Çok büyük dosyalar (1.5-1.7MB), w/h eksik |
| Mobile | ✅ Responsive (breakpoint 760px) |
| Internal linking | ✅ Tutarlı navigasyon, ilgili hizmet bağlantıları |
| Broken links | ✅ Yok |
| SSL/HTTPS | ✅ Canonical'lar HTTPS |
| Dil | ✅ `lang="tr"` tüm sayfalarda |

---

## Sayfa Bazında Detay

### `/` (index.html)

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Konya Cenaze Hizmetleri \| 7/24 Cenaze Taşıma ve Defin" — benzersiz, uygun uzunluk |
| Meta description | ✅ | "Konya merkezli 7/24 cenaze taşıma, şehirler arası cenaze nakli, yurt dışı cenaze nakli ve defin organizasyonu. Bellisoy Cenaze Hizmetleri." — benzersiz, özetleyici |
| H1 | ✅ | "Konya Cenaze Taşıma ve Defin Hizmetleri" — anahtar kelimeyi karşılıyor |
| H2/H3 | ✅ | 3x H2 (hizmetler, nasıl ilerler, CTA), 3x H3 (hizmet kartları) |
| Canonical | ✅ | `https://www.konyacenazehizmetleri.com/` |
| Robots meta | ✅ | `index,follow,max-image-preview:large` |
| Schema | ✅ | `@graph` içinde 1 LocalBusiness + 6 Service (tüm hizmet sayfaları) |
| OG tags | ✅ | title, description, url, image, locale, type |
| Görseller | ⚠️ | hero: `yan-3.jpeg` (1.56MB), band: `yan-1.jpeg` (1.68MB) — çok büyük, w/h yok |
| Internal links | ✅ | 8 sayfaya + iletişim/WhatsApp bağlantıları |
| Sayfa boyutu | ✅ | ~9.2KB HTML (makul) |

> **Not:** Schema `@context` → `https://schema.org` ✅ doğru. (Terminal çıktısında *** olarak görünmesi maskeleme artefaktıdır, dosyada sorun yok.)

---

### `/hakkimizda.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Hakkımızda \| Bellisoy Cenaze Hizmetleri Konya" |
| Meta description | ✅ | "Bellisoy Cenaze Hizmetleri; Konya merkezli, Türkiye geneli 7/24 cenaze taşıma, nakil ve defin organizasyonu sunar." |
| H1 | ✅ | "Bellisoy Cenaze Hizmetleri Hakkında" |
| H2 | ✅ | 4x H2 (zor zamanlar, Konya merkezli, hizmet anlayışı, ilgili hizmetler) |
| Canonical | ✅ | `https://www.konyacenazehizmetleri.com/hakkimizda.html` |
| Schema | ✅ | `Service` tipi, Bellisoy referanslı |
| OG tags | ❌ | Eksik |
| Görsel | ✅ | Yok |
| Internal links | ✅ | Cenaze taşıma, şehirler arası, yurt dışı, defin sayfalarına |
| İçerik | ✅ | Özgün, doğal, marka/domain ilişkisi açık |

---

### `/cenaze-tasima.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Konya Cenaze Taşıma Hizmeti \| 7/24 Cenaze Nakil" |
| Meta description | ✅ | "Konya cenaze taşıma ve cenaze nakil hizmeti..." |
| H1 | ✅ | "Konya Cenaze Taşıma Hizmeti" |
| H2 | ✅ | 3x H2 (nasıl organize edilir, neler planlanır, güvenli taşıma) |
| Canonical | ✅ | |
| Schema | ✅ | `Service` tipi |
| OG tags | ❌ | Eksik |
| Görsel | ✅ | Yok |
| Internal links | ✅ | Araçlar, şehirler arası sayfalarına |

---

### `/sehirler-arasi-cenaze-nakli.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Şehirler Arası Cenaze Nakli \| Konya 7/24 Nakil" |
| Meta description | ✅ | "Konya'dan Türkiye geneline şehirler arası cenaze nakli..." |
| H1 | ✅ | "Şehirler Arası Cenaze Nakli" |
| H2 | ✅ | 3x H2 (nasıl yapılır, süreç adımları, neden Bellisoy) |
| Schema | ✅ | `Service` tipi |
| OG tags | ❌ | Eksik |
| İçerik | ⚠️ | "81 il cenaze nakli ağı", "TSE onaylı" iddiaları → doğrulanmamış |

---

### `/yurt-disi-cenaze-nakli.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Yurt Dışı Cenaze Nakli \| Konya Cenaze Hizmetleri" |
| Meta description | ✅ | "Yurt dışından cenaze getirme ve yurt dışı cenaze nakli..." |
| H1 | ✅ | "Yurt Dışı Cenaze Nakli" |
| H2 | ✅ | 3x H2 (işlemler, süreç adımları, Bellisoy farkı) |
| Schema | ✅ | `Service` tipi (serviceType: Uluslararası Cenaze Nakli) |
| OG tags | ❌ | Eksik |
| İçerik | ⚠️ | "7/24 çok dilli iletişim desteği" → doğrulanmamış |

---

### `/cenaze-defin-organizasyonu.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Cenaze Defin Organizasyonu \| Konya 7/24 Hizmet" |
| Meta description | ✅ | "Konya cenaze defin organizasyonu..." |
| H1 | ✅ | "Cenaze Defin Organizasyonu" |
| H2 | ✅ | 3x H2 (destek, adımlar, ek hizmetler) |
| Schema | ✅ | `Service` tipi |
| OG tags | ❌ | Eksik |

---

### `/araclar.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Cenaze Araçlarımız \| Bellisoy Konya Cenaze Nakil" |
| Meta description | ✅ | "Bellisoy cenaze aracı filosu..." |
| H1 | ✅ | "Cenaze Nakil Araçlarımız" |
| H2 | ✅ | 3x H2 (neden önemli, filo özellikleri, hizmet kapsamı) |
| Schema | ✅ | `Service` tipi (serviceType: Cenaze Nakil Aracı Kiralama ve Operasyon) |
| OG tags | ❌ | Eksik |

---

### `/sss.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "Sık Sorulan Sorular \| Konya Cenaze Hizmetleri" |
| Meta description | ✅ | "Konya cenaze taşıma, şehirler arası cenaze nakli..." |
| H1 | ✅ | "Cenaze Hizmetleri Sık Sorulan Sorular" |
| H2 | ✅ | 1x H2 ("Sık sorulan sorular") — yetersiz |
| H3 | ❌ | Yok (FAQ detayları H3 yerine `<details><summary>` ile) |
| Schema | ✅ | `FAQPage` tipi, 8 soru-cevap (`mainEntity`) |
| OG tags | ❌ | Eksik |
| İçerik | ✅ | 8 soru, kapsamlı, hizmet sayfalarıyla tutarlı |

---

### `/iletisim.html`

| Kontrol | Durum | Detay |
|---------|-------|-------|
| Title | ✅ | "İletişim \| Bellisoy Cenaze Hizmetleri Konya" |
| Meta description | ✅ | "Bellisoy Cenaze Hizmetleri iletişim..." |
| H1 | ✅ | "7/24 Cenaze Hizmetleri İletişim" |
| H2 | ✅ | 3x H2 (hemen ulaşın, hizmet bölgesi, ofis bilgileri) |
| Schema | ✅ | `ContactPage` tipi, içinde `LocalBusiness` |
| OG tags | ❌ | Eksik |
| Adres | ⚠️ | "Konya merkezli operasyon ofisimizden" — tam adres yok, yalnızca il düzeyinde |

---

## Altyapı Kontrolleri

### Sitemap (`sitemap.xml`)

| Kontrol | Durum |
|---------|-------|
| XML geçerli | ✅ |
| URL sayısı | ✅ 9 (doğru) |
| URL formatı | ✅ Absolute HTTPS |
| lastmod | ✅ Tümü 2026-08-18 (tutarlı) |
| priority | ⚠️ 1.0, 0.9, 0.8, 0.7 gibi değerler — Google için anlamsız, zararsız |
| Eksik sayfa | ❌ Yok |

### Robots.txt

| Kontrol | Durum |
|---------|-------|
| Allow all | ✅ |
| Sitemap referansı | ✅ `https://www.konyacenazehizmetleri.com/sitemap.xml` |
| CSS/JS engel | ✅ Engellenmemiş |

### HTTPS / Host

| Kontrol | Durum |
|---------|-------|
| www/non-www | ✅ www kullanılıyor (tutarlı) |
| canonical HTTPS | ✅ |
| Trailing slash | ✅ Tutarlı (www'de / ile biten, .html'lerde tutarlı) |

### Structured Data (Schema.org)

| Sayfa | Tip | Geçerli? |
|-------|-----|----------|
| index | `@graph` (1 LocalBusiness + 6 Service) | ✅ |
| hakkimizda | `Service` | ✅ |
| cenaze-tasima | `Service` | ✅ |
| sehirler-arasi | `Service` | ✅ |
| yurt-disi | `Service` | ✅ |
| defin | `Service` | ✅ |
| araclar | `Service` | ✅ |
| sss | `FAQPage` (8Q&A) | ✅ |
| iletisim | `ContactPage` + `LocalBusiness` | ✅ |

> **Not:** Index sayfasındaki `@graph` şeması tüm hizmet sayfalarını listeliyor. Bu hem kapsamlı hem de doğru bir yaklaşım.

---

## Tespit Edilen Sorunlar (Öncelik Sırasına Göre)

### P0 — Hemen düzeltilmeli

| # | Sorun | Sayfalar | Etki |
|---|-------|----------|------|
| P0.1 | **Dev görseller** — yan-1.jpeg 1.68MB, yan-3.jpeg 1.56MB | index (hero + band) | LCP süresini ciddi artırır, mobilde çok yavaş yüklenir |
| P0.2 | **Görsellerde width/height yok** — CLS riski | index.html | Layout shift puanını düşürür |
| P0.3 | **Kullanılmayan görseller** — yan-2.jpeg (1.62MB), rear.jpeg (1.51MB), bellisoy-logo2.jpg (313KB) | images/ | Sadece şişkinlik, silinmeli |

### P1 — Kısa vadede düzeltilmeli

| # | Sorun | Sayfalar | Etki |
|---|-------|----------|------|
| P1.1 | **Open Graph eksik** — title, description, image, url, locale eksik | Tüm iç sayfalar (8 sayfa) | Sosyal medyada paylaşımda zengin önizleme gösterilmez |
| P1.2 | **Logo 313KB** — gereksiz büyük | bellisoy-logo2.jpg | Performans +
- Gereksiz yük |
| P1.3 | **"81 il cenaze nakli ağı", "TSE onaylı" vb. iddialar** — doğrulanmamış | sehirler-arasi, araclar | Doğrulanamayan iddialar güven sorunu yaratabilir |

### P2 — Orta vadede düzeltilmeli

| # | Sorun | Sayfalar | Etki |
|---|-------|----------|------|
| P2.1 | **SSS sayfasında H3 yok** — FAQ detayları `<details>` içinde, heading hiyerarşisi zayıf | sss.html | İçerik yapısı net değil |
| P2.2 | **İletişim sayfasında tam adres yok** | iletisim.html | LocalBusiness schema'da adres eksik |
| P2.3 | **Hizmet sayfalarında görsel yok** — araç gösterimi veya hizmete özgü fotoğraf | cenaze-tasima, defin, araclar | Kullanıcı deneyimini zenginleştirmez |
| P2.4 | **Internal linking artırılabilir** — hizmet sayfaları arasında çapraz bağlantılar mevcut ancak SSS'ye bağlantı eksik | çoğu sayfa | Kullanıcıyı ilgili FAQ'a yönlendirmek faydalı olur |

### P3 — Uzun vadede değerlendirilmeli

| # | Sorun | Sayfalar | Etki |
|---|-------|----------|------|
| P3.1 | **BreadcrumbList schema** eksik (breadcrumb UI mevcut) | Tüm iç sayfalar | Zengin sonuç fırsatı |
| P3.2 | **Araç sayfasında galeri görselleri yok** | araclar.html | Kullanıcı araçları görmek isteyebilir |
| P3.3 | **Hizmet sayfalarında Service schema'ya `areaServed` il bazında detaylandırılabilir** | hizmet sayfaları | Yerel SEO sinyali |

---

## Keyword Map (Mevcut)

| Sayfa | Birincil odak | Title'da | H1'de | Meta'da |
|-------|---------------|----------|-------|---------|
| `/` | Konya cenaze hizmetleri | ✅ | ✅ | ✅ |
| `/cenaze-tasima.html` | Konya cenaze taşıma | ✅ | ✅ | ✅ |
| `/sehirler-arasi-cenaze-nakli.html` | şehirler arası cenaze nakli | ✅ | ✅ | ✅ |
| `/yurt-disi-cenaze-nakli.html` | yurt dışı cenaze nakli | ✅ | ✅ | ✅ |
| `/cenaze-defin-organizasyonu.html` | cenaze defin organizasyonu | ✅ | ✅ | ✅ |
| `/araclar.html` | cenaze nakil araçları | ✅ | ✅ | ✅ |
| `/hakkimizda.html` | Bellisoy Cenaze Hizmetleri | ✅ | ✅ | ✅ |
| `/sss.html` | cenaze hizmetleri hakkında sorular | ✅ | ✅ | ✅ |
| `/iletisim.html` | Bellisoy iletişim | ✅ | ✅ | ✅ |

> **Tespit:** Keyword cannibalization yok. Her sayfanın net bir odağı var. ✅

---

## Marka / Domain Tutarlılığı

| Alan | Durum |
|------|-------|
| İşletme adı schema'da | ✅ "Bellisoy Cenaze Hizmetleri" |
| Header brand | ✅ "BELLİSOY CENAZE HİZMETLERİ - 7/24 TÜM TÜRKİYE" |
| Title'da Bellisoy | ⚠️ Yalnızca hakkimizda, araclar, iletisim sayfalarında |
| H1'de Bellisoy | ⚠️ Yalnızca hakkimizda sayfasında |
| Footer | ✅ "Bellisoy Cenaze Hizmetleri" |
| Domain/name ilişkisi | ✅ Schema'da url ve name birlikte kullanılıyor |

---

## Sonuç

**Website genel durumu: İYİ**

Site temel teknik SEO gerekliliklerinin çoğunu karşılıyor. Schema yapısı kapsamlı, canonical'lar doğru, internal linking tutarlı, içerik benzersiz ve doğal.

**Kritik bulgu yok** (schema bozuk değil, canonical hatalı değil, indexability sorunu yok).

En acil iyileştirme alanı: **görsel optimizasyonu** (dev dosyalar → küçültme + w/h ekleme, kullanılmayan dosyaları temizleme).

---

*Oluşturan: SEO Agent — Bellisoy Cenaze Hizmetleri*  
*Faz 1 — Baseline Audit tamamlandı. Sonraki adım: Faz 2 (P0 düzeltmeleri).*
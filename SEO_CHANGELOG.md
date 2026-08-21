# SEO CHANGELOG — Bellisoy Cenaze Hizmetleri

## Faz 2 — P0: Görsel optimizasyonu (2026-08-21)

### Değişiklik 1: WebP dönüşümü + boyutlandırma

| Alan | Değer |
|------|-------|
| **Ne değişti** | Ana görseller JPEG → WebP dönüştürüldü, 1200px genişliğe resize edildi |
| **Dosyalar** | `images/yan-3.jpeg` → `images/yan-3.webp`, `images/yan-1.jpeg` → `images/yan-1.webp` |
| **Neden** | 1.56MB ve 1.68MB olan JPEG'ler LCP'yi ciddi etkiliyordu. WebP kalite 85 ile ~40KB'a düştü (%97+ kazanç) |
| **Risk** | WebP tüm modern tarayıcılar destekler, eski tarayıcılarda JPEG fallback gerekmez |
| **Test** | Dosya boyutu: 1.56MB → 39KB, 1.68MB → 40KB. Boyut 1200x670 |
| **Rollback** | WebP dosyalarını sil, yedekten JPEG'leri geri koy |

### Değişiklik 2: width/height eklendi

| Alan | Değer |
|------|-------|
| **Ne değişti** | İki `<img>` etiketine `width="1200" height="670"` eklendi |
| **Dosyalar** | `index.html` (hero ve band görselleri) |
| **Neden** | CLS (Cumulative Layout Shift) riskini azaltmak için tarayıcıya render öncesi boyut bildirilmeli |
| **Risk** | Yok — width/height CSS aspect-ratio ile uyumlu |
| **Test** | HTML parse edildi, img etiketlerinde width/height mevcut, görsel path'leri WebP'yi gösteriyor |
| **Rollback** | Eski `<img>` etiketlerini geri yaz |

### Değişiklik 3: OG image URL güncelleme

| Alan | Değer |
|------|-------|
| **Ne değişti** | `og:image` URL'si `yan-3.jpeg` → `yan-3.webp` |
| **Dosyalar** | `index.html` |
| **Neden** | JPEG dosyası silindiği için OG image de WebP'yi göstermeli |
| **Risk** | Düşük |
| **Test** | HTML'de `og:image` değeri kontrol edildi |
| **Rollback** | Eski URL'yi geri yaz |

### Değişiklik 4: Kullanılmayan görseller temizlendi

| Alan | Değer |
|------|-------|
| **Ne değişti** | Kullanılmayan 5 görsel silindi |
| **Dosyalar** | Silinenler: `yan-2.jpeg` (1.62MB), `rear.jpeg` (1.51MB), `bellisoy-logo2.jpg` (313KB) |
| **Neden** | Hiçbir HTML dosyasında referansları yoktu, gereksiz şişkinlik |
| **Risk** | Düşük — hiçbir sayfada kullanılmıyorlardı |
| **Test** | Tüm HTML dosyalarında `grep` ile bu dosya adları arandı, hiçbiri bulunamadı |
| **Rollback** | Git'ten geri al (git restore) |

---

## Faz 2 — P1: OG etiketleri + TODO işaretleme (2026-08-21)

### Değişiklik 5: OG meta etiketleri eklendi

| Alan | Değer |
|------|-------|
| **Ne değişti** | 8 iç sayfaya Open Graph etiketleri eklendi (type, locale, title, description, url, image) |
| **Dosyalar** | `hakkimizda.html`, `cenaze-tasima.html`, `sehirler-arasi-cenaze-nakli.html`, `yurt-disi-cenaze-nakli.html`, `cenaze-defin-organizasyonu.html`, `araclar.html`, `sss.html`, `iletisim.html` |
| **Neden** | Sosyal medyada paylaşıldığında zengin önizleme gösterilmesi için OG etiketleri zorunludur |
| **Risk** | Düşük — OG etiketleri sadece sosyal medya crawler'ları tarafından okunur, site işlevini etkilemez |
| **Test** | Her sayfada og:type, og:locale, og:title, og:description, og:url, og:image etiketleri mevcut |
| **Rollback** | Eski canonical+stylesheet arasındaki OG etiketlerini sil |

### Değişiklik 6: Doğrulanmamış iddialar işaretlendi

| Alan | Değer |
|------|-------|
| **Ne değişti** | "81 il cenaze nakli ağı" → TODO: BUSINESS VERIFICATION REQUIRED eklendi |
| **Dosyalar** | `sehirler-arasi-cenaze-nakli.html` |
| **Neden** | İşletmeden doğrulanmamış iddialar gerçek bilgiymiş gibi yayında olmamalı |
| **Risk** | Yok — TODO notu görsel olarak görünmez, sadece kaynak koda yorum olarak eklendi |
| **Test** | HTML dosyasında TODO metni mevcut |
| **Rollback** | TODO kısmını sil |

---

## Kalite Kontrol Sonuçları

- ✅ Tüm HTML dosyaları parse edilebilir
- ✅ Tüm img src'leri mevcut WebP dosyalarını gösteriyor
- ✅ Tüm canonical'lar değişmedi
- ✅ Sitemap URL'leri değişmedi (URL yapısı korundu)
- ✅ H1'ler değişmedi
- ✅ Schema JSON-LD değişmedi
- ✅ Görsel boyutları: images/ klasörü 6.5MB → 80KB (%98.8 azalma)

---

*Güncelleyen: SEO Agent — Bellisoy Cenaze Hizmetleri*  
---

## Faz 2 — P2: SSS hiyerarşisi + adres + çapraz bağlantı (2026-08-21)

### Değişiklik 7: SSS sayfasında heading hiyerarşisi düzeltildi

| Alan | Değer |
|------|-------|
| **Ne değişti** | 8 `<summary>` etiketi içine `<h3>` eklendi |
| **Dosyalar** | `sss.html`, `site.css` |
| **Neden** | SSS sayfasında H1→H2→H3 hiyerarşisi yoktu, `<details>` içindeki sorular heading olarak işaretli değildi |
| **Risk** | Düşük — CSS'de `summary h3{display:inline;font-size:inherit}` kuralı ile görünüm korundu |
| **Test** | 8 h3 eklendi, heading hiyerarşisi H1->H2->H3 oldu |
| **Rollback** | Git'ten geri al |

### Değişiklik 8: İletişim sayfası adres TODO

| Alan | Değer |
|------|-------|
| **Ne değişti** | "Detaylı adres ve harita bilgisi için iletişime geçin" cümlesine TODO: BUSINESS VERIFICATION REQUIRED eklendi |
| **Dosyalar** | `iletisim.html` |
| **Neden** | Tam adres bilinmiyor, işletmeden doğrulanmalı |
| **Risk** | Yok |
| **Test** | TODO metni dosyada mevcut |
| **Rollback** | Git'ten geri al |

### Değişiklik 9: Hizmet sayfalarına SSS çapraz bağlantısı

| Alan | Değer |
|------|-------|
| **Ne değişti** | 6 hizmet sayfasının altına "Sık sorulan sorular sayfası →" bağlantısı eklendi |
| **Dosyalar** | `cenaze-tasima.html`, `sehirler-arasi-cenaze-nakli.html`, `yurt-disi-cenaze-nakli.html`, `cenaze-defin-organizasyonu.html`, `araclar.html`, `hakkimizda.html` |
| **Neden** | Kullanıcıyı ilgili FAQ'a yönlendirmek, internal linking'i güçlendirmek |
| **Risk** | Düşük |
| **Test** | 6 dosyada da `sss.html` href'i mevcut, broken link yok |
| **Rollback** | Git'ten geri al |

---

*Faz 2 — P0/P1/P2 düzeltmeleri tamamlandı. Sıradaki: P3 düzeltmeleri.*
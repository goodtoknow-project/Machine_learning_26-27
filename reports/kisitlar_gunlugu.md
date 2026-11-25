# Kısıtlar Günlüğü

Projede karşılaşılan her sorunu buraya ekleyin. Künyenin 8. bölümü ("Kısıtlar ve Aşma Yöntemleri") ve sonuç raporu bu kayıtlardan hazırlanacak.

| Tarih | Aşama | Kısıt / sorun | Etkisi | Nasıl aşıldı | Yazan |
| --- | --- | --- | --- | --- | --- |
| 2026-11-26 | Veri sızıntısı | `reservation_status`, `reservation_status_date` iptal sonucunu içeriyor | Model cevabı kopyalar, doğruluk yapay olarak yükselir | Girdilerden çıkarılması öneriliyor, ekip onayı bekleniyor | |
| 2026-11-26 | Veri sızıntısı | `is_canceled` hedef değişken, girdi olarak kullanılırsa model cevabı kopyalar | Doğruluk yapay olarak yükselir | Yalnızca hedef olarak kullanılması öneriliyor | |
| 2026-11-26 | Tahmin anı | Tahmin anı belirsiz (rezervasyon anı mı, giriş öncesi mi) | Hangi sütunların kullanılabileceği değişir | Ekip kararı bekleniyor | |
| 2026-11-26 | Temizlik | Veri setinde 31.994 tekrarlanan satır var (yaklaşık %27). Veri setinde rezervasyon kimliği olmadığı için bunların gerçek tekrar mı yoksa ayrı rezervasyon mu olduğu bilinmiyor | Veri şişer, aynı rezervasyon birden fazla kez sayılabilir | Silme kararı ekip onayı bekliyor | |
| 2026-11-26 | Temizlik | 180 rezervasyonda misafir sayısı (yetişkin + çocuk + bebek) 0 | Mantıksız kayıtlar, modeli bozabilir | Silinmesi öneriliyor, ekip onayı bekleniyor | |
| 2026-11-26 | Temizlik | `adr` (ortalama günlük oda ücreti) bir satırda negatif | Oda ücreti negatif olamaz, muhtemelen iade ya da veri hatası | Satır incelenecek | |
| 2026-11-26 | Temizlik | `adr` bir satırda 5.000'in üzerinde (uç değer) | Tek bir satır ortalamaları ve modeli etkileyebilir | Satır incelenecek | |
| 2026-11-26 | Veri sızıntısı | `booking_changes` veri setinde son hal sayılmış, tahmin anından sonraki değişiklikleri içeriyor olabilir | Model gelecekteki bilgiyi görür | Ekip kararı bekleniyor | |
| | | | | | |

**Aşama örnekleri:** Keşifsel analiz, Temizlik, Kayıp veri, Veri sızıntısı, Öznitelik çıkarımı, Boyut azaltma, Modelleme, Optimizasyon, Değerlendirme, Arayüz

## Alınan kararlar

Ekipçe verilen kararları (ör. hangi sütunun çıkarıldığı, uç değer eşiği) gerekçesiyle buraya yazın.

| Tarih | Karar | Gerekçe |
| --- | --- | --- |
| | | |

# Good to Know
### Makine Öğrenmesi ile Otel Rezervasyonu İptal Tahmini

Otellerde rezervasyonların yaklaşık üçte biri iptal ediliyor. Son dakikada boşalan oda yeniden satılamıyor ve otel gelir kaybediyor. Oteller bu yüzden kapasiteden fazla rezervasyon alıyor (overbooking). Bu sefer de beklenenden az iptal olursa gelen misafire oda verilemiyor.

Bu projede, bir rezervasyonun iptal edilip edilmeyeceğini **rezervasyon yapıldığı anda bilinen bilgilerle** tahmin eden bir makine öğrenmesi modeli geliştiriyoruz. Model her rezervasyon için bir iptal olasılığı hesaplar ve rezervasyonu "iptal edilir" ya da "iptal edilmez" olarak sınıflandırır (`is_canceled` = 1 / 0). Bu, denetimli öğrenmeyle çözülen bir **ikili sınıflandırma** problemidir.

## Model Neye Bakıyor?

Model yalnızca rezervasyon yapıldığı anda bilinen bilgileri kullanır. Bunlardan bazıları:

- Rezervasyonun gelişten kaç gün önce yapıldığı (`lead_time`)
- Depozito türü
- Misafirin geçmiş iptalleri
- Rezervasyon kanalı
- Fiyat ve özel istek sayısı

## Otel Bu Tahminle Ne Yapar?

- **Yüksek riskli rezervasyonlar:** Depozito ister ya da misafiri arayıp teyit alır.
- **Overbooking:** Kaç fazla rezervasyon alacağını tahmin edilen iptal sayısına göre ayarlar.
- **Düşük riskli misafirler:** Esnek iptal koşulları sunar.

## Yaklaşım

1. **Veriyi tanıma:** İptal oranının otel türüne, aya, kanala ve depozito türüne göre nasıl değiştiği incelenir.
2. **Ön işleme:** Hatalı kayıtlar temizlenir, eksik değerler ele alınır ve rezervasyonun sonucunu ele veren sütunlar çıkarılır. Böylece model yalnızca gerçekte kullanılabilecek bilgilerle çalışır.
3. **Öznitelik çıkarımı ve boyut azaltma:** Var olan sütunlardan yeni ve anlamlı öznitelikler üretilir, katkısı düşük olanlar elenir.
4. **Modelleme:** Lojistik regresyon ve karar ağacı gibi basit modellerden Random Forest ve XGBoost / LightGBM gibi güçlü modellere kadar birden fazla yöntem aynı koşullarda karşılaştırılır.
5. **Değerlendirme:** Modeller, hiç görmedikleri test verisinde ölçülür. İptaller azınlıkta olduğu için ana metrik F1 skorudur. İptali en çok etkileyen etkenler de raporlanır.
6. **Kümeleme:** Destekleyici bir analiz olarak misafirler gruplara ayrılır ve her grubun iptal davranışı incelenir.

## Arayüz

Model, Streamlit ile hazırlanan bir web arayüzüyle sunulacak. Kullanıcı tek bir rezervasyonun ya da bir CSV dosyasındaki rezervasyonların iptal olasılığını görebilecek. Arayüzde veri setine ait analiz grafikleri ve modellerin karşılaştırması da yer alacak.

## Veri

Projede **Hotel Booking Demand** veri seti kullanılıyor.

- **Kaynak:** Portekiz'deki bir şehir oteli (City Hotel) ve bir tatil oteli (Resort Hotel)
- **Dönem:** Temmuz 2015 – Ağustos 2017 arası gelişler
- **Boyut:** 119.390 rezervasyon, 32 sütun
- **Dosya:** `data/raw/hotel_bookings.csv` (repoda hazır, ayrıca indirmeye gerek yok)

Veri seti, yazarları tarafından açık erişimli olarak ve **CC BY 4.0** lisansıyla yayımlanmıştır:

> Antonio, N., de Almeida, A., & Nunes, L. (2019). Hotel booking demand datasets. *Data in Brief*, 22, 41–49. https://doi.org/10.1016/j.dib.2018.11.126

Yazarlar iki oteli ayrı dosyalar olarak yayımlamıştır. Repodaki dosya, ikisini tek dosyada birleştiren [Kaggle sürümüdür](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand). Yazarlar, veriyi yayımlamadan önce misafirleri ve otelleri tanımlayan tüm bilgileri silmiştir. Veri seti hiçbir kişisel veri içermez.

`data/raw/` klasöründeki dosya **hiç değiştirilmez**. Temizlik kodla (`src/`) yapılır, temiz veri `data/processed/` klasörüne yazılır.

## Kurulum

**Gerekenler:** Python 3.13 ve Git.

1. Repoyu indirin.
2. Repo klasöründe kütüphaneleri kurun:
   ```
   pip install -r requirements.txt
   ```
3. Kurulumu kontrol edin:
   ```
   python -m src.data
   ```
   Çıktıda satır sayısı (119,390) ve iptal oranı (yaklaşık 0.370) görünüyorsa her şey hazır.

## Kullanılan Teknolojiler

Python, Jupyter Notebook / Google Colab, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, LightGBM, GridSearchCV / RandomizedSearchCV veya Optuna, Streamlit, Git / GitHub

## Kaynaklar

1. Antonio, N., de Almeida, A., & Nunes, L. (2017). Predicting hotel booking cancellations to decrease uncertainty and increase revenue. *Tourism & Management Studies*, 13(2), 25–39. https://doi.org/10.18089/tms.2017.13203
2. Antonio, N., de Almeida, A., & Nunes, L. (2019). Big Data in Hotel Revenue Management: Exploring Cancellation Drivers to Gain Insights Into Booking Cancellation Behavior. *Cornell Hospitality Quarterly*, 60(4), 298–319. https://doi.org/10.1177/1938965519851466
3. Antonio, N., de Almeida, A., & Nunes, L. (2019). Hotel booking demand datasets. *Data in Brief*, 22, 41–49. https://doi.org/10.1016/j.dib.2018.11.126
4. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.
5. Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785–794.
6. Hotel Booking Demand veri seti (Kaggle). Erişim adresi: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
7. Ke, G., et al. (2017). LightGBM: A Highly Efficient Gradient Boosting Decision Tree. *Advances in Neural Information Processing Systems (NeurIPS)*, 30.
8. Streamlit Inc. Streamlit Documentation. Erişim adresi: https://docs.streamlit.io

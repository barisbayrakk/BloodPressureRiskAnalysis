# Tansiyon Risk Analizi

Bu proje, günlük sabah ve akşam tansiyon verilerini analiz ederek **K-Means kümeleme algoritması** ile risk değerlendirmesi yapar.
Sistolik ve diyastolik değerler ayrıştırılır ve yüksek ortalamaya sahip küme **"Risk"** olarak etiketlenir.

---

## 🛠️ Kullanılan Teknolojiler

* Python
* pandas
* numpy
* scikit-learn

---

## 🧠 Nasıl Çalışır?

1. Excel dosyasından tansiyon verileri okunur
2. Veriler sistolik ve diyastolik olarak ayrılır
3. K-Means algoritması uygulanır (2 küme)
4. Ortalama değeri yüksek olan küme riskli olarak belirlenir
5. Her kayıt buna göre etiketlenir

---

## 📌 Örnek

Girdi:

```id="cl4xvq"
120/80
140/90
130/85
```

Çıktı:

```id="w0fd61"
Tarih        Risk
2024-01-01   Normal
2024-01-02   Risk
2024-01-03   Normal
```

---

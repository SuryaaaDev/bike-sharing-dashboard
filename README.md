
# 🚲 Bike Sharing Analysis Project

Proyek ini merupakan bagian dari submission kelas Analisis Data. Kami menggunakan **Bike Sharing Dataset** untuk menjawab dua pertanyaan analisis utama terkait perilaku peminjaman sepeda.

## 📌 Pertanyaan Bisnis
1. Apa saja yang memengaruhi jumlah peminjaman sepeda?
2. Bagaimana perbedaan pola peminjaman antara hari kerja dan akhir pekan?

## 🧪 Proses Analisis
Analisis dilakukan melalui tahapan berikut:
- Gathering Data
- Assessing Data
- Cleaning Data
- Exploratory Data Analysis
- Explanatory Analysis

Insight dari setiap tahapan telah disusun dalam file `notebook.ipynb`.

## 📊 Dashboard Interaktif
Kami membuat dashboard menggunakan Streamlit yang berisi dua visualisasi utama untuk menjawab pertanyaan analisis:
- Jumlah peminjaman berdasarkan musim
- Rata-rata peminjaman di hari kerja vs akhir pekan

## ▶️ Cara Menjalankan Dashboard

1. Pastikan semua dependensi sudah terinstall (lihat bagian `Requirements` di bawah).
2. Jalankan perintah berikut di terminal:
```
streamlit run dashboard.py
```

## 📁 Struktur Folder
```
submission/
├───dashboard/
│   ├───main_data.csv
│   └───dashboard.py
├───data/
│   ├───data_1.csv
│   └───data_2.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## 📦 Requirements

Lihat file `requirements.txt` untuk daftar lengkap library yang dibutuhkan.

---

Data sumber: [Bike Sharing Dataset - UCI](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

# Prediksi Kualitas Air 💧
Sistem prediksi kelayakan air minum berbasis machine learning yang 
memungkinkan pengguna mengetahui apakah air layak dikonsumsi tanpa 
memerlukan pengujian laboratorium.

## Latar Belakang
Mengetahui kelayakan air minum sering kali membutuhkan pengujian 
laboratorium yang mahal dan memakan waktu. Proyek ini hadir sebagai 
solusi praktis berbasis machine learning yang dapat memprediksi 
kelayakan air secara cepat hanya dengan memasukkan parameter kualitas air.

## Fitur Utama
- Input parameter kualitas air secara manual (pH, TDS, Chloramines, dll.)
- Prediksi hasil: **Layak Minum** atau **Tidak Layak Minum**
- Validasi parameter terhadap standar internasional
- Sistem peringatan otomatis jika parameter melebihi batas toleransi
- Rekomendasi mitigasi untuk parameter yang tidak sesuai standar
- Visualisasi grafik probabilitas prediksi secara interaktif

## Dataset
- Sumber: [Kaggle — water_potability.csv](https://www.kaggle.com/datasets/adityakadiwal/water-potability)
- Fitur: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity,
  Organic Carbon, Trihalomethanes, Turbidity
- Target: Potability (0 = Tidak Layak, 1 = Layak Minum)

## Metode
- Algoritma: [K-Nearest Neighbors (KNN)]
- Akurasi model: [0.65%]
- Library: Pandas, NumPy, Scikit-learn, StandardScaler, plotly.express, Matplotlib, Seaborn

## Metodologi
1. **Data Collection** — Dataset publik dari Kaggle
2. **Preprocessing** — Handling missing values, normalisasi dengan 
   StandardScaler, pembagian data latih & uji
3. **Modeling** — Algoritma K-Nearest Neighbors (KNN)
4. **Evaluation** — Metrik akurasi dan F1-score
5. **Deployment** — Antarmuka interaktif berbasis Streamlit

## Struktur File
├── Olahdata.ipynb   
├── water_potability.csv
├── Prediksi.py
├── HasilModel_air.pkl
├── HasilModel_air.sav
├── requirements.txt
└── README.md

## Cara Menjalankan
1. Clone repo ini
```bash
   git clone https://github.com/viienz/Prediksi_Air.git
   cd Prediksi_Air
```
2. Install dependensi
```bash
   pip install -r requirements.txt
```
3. Jalankan aplikasi
```bash
   streamlit run Prediksi.py
```
4. Buka browser dan akses `http://localhost:8501`

## Screenshots
### Tampilan Input & Hasil Prediksi
![App Screenshot](screenshot_app.png)

## Hasil Evaluasi
Model KNN dievaluasi menggunakan metrik akurasi dan F1-score dengan 
pembagian data latih dan data uji. Model dilengkapi validasi terhadap 
standar internasional untuk setiap parameter air.

## Pengembang
**Devin Pandya Subarkah** — Informatika, Universitas Islam Indonesia  
Mata Kuliah: Fundamen Sains Data | Dosen: Dr. Syarif Hidayat, S.Kom., M.I.T.

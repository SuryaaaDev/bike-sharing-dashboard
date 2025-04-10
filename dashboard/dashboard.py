
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("🚲 Bike Sharing Dashboard")
st.markdown("Visualisasi interaktif untuk menjawab pertanyaan analisis seputar peminjaman sepeda.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("dashboard/main_data.csv")

data = load_data()

# Preprocessing sederhana
data['dteday'] = pd.to_datetime(data['dteday'])
data['season'] = data['season'].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
data['weekday'] = data['weekday'].map({
    0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
    4: "Thursday", 5: "Friday", 6: "Saturday"
})
data['workingday'] = data['workingday'].map({0: "Weekend/Holiday", 1: "Working Day"})

# Visualisasi 1: Pengaruh Musim terhadap Jumlah Peminjaman
st.subheader("📅 Jumlah Peminjaman Berdasarkan Musim")
fig1, ax1 = plt.subplots()
sns.boxplot(data=data, x='season', y='cnt', palette='Set2', ax=ax1)
ax1.set_xlabel("Musim")
ax1.set_ylabel("Jumlah Peminjaman")
ax1.set_title("Distribusi Jumlah Peminjaman per Musim")
st.pyplot(fig1)

# Visualisasi 2: Perbedaan Hari Kerja vs Akhir Pekan
st.subheader("🗓️ Perbandingan Jumlah Peminjaman Hari Kerja vs Akhir Pekan")
avg_cnt = data.groupby('workingday')['cnt'].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(data=avg_cnt, x='workingday', y='cnt', palette='pastel', ax=ax2)
ax2.set_xlabel("Tipe Hari")
ax2.set_ylabel("Rata-rata Jumlah Peminjaman")
ax2.set_title("Rata-rata Jumlah Peminjaman: Hari Kerja vs Akhir Pekan")
st.pyplot(fig2)

st.markdown("---")
st.markdown("📌 Data berasal dari [Bike Sharing Dataset]")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Interaktif Bike Sharing", layout="centered")

st.title("🚲 Dashboard Interaktif Peminjaman Sepeda")
st.markdown("Gunakan filter di bawah untuk mengeksplorasi jumlah peminjaman sepeda berdasarkan musim dan cuaca.")

@st.cache_data
def load_data():
    data = pd.read_csv("dashboard/main_data.csv")
    data['season'] = data['season'].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
    data['weathersit'] = data['weathersit'].map({
        1: "Clear/Few clouds",
        2: "Mist + Cloudy",
        3: "Light Snow/Light Rain",
        4: "Heavy Rain/Snow"
    })
    return data

data = load_data()

# Filter interaktif
selected_season = st.selectbox("Pilih Musim", options=data['season'].unique())
selected_weather = st.multiselect("Pilih Kondisi Cuaca", options=data['weathersit'].unique(), default=data['weathersit'].unique())

filtered_data = data[(data['season'] == selected_season) & (data['weathersit'].isin(selected_weather))]

# Visualisasi
fig, ax = plt.subplots()
sns.lineplot(data=filtered_data, x='dteday', y='cnt', marker='o', ax=ax)
ax.set_title(f"Jumlah Peminjaman Sepeda pada Musim {selected_season} dan Cuaca Tertentu")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("📌 Data difilter berdasarkan pilihan musim dan kondisi cuaca.")
st.markdown("Sumber data: [Bike Sharing Dataset - UCI](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset)")

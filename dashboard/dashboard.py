
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard Interaktif Bike Sharing", layout="wide")
st.title("🚲 Dashboard Interaktif Peminjaman Sepeda")
st.markdown("Eksplorasi data peminjaman sepeda berdasarkan musim, cuaca, hari kerja, dan waktu.")

@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['weathersit'] = df['weathersit'].map({
        1: 'Clear/Few clouds',
        2: 'Mist + Cloudy',
        3: 'Light Snow/Light Rain',
        4: 'Heavy Rain/Snow'
    })
    df['workingday'] = df['workingday'].map({0: 'Weekend', 1: 'Working Day'})
    return df

df = load_data()

# Sidebar untuk interaktif
st.sidebar.header("🔧 Filter Data")
min_date, max_date = df['dteday'].min(), df['dteday'].max()
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date], min_value=min_date, max_value=max_date)

selected_season = st.sidebar.multiselect("Pilih Musim", options=df['season'].unique(), default=df['season'].unique())
selected_weather = st.sidebar.multiselect("Pilih Cuaca", options=df['weathersit'].unique(), default=df['weathersit'].unique())

# Filter data
filtered_df = df[
    (df['dteday'] >= pd.to_datetime(date_range[0])) &
    (df['dteday'] <= pd.to_datetime(date_range[1])) &
    (df['season'].isin(selected_season)) &
    (df['weathersit'].isin(selected_weather))
]

# Visualisasi 1: Peminjaman berdasarkan musim
st.subheader("📊 Jumlah Peminjaman Berdasarkan Musim")
fig1, ax1 = plt.subplots()
sns.boxplot(data=filtered_df, x="season", y="cnt", ax=ax1)
ax1.set_title("Distribusi Peminjaman Sepeda per Musim")
st.pyplot(fig1)

# Visualisasi 2: Perbedaan Hari Kerja dan Akhir Pekan
st.subheader("📅 Perbedaan Peminjaman: Hari Kerja vs Akhir Pekan")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered_df, x="workingday", y="cnt", estimator=sum, ci=None, ax=ax2)
ax2.set_title("Total Peminjaman pada Hari Kerja dan Akhir Pekan")
st.pyplot(fig2)

st.markdown("---")
st.markdown("📌 Data difilter berdasarkan musim, cuaca, dan tanggal yang dipilih.")
st.markdown("Sumber data: [Bike Sharing Dataset - UCI](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset)")

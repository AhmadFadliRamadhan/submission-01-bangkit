import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style="dark")

df_qualityair = pd.read_csv("df_qualityair.csv")
df_qualityair["date"] = pd.to_datetime(df_qualityair["date"])

df_variable = pd.read_csv("df_variable.csv")
df_variable["date"] = pd.to_datetime(df_variable["date"])

# Filter data
min_date = df_qualityair["date"].min()
max_date = df_qualityair["date"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image(
        "https://raw.githubusercontent.com/AhmadFadliRamadhan/submission-01-bangkit/main/dashboard/logo.png",
        width=200,
    )

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label="Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
    )

df_a = df_qualityair[
    (df_qualityair["date"] >= str(start_date))
    & (df_qualityair["date"] <= str(end_date))
]

df_b = df_variable[
    (df_variable["date"] >= str(start_date)) & (df_variable["date"] <= str(end_date))
]


st.title("Submission 1 | Ahmad Fadli Ramadhan")

st.header("Belajar Analisis Data dengan Python")

st.write("### Scatter Plot Matrix Parameter Kualitas Udara di Stasiun Dingling")

# Membuat scatter matrix
scatter_data = df_a[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]]
scatter_matrix = pd.plotting.scatter_matrix(
    scatter_data, figsize=(12, 12), diagonal="kde"
)

# Memodifikasi plot
for i in range(len(scatter_data.columns)):
    for j in range(len(scatter_data.columns)):
        ax = scatter_matrix[i, j]
        ax.xaxis.label.set_rotation(45)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha("right")
        ax.xaxis.label.set_size(10)
        ax.yaxis.label.set_size(10)

# Menambah judul
scatter_matrix[0, 0].get_figure().suptitle(
    "Scatter Plot Matrix Parameter Kualitas Udara di Stasiun Pemantauan Dingling"
)

# Menampilkan plot di Streamlit
st.pyplot(scatter_matrix[0, 0].get_figure())

st.write(
    "### Grafik Rata-Rata Nilai Tiap Kolom per Hari di Stasiun Pemantauan Dingling"
)

daily_mean = df_b.groupby(df_b["date"].dt.date).mean()
fig, ax = plt.subplots(figsize=(18, 6))
for column in daily_mean.columns:
    if column != "date":
        ax.plot(daily_mean.index, daily_mean[column], label=column)

ax.set_title(
    "Grafik Rata-Rata Nilai Tiap Kolom per Hari di Stasiun Pemantauan Dingling"
)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Nilai Rata-Rata")
ax.legend()
st.pyplot(fig)

st.caption("Oleh Ahmad Fadli Ramadhan")

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


@st.cache_data
def load_csv(url):
    df = pd.read_csv(url)
    df["date"] = pd.to_datetime(df["date"])
    return df


@st.cache_data
def filter(df, start, end):
    return df[(df["date"] >= str(start)) & (df["date"] <= str(end))]


@st.cache_data
def min_max(df):
    return df["date"].min(), df["date"].max()


@st.cache_data
def groupbydate(df):
    return df.groupby(df["date"].dt.date).mean()


@st.cache_data
def scatterplot(df):
    # Membuat scatter matrix
    scatter_data = df[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]]
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


def linechart(df):
    fig, ax = plt.subplots(figsize=(18, 6))
    for column in df.columns:
        if column != "date":
            ax.plot(df.index, df[column], label=column)

    ax.set_title(
        "Grafik Rata-Rata Nilai Tiap Kolom per Hari di Stasiun Pemantauan Dingling"
    )
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Nilai Rata-Rata")
    ax.legend()
    st.pyplot(fig)


def main():
    df_qualityair = load_csv(
        "https://raw.githubusercontent.com/AhmadFadliRamadhan/submission-01-bangkit/main/dashboard/df_qualityair.csv"
    )
    df_variable = load_csv(
        "https://raw.githubusercontent.com/AhmadFadliRamadhan/submission-01-bangkit/main/dashboard/df_variable.csv"
    )

    # Filter data
    min_date, max_date = min_max(df_qualityair)

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

    df_a = filter(df_qualityair, start_date, end_date)
    df_b = filter(df_variable, start_date, end_date)

    st.title("Submission 1 | Ahmad Fadli Ramadhan")

    st.header("Air Quality Dataset")

    st.write("##### Scatter Plot Matrix Parameter Kualitas Udara di Stasiun Dingling")

    scatterplot(df_qualityair)

    st.write(
        """
            Berdasarkan visualisasi scatter matriks di atas, diketahui bahwa:

            - `PM2.5` dan `PM10` terlihat dengan jelas membentuk sebuah garis mengarah ke kanan atas, menunjukkan korelasi positif yang kuat.
            - `CO` dan `NO2` membentuk persebaran mengarah ke kanan atas, persebarannya agak tersebar, menunjukkan korelasi positif yang sedang.
            - `CO` - `PM2.5`, `NO2` - `PM2.5`, `CO` - `PM10`, dan `NO2` - `PM10` membentuk persebaran mengarah ke kanan atas walau tidak terlalu condong, memiliki persebaran yang luas, menunjukkan korelasi positif yang lemah.
            - Sisa pasangan yang tidak disebutkan memiliki persebaran yang acak.
            """
    )

    st.write(
        "##### Grafik Rata-Rata Nilai Tiap Kolom per Hari di Stasiun Pemantauan Dingling"
    )

    st.write(
        """
            Berdasarkan visualisasi di atas, diketahui bahwa:

            - `TEMP`, `PRES`, dan `DEWP` memiliki pola musiman, di mana `TEMP` dan `DEWP` memiliki pola garis yang cenderung mirip.
            - `PRES` terhadap `TEMP` dan `DEWP` memiliki pola garis yang berlawanan.
            - `RAIN` memiliki pola garis lurus yang cenderung konstan pada nilai nol.
            """
    )

    daily_mean = groupbydate(df_variable)
    linechart(daily_mean)

    st.caption("Oleh Ahmad Fadli Ramadhan")


if __name__ == "__main__":
    main()

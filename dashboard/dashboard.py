import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

st.title("Submission 1 | Ahmad Fadli Ramadhan")

st.header("Belajar Analisis Data dengan Python")

st.write(
    """
    # Scatter Plot Matrix Parameter Kualitas Udara di Stasiun Dingling
    """
)

st.image(
    "https://example.com/image.jpg", caption="Deskripsi gambar", use_column_width=True
)

# Menyisipkan gambar dari file lokal
st.image("nama_file.jpg", caption="Deskripsi gambar", use_column_width=True)

st.write(
    """
    # Scatter Plot: Pengaruh Curah Hujan terhadap NO2 di Stasiun Dingling
    """
)

st.image(
    "https://example.com/image.jpg", caption="Deskripsi gambar", use_column_width=True
)

# Menyisipkan gambar dari file lokal
st.image("nama_file.jpg", caption="Deskripsi gambar", use_column_width=True)

st.caption("Oleh Ahmad Fadli Ramadhan")

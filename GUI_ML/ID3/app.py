import streamlit as st
import predict_page as pred

st.set_page_config(page_title="Diabetes Prediction")

st.header("Aplikasi Deteksi Diabetes", divider='rainbow')


st.info("Aplikasi Ini Menggunakan bebrapa parameter untuk mengecek kemungkinan diabetes seperti:  tingkat Hb1Ac, kandungan gula darah, usia, jenis kelamin, riwayat hipertensi, riwayat merokok, dan skala BMI")
st.write("*Masukkan beberapa data yang terkait*")

genders =[
    "Perempuan",
    "Laki Laki",
    "Lainnya",
]
smoking_H =[
    "no Info",
    "current",
    "ever",
    "former",
    "never",
    "not current",
]
option =[
    "Ya",
    "Tidak",
]

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Jenis Kelamin", genders)
    bg = st.number_input("Tingkat Gula Darah")
    Hb1Ac = st.number_input("Tingkat Hb1Ac")
    ht = st.selectbox("Hipertensi", option)

with col2:
    age = st.number_input("Umur")
    hd = st.selectbox("Penyakit Jantung", option)
    bmi = st.number_input("BMI")
    sh = st.selectbox("Riwayat Merokok", smoking_H)
        

predict = st.button("Prediksi", type='primary')
if predict:
    hasil = pred.prediksi(gender,age,ht,hd,sh,bmi,Hb1Ac,bg)
    st.info(f"Hasil Prediksi adalah {hasil[0]}")

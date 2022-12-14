import streamlit as st
from custom_module.custom import *


def luas_lingkaran():
    st.header("BANGUN DATAR LINGKARAN")

    st.subheader("Mencari Luas")

    luas_lingkaran = st.number_input("Masukkan Jari-Jari :")

    btn_luas = btnhasil(1)

    if btn_luas:
        result_luas = 3.14 * luas_lingkaran * luas_lingkaran

        rumusbangundatar("Luas", "Lingkaran", "π x r x r")

        resultbangundatar("Luas", "Lingkaran", result_luas)


def keliling_lingkaran():
    st.subheader("Mencari Keliling")

    keliling_lingkaran = st.number_input("Masukkan Jari-Jari : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_keliling = 2 * 3.14 * keliling_lingkaran

        rumusbangundatar("Keliling", "Lingkaran", "2 x π x r")

        resultbangundatar("Keliling", "Lingkaran", result_keliling)


def lingkaran():
    import streamlit as st
    luas_lingkaran()
    keliling_lingkaran()
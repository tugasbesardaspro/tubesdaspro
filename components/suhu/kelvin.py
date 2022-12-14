import streamlit as st
from custom_module.custom import *


def ctokelvin():
    st.header("KONVERSI SUHU KELVIN")

    st.subheader("Celcius Ke Kelvin")

    c = st.number_input("Masukkan Suhu (C) :")

    btn_luas = btnhasil(1)

    if btn_luas:
        result_luas = c + 273

        rumussuhu("Suhu", "Ke Kelvin", "C + 273")

        resultsuhu(f"Suhu", "Ke Kelvin", result_luas)


def kelvintoc():
    st.subheader("Kelvin ke Celcius")

    k = st.number_input("Masukkan Suhu (K) : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_keliling =  k - 273

        rumussuhu("Suhu", "Ke Celcius", "K - 273")

        resultsuhu("Suhu", "Ke Celcius", result_keliling)


def kelvin():
    import streamlit as st
    ctokelvin()
    kelvintoc()
import streamlit as st
from custom_module.custom import *


def fahrenheittoc():
    st.header("KONVERSI SUHU FAHRENHEIT")

    st.subheader("Celcius Ke Fahrenheit")

    c = st.number_input("Masukkan Suhu (C) :")

    btn_luas = btnhasil(1)

    if btn_luas:
        result_luas = (9/5) * c + 32

        rumussuhu("Suhu", "Ke Fahrenheit", "9/5 x C + 32")

        resultsuhu(f"Suhu", "Ke Fahrenheit", result_luas)


def ctofahrenheit():
    st.subheader("Fahrenheit ke Celcius")

    f = st.number_input("Masukkan Suhu (F) : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_keliling =  5/9 * (f-32)

        rumussuhu("Suhu", "Ke Celcius", "5/9 * (F - 32)")

        resultsuhu("Suhu", "Ke Celcius", result_keliling)


def fahrenheit():
    import streamlit as st
    fahrenheittoc()
    ctofahrenheit()
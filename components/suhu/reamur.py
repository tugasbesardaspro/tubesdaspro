import streamlit as st
from custom_module.custom import *


def ctoreamur():
    st.header("KONVERSI SUHU REAMUR")

    st.subheader("Celcius Ke Reamur")

    c = st.number_input("Masukkan Suhu (C) :")

    btn_luas = btnhasil(1)

    if btn_luas:
        result_luas = 4/5 * c

        rumussuhu("Suhu", "Ke Reamur", "4/5 x C")

        resultsuhu(f"Suhu", "Ke Reamur", result_luas)


def reamurtoc():
    st.subheader("Reamur ke Celcius")

    r = st.number_input("Masukkan Suhu (R) : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_keliling =  5/4 * r

        rumussuhu("Suhu", "Ke Celcius", "5/4 x R")

        resultsuhu("Suhu", "Ke Celcius", result_keliling)


def reamur():
    import streamlit as st
    ctoreamur()
    reamurtoc()
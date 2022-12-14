import streamlit as st
# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components
from custom_module.custom import *

def waktu():
    st.header("WAKTU")
    st.subheader("Mencari Waktu")

    jarak = st.number_input("Masukkan Jarak : ")
    kecepatan = st.number_input("Masukkan Kecepatan : ")

    btn_keliling = btnhasil(3)

    if btn_keliling:

        result_waktu = jarak/kecepatan

        rumuskecepatan("Rumus", "Waktu", "Jarak / Kecepatan")

        resulkecepatan("Waktu", "Benda", result_waktu)

def wak():
    import streamlit as st
    waktu()
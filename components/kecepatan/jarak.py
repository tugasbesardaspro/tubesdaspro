import streamlit as st
# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components
from custom_module.custom import *

def jarak():
    st.header("JARAK")
    st.subheader("Mencari Jarak")

    waktu = st.number_input("Masukkan Waktu (s) : ")
    kecepatan = st.number_input("Masukkan Kecepatan : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_jarak = waktu*kecepatan 

        rumuskecepatan("Rumus", "Jarak", "Waktu x Kecepatan")

        resulkecepatan("Jarak", "Benda", result_jarak)

def jar():
    import streamlit as st
    jarak()

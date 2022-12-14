import streamlit as st
# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components
from custom_module.custom import *

def kecepatan():
    st.header("KECEPATAN")

    st.subheader("Mencari Kecepatan")

    jarak = st.number_input("Masukkan Jarak (m) :")
    waktu = st.number_input("Masukkan Waktu (s) :")
    btn_luas = btnhasil(1)

    if btn_luas:
        result_kecepatan = jarak / waktu

        rumuskecepatan("Rumus", "Kecepatan", "Jarak / Waktu")

        resulkecepatan("Kecepatan", "Benda", result_kecepatan)


def kec():
    import streamlit as st
    kecepatan()

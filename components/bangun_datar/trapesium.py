import streamlit as st
import codecs
import streamlit.components.v1 as components
from custom_module.custom import *


def luas_trapesium():
    st.header("BANGUN DATAR TRAPESIUM")

    st.subheader("Mencari Luas")

    alas_jajargenjang = st.number_input("Masukkan Alas")
    tinggi_jajargenjang = st.number_input("Masukkan Tinngi")

    result_luas = alas_jajargenjang * tinggi_jajargenjang

    
    f=codecs.open("./components/htmlFiles/luas-jajargenjang.html", 'r')
    page7 = f.read().format(alas = alas_jajargenjang, tinggi = tinggi_jajargenjang)
    components.html(page7,width=340,height=200,scrolling=False)
    if st.button("Luas Jajargenjang"):

        rumusbangundatar("Luas", "jajargenjang", "a x t")

        resultbangundatar("Luas", "jajargenjang", result_luas)


def keliling_trapesium():
    st.subheader("Mencari keliling")

    a = st.number_input("Masukkan a")
    b = st.number_input("Masukkan b")
    result_keliling = 2 * (a + b)

    f=codecs.open("./components/htmlFiles/keliling-jajargenjang.html", 'r')
    page7 = f.read().format(a = a, b = b)
    components.html(page7,width=340,height=200,scrolling=False)

    if st.button("Keliling Jajargenjang"):
        rumusbangundatar("Keliling", "Jajargenjang", "2 x ( a + b )")

        resultbangundatar("Keliling","jajargenjang", result_keliling)

def jajargenjang():
    luas_trapesium()
    keliling_trapesium()

import streamlit as st
import turtle
# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components
from custom_module.custom import *


def luas_persegi():
    st.header("BANGUN DATAR PERSEGI")

    st.subheader("Mencari Luas")

    luas_persegi = st.number_input("Masukkan Sisi :")

    btn_luas = btnhasil(1)

    if btn_luas:
        result_luas = luas_persegi * luas_persegi

        rumusbangundatar("Luas", "Persegi", "S x S")

        resultbangundatar("Luas", "Persegi", result_luas)

     

        # Custom Components Fxn
        f=codecs.open("./components/htmlFiles/luas-persegi.html", 'r')
        page = f.read().format(luas = luas_persegi+100)
        components.html(page,width=300,height=300,scrolling=False)
        


def keliling_persegi():
    st.subheader("Mencari Keliling")

    keliling_persegi = st.number_input("Masukkan Sisi : ")

    btn_keliling = btnhasil(2)

    if btn_keliling:

        result_keliling = 4*keliling_persegi 

        rumusbangundatar("Keliling", "Persegi", "S x 4")

        resultbangundatar("Keliling", "Persegi", result_keliling)

         # Custom Components Fxn
        f=codecs.open("./components/htmlFiles/keliling-persegi.html", 'r')
        page = f.read().format(keliling = keliling_persegi)
        components.html(page,width=300,height=300,scrolling=False)


def persegi():
    import streamlit as st
    luas_persegi()
    keliling_persegi()
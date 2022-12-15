import streamlit as st
from custom_module.custom import *
import codecs
import streamlit.components.v1 as components


def luas_lingkaran():
    st.header("BANGUN DATAR LINGKARAN")

    st.subheader("Mencari Luas")

    luas_lingkaran = st.number_input("Masukkan Jari-Jari :")

    result_luas = 3.14 * luas_lingkaran * luas_lingkaran

    f=codecs.open("./components/htmlFiles/luas-lingkaran.html", 'r')
    page5 = f.read().format(r = luas_lingkaran)
    components.html(page5,width=300,height=270,scrolling=False)

    if st.button("Luas Lingkaran"):

        rumusbangundatar("Luas", "Lingkaran", "π x r x r")

        resultbangundatar("Luas", "Lingkaran", result_luas)

        penjelasan("Luas lingkaran adalah ruang yang ditempati oleh lingkaran pada bidang dua dimensi. Atau, ruang yang ditempati dalam batas/keliling lingkaran yang disebut sebagai luas lingkaran. Untuk menghitung luas sebuah lingkaran adalah dengan mengalikan nilai π (atau pi) dengan jari-jari lingkaran (r).")


def keliling_lingkaran():
    st.subheader("Mencari Keliling")

    keliling_lingkaran = st.number_input("Masukkan Jari-Jari : ")

    result_keliling = 2 * 3.14 * (keliling_lingkaran + keliling_lingkaran)

    f=codecs.open("./components/htmlFiles/keliling-lingkaran.html", 'r')
    page6 = f.read().format(r = keliling_lingkaran*2)
    components.html(page6,width=300,height=270,scrolling=False)

    if st.button("Keliling Lingkaran"):

        rumusbangundatar("Keliling", "Lingkaran", "2 x π x d")

        resultbangundatar("Keliling", "Lingkaran", result_keliling)

        penjelasan("Keliling lingkaran merupakan busur terpanjang pada suatu lingkaran. Dalam menghitung keliling lingkaran tidaklah sulit. Sobat Pintar dapat menggunakan dua cara untuk menghitung keliling lingkaran, yaitu jika diketahui jari-jari (r) atau jika diketahui diameter (d).")


def lingkaran():
    import streamlit as st
    luas_lingkaran()
    keliling_lingkaran()
import streamlit as st
import codecs
import streamlit.components.v1 as components
from custom_module.custom import *

def luas_persegi():
    st.header("BANGUN DATAR PERSEGI")

    st.subheader("Mencari Luas")

    luas_persegi = st.number_input("Masukkan Sisi :")

    result_luas = luas_persegi * luas_persegi

    f=codecs.open("./components/htmlFiles/luas-persegi.html", 'r')
    page = f.read().format(luas = luas_persegi)
    components.html(page,width=300,height=250,scrolling=False)

    if st.button("Hasil") or luas_persegi:
        

        rumusbangundatar("Luas", "Persegi", "S x S")


        resultbangundatar("Luas", "Persegi", result_luas)

        penjelasan("Persegi merupakan bangun datar yang memiliki empat sisi dengan panjang yang seluruhnya sama. Untuk menghitung luas persegi, maka rumus yang digunakan adalah L = s x s. Dengan keterangan L adalah luas, sedangkan s adalah sisi.")

def keliling_persegi():
    st.subheader("Mencari Keliling")

    keliling_persegi = st.number_input("Masukkan Sisi : ")

    result_keliling = 4*keliling_persegi

    # Custom Components Fxn
    f=codecs.open("./components/htmlFiles/keliling-persegi.html", 'r')
    page2 = f.read().format(keliling = result_keliling)
    components.html(page2,width=300,height=250,scrolling=False)

    if st.button("Keliling Persegi") or keliling_persegi:

        rumusbangundatar("Keliling", "Persegi", "4 x s")

        resultbangundatar("Keliling", "Persegi", result_keliling)

        penjelasan("Keliling adalah total penjumlahan dari semua sisi luar bangun datar bentuk apa pun, termasuk tidak beraturan dan bangun gabungan. Bicara soal rumus keliling persegi, berikut hal yang perlu kalian ketahui: Rumus keliling persegi empat sisi: K = 4 x s.")


def persegi():    
    luas_persegi()
    keliling_persegi()
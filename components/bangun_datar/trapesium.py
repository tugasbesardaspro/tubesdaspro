import streamlit as st
import codecs
import streamlit.components.v1 as components
from custom_module.custom import *


def luas_trapesium():
    st.header("BANGUN DATAR TRAPESIUM SAMA KAKI")

    st.subheader("Mencari Luas Trapesium Sama Kaki")

    sisi1_trapesium = st.number_input("Masukkan Sisi 1 : ")
    sisi2_trapesium = st.number_input("Masukkan Sisi 2 : ")
    tinggi_trapesium = st.number_input("Masukkan Tinggi trapesium : ")

    result_luas = (sisi1_trapesium + sisi2_trapesium) * tinggi_trapesium/2
    
    f=codecs.open("./components/htmlFiles/luas-trapesium.html", 'r')
    page9 = f.read().format(sisi1 = sisi1_trapesium, sisi2 = sisi2_trapesium, tinggi = tinggi_trapesium)
    components.html(page9,width=420,height=250,scrolling=False)
    if st.button("Luas Trapesium"):

        rumusbangundatar("Luas", "Trapesium", "(sisi1 + sisi2) X tinggi / 2")

        resultbangundatar("Luas", "Trapesium", result_luas)
        
        penjelasan("Luas dari Trapesium yaitu yang mana terdiri dari dua sisi yang ditambahkan, kemudian dikali kan oleh tinggi dan 1/2")


def keliling_trapesium():
    st.subheader("Mencari keliling Trapesium Sama Kaki")

    sisi1 = st.number_input("Masukkan Sisi 1 :")
    sisi2 = st.number_input("Masukkan Sisi 2 :")
    sisi3 = st.number_input("Masukkan Sisi 3 :")
    sisi4 = st.number_input("Masukkan Sisi 4 :")
    
    result_keliling = sisi1 + sisi2 + sisi3 + sisi4

    f=codecs.open("./components/htmlFiles/keliling-trapesium.html", 'r')
    page10 = f.read().format(sisi1 = sisi1, sisi2 = sisi2, sisi3 = sisi3, sisi4 = sisi4)
    components.html(page10,width=420,height=250,scrolling=False)

    if st.button("Keliling Trapesium"):
        rumusbangundatar("Keliling", "Trapesium", "sisi1 + sisi2 + sisi3 + sisi4")

        resultbangundatar("Keliling","Trapesium", result_keliling)
        
        penjelasan("Keliling dari Trapesium yaitu berada pada keempat sisi tersebut yang terdiri sisi AB dan sisi CD terletak dibagian alas yang mana posisinya itu sejajar. Sedangkan sisi AD dan sisi BC pada bagian kaki yang mana kedua sisi tersebut tidak sejajar.")

def trapesium():
    luas_trapesium()
    keliling_trapesium()

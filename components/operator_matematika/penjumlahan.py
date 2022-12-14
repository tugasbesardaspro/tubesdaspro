import streamlit as st
from custom_module.custom import *


def pjmlh_bil():
    st.header("PERHITUNGAN PENJUMLAHAN MATEMATIKA")

    st.subheader("Penjumlahan Pada Dua Bilangan")
    
    pjm1 = st.number_input("Masukkan bilangan x : ")
    pjm2 = st.number_input("Masukkan bilangan y : ")

    btn_pjm = btnhasil(1)

    if btn_pjm:
        total_pjm = pjm1 + pjm2

        rumusoperator("Penjumlahan", "Pada Bilangan", "x + y")

        resultoperator("Hasil", "Dari Penjumlahan", total_pjm)

# def pjmlh_pecahan():
#     st.subheader("Penjumlahan Pada Pecahan")
    
#     pembilang1 = st.number_input("Masukkan Pembilang 1 : ")
#     penyebut1 = st.number_input("Masukkan Penyebut 1 : ")
    
#     pembilang2 = st.number_input("Masukkan Pembilang 2 : ")
#     penyebut2 = st.number_input("Masukkan Penyebut 2 :")
    
#     btn_pecahan = btnhasil(2)
    
#     if btn_pecahan:
        
        
def penjumlahan():
    import streamlit as st
    pjmlh_bil()

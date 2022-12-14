import streamlit as st
from custom_module.custom import *

def pmbg_bil():
    st.header("PERHITUNGAN PEMBAGIAN MATEMATIKA")
    
    pmbg1 = st.number_input("Masukkan bilangan x : ")
    pmbg2 = st.number_input("Masukkan bilangan y : ")
    
    btn_pmbg = btnhasil(1)
    
    if btn_pmbg:
        total_pmbg = pmbg1 / pmbg2
        
        rumusoperator("Pembagian", "Pada Bilangan", "x / y")
        resultoperator(f"Hasil", "Dari Pembagian", total_pmbg)
        
def pembagian():
    import streamlit as st
    pmbg_bil()
import streamlit as st
from custom_module.custom import *

def prkl_bil():
    st.header("PERHITUNGAN PERKALIAN MATEMATIKA")
    
    prkl1 = st.number_input("Masukkan bilangan x : ")
    prkl2 = st.number_input("Masukkan bilangan y : ")
    
    btn_prkl = btnhasil(1)
    
    if btn_prkl:
        total_prkl = prkl1 * prkl2
        
        rumusoperator("Perkalian", "Pada Bilangan", "x * y")
        resultoperator(f"Hasil", "Dari Perkalian", total_prkl)
        
def perkalian():
    import streamlit as st
    prkl_bil()
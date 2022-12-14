import streamlit as st
from custom_module.custom import *

def pgrn_bil():
    st.header("PERHITUNGAN PENGURANGAN MATEMATIKA")
    
    pgrn1 = st.number_input("Masukkan bilangan x : ")
    pgrn2 = st.number_input("Masukkan bilangan y : ")
    
    btn_pgrn = btnhasil(1)
    
    if btn_pgrn:
        total_pgrn = pgrn1 - pgrn2
        
        rumusoperator("Pengurangan", "Pada Bilangan", "x - y")
        
        resultoperator("Hasil", "Dari Pengurangan", total_pgrn)
        
def pengurangan():
    import streamlit as st
    pgrn_bil()
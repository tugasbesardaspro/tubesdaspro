import streamlit as st
from components.operator_matematika.penjumlahan import penjumlahan
from components.operator_matematika.pengurangan import pengurangan
from components.operator_matematika.perkalian import perkalian
from components.operator_matematika.pembagian import pembagian

page_names_to_funcs = {
    "Penjumlahan" : penjumlahan,
    "Pengurangan" : pengurangan,
    "Perkalian"   : perkalian,
    "Pembagian"   : pembagian,
}

demo_name = st.sidebar.selectbox(
    "Pilih Operator Matematika", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
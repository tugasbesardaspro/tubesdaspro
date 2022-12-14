import streamlit as st

from components.kecepatan.kecepatan import kecepatan
from components.kecepatan.jarak import jarak
from components.kecepatan.waktu import waktu

page_names_to_funcs = {
    "Kecepatan": kecepatan,
    "Jarak": jarak,
    "Waktu": waktu,

}

demo_name = st.sidebar.selectbox(
    "Mencari Kecepatan, Jarak, Waktu", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
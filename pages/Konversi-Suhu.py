import streamlit as st

from components.suhu.fahrenheit import fahrenheit
from components.suhu.reamur import reamur
from components.suhu.kelvin import kelvin

page_names_to_funcs = {
    "Fahrenheit": fahrenheit,
    "Reamur": reamur,
    "Kelvin": kelvin,
}

demo_name = st.sidebar.selectbox(
    "Pilih Konversi Suhu", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
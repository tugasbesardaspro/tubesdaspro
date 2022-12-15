import streamlit as st

from components.bangun_datar.persegi import persegi
from components.bangun_datar.persegi_panjang import persegi_panjang
from components.bangun_datar.lingkaran import lingkaran
from components.bangun_datar.segitiga import segitiga
from components.bangun_datar.jajargenjang import jajargenjang

page_names_to_funcs = {
    "Persegi": persegi,
    "Persegi Panjang": persegi_panjang,
    "Lingkaran": lingkaran,
    "Segitiga": segitiga,
    "Jajargenjang": jajargenjang,
}

demo_name = st.sidebar.selectbox(
    "Pilih bangun datar", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

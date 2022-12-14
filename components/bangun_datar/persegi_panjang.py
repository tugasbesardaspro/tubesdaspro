import streamlit as st
from custom_module.custom import *

import codecs

# Components Pkgs
import streamlit.components.v1 as components
from custom_module.custom import *

def blueprint(param, param2):
  
  global panjang_persegi_panjang
  global lebar_persegi_panjang
  panjang_persegi_panjang = st.number_input("Masukkan Panjang :", key=param)
  lebar_persegi_panjang = st.number_input("Masukkan Lebar :" , key=param2)
  return panjang_persegi_panjang , lebar_persegi_panjang

def luas_persegi_panjang():
  st.header("BANGUN DATAR PERSEGI PANJANG")

  st.subheader("Mencari Luas")

  blueprint(4,5)

  btn_luas = btnhasil(2)

  if btn_luas:
      result_luas = panjang_persegi_panjang * lebar_persegi_panjang 

      rumusbangundatar("Luas", "Persegi Panjang", "P x L")

      resultbangundatar("Luas", "Persegi Panjang", result_luas)


def keliling_persegi_panjang():
  st.subheader("Mencari Keliling")

  blueprint(7,8)

  btn_keliling = btnhasil(1)

  if btn_keliling:

      result_keliling = (2*panjang_persegi_panjang) + (2*lebar_persegi_panjang)

      rumusbangundatar("Keliling", "Persegi Panjang", "2P x 2L")

      resultbangundatar("Keliling", "Persegi Panjang", result_keliling)

def persegi_panjang():
    import streamlit as st

    luas_persegi_panjang()
    keliling_persegi_panjang()
   
import streamlit as st
from custom_module.custom import *

def blueprint(param, param2):
  
  global alas_segitiga
  global tinggi_segitiga
  alas_segitiga = st.number_input("Masukkan Alas :", key=param)
  tinggi_segitiga = st.number_input("Masukkan Tinggi :" , key=param2)
  return alas_segitiga , tinggi_segitiga

def keliling(param, param2, param3):
    global a
    global b
    global c
    a = st.number_input("Masukkan sisi A :", key=param)
    b = st.number_input("Masukkan sisi B :" , key=param2)
    c = st.number_input("Masukkan sisi C :" , key=param3)
    return a, b, c

def luas_segitiga():
  st.header("BANGUN DATAR SEGITIGA")

  st.subheader("Mencari Luas")

  blueprint(4,5)

  btn_luas = btnhasil(2)

  if btn_luas:
      result_luas = 1/2 * alas_segitiga * tinggi_segitiga 

      rumusbangundatar("Luas", "Segitiga", "1/2 x a x t")

      resultbangundatar("Luas", "Segitiga", result_luas)


def keliling_segitiga():
  st.subheader("Mencari Keliling")

  keliling(7,8,9)

  btn_keliling = btnhasil(1)

  if btn_keliling:

      result_keliling = a + b + c

      rumusbangundatar("Keliling", "Segitiga", "a + b + c")

      resultbangundatar("Keliling", "Segitiga", result_keliling)

def segitiga():
    import streamlit as st

    luas_segitiga()
    keliling_segitiga()
   
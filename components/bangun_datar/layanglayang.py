import streamlit as st
from custom_module.custom import *
import codecs
import streamlit.components.v1 as components

def luas_layang():
  st.header("BANGUN DATAR LAYANG LAYANG")

  st.subheader("Mencari Luas")

  d1 = st.number_input("Masukkan Nilai Sisi Diagonal 1: ")
  d2 = st.number_input("Masukkan Nilai Sisi Diagonal 2: ")

  result_luas = (d1 * d2)/2

  f=codecs.open("./components/htmlFiles/luas-layangan.html", 'r')
  page9 = f.read().format(dig1 = d1, dig2 = d2)
  components.html(page9,width=320,height=250,scrolling=False)
  
  if st.button("Luas Layang Layang"):
      
      rumusbangundatar("Luas", "Layang Layang", "(Diagonal 1 x Diagonal 2) / 2")
      resultbangundatar("Luas", "Layang Layang", result_luas)
      penjelasan("Luas layang-layang adalah setengah hasil kali panjang diagonal-diagonalnya. Rumus untuk menentukan luas layang-layang adalah: Luas = 1/2 × (d)1 × (d)2. Di sini (d)1 dan (d)2 adalah panjang dan pendek diagonal layang-layang.")

def keliling_layang():
  st.subheader("Mencari Keliling")

  panjanglayang = st.number_input("Masukkan Panjang :", key = 1)
  lebarlayang = st.number_input("Masukkan Lebar :", key = 2)

  result_keliling = (2 * panjanglayang) + (2 * lebarlayang)

  f=codecs.open("./components/htmlFiles/keliling-layang.html", 'r')
  page10 = f.read().format(panjang = panjanglayang, lebar = lebarlayang)
  components.html(page10,width=520,height=270,scrolling=False)
  
  if st.button("Keliling Layang Layang"):
      rumusbangundatar("Keliling", "Layang Layang", "(2 x panjang) + (2 x lebar)")
      resultbangundatar("Keliling", "Layang Layang", result_keliling)
      penjelasan("Keliling layang-layang = 2 (a + b) Penjelasannya, a dan b adalah panjang kedua pasang sisi layang-layang dengan ukuran yang sama.")

def layang():    
    luas_layang()
    keliling_layang()
   
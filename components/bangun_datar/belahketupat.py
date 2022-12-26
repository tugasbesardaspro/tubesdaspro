import streamlit as st
import codecs
import streamlit.components.v1 as components
from custom_module.custom import *

def luas_ketupat():
  st.header("BANGUN DATAR BELAH KETUPAT")

  st.subheader("Mencari Luas")

  d1 = st.number_input("Masukkan Nilai Sisi Diagonal 1: ")
  d2 = st.number_input("Masukkan Nilai Sisi Diagonal 2: ")

  result_luas = (d1 * d2)/2

  f=codecs.open("./components/htmlFiles/luas-belahketupat.html", 'r')
  page10 = f.read().format(d1 = d1, d2 = d2)
  components.html(page10,width=310,height=310,scrolling=False)

  if st.button("Luas Belah Ketupat"):
      
      rumusbangundatar("Luas", "Belah Ketupat", "(Diagonal 1 x Diagonal 2) / 2")
      resultbangundatar("Luas", "Belah Ketupat", result_luas)
      penjelasan("Luas belah ketupat adalah setengah perkalian panjang diagonal-diagonalnya. Maka rumus luas belah ketupat adalah ½ × d1 × d2. Sebagai keterangan, d1 dan d2 adalah diagonal sisi dalam bangun datar belah ketupat.")

def keliling_ketupat():
  st.subheader("Mencari Keliling")
  s = st.number_input("Masukkan Sisi :")
  result_keliling = 4*s
  f=codecs.open("./components/htmlFiles/keliling-belahketupat.html", 'r')
  page12 = f.read().format(keliling = result_keliling)
  components.html(page12,width=310,height=310,scrolling=False)

  if st.button("Keliling Belah Ketupat"):
      rumusbangundatar("Keliling", "Belah Ketupat", "4 x Sisi (s)")
      resultbangundatar("Keliling", "Belah Ketupat", result_keliling)
      penjelasan("Keliling suatu belah ketupat adalah jumlah semua panjang sisinya atau empat kali jumlah panjang sisinya. Jadi, rumus keliling belah ketupat adalah K = 4s dengan K sebagai lambang keliling. Sedangkan s adalah panjang sisi.")

def ketupat():    
    luas_ketupat()
    keliling_ketupat()
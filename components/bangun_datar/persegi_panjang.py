import streamlit as st
from custom_module.custom import *
import codecs
import streamlit.components.v1 as components
from custom_module.custom import *



def luas_persegi_panjang():
  st.header("BANGUN DATAR PERSEGI PANJANG")

  st.subheader("Mencari Luas")

  panjang_pp_luas = st.number_input("Masukkan Panjang :")
  lebar_pp_luas = st.number_input("Masukkan Lebar :")

  result_luas = panjang_pp_luas * lebar_pp_luas

  f=codecs.open("./components/htmlFiles/luas-pp.html", 'r')
  page3 = f.read().format(panjang = panjang_pp_luas, lebar = lebar_pp_luas)
  components.html(page3,width=390,height=200,scrolling=False)


  if st.button("Luas Persegi Panjang"):
      

      rumusbangundatar("Luas", "Persegi Panjang", "P x L")


      resultbangundatar("Luas", "Persegi Panjang", result_luas)

      penjelasan("Persegi Panjang memiliki besaran yang menyatakan ukuran dua dimensi dari bagian daerah dalamnya. Besaran ini kita sebut sebagai luas. Rumus luas persegi panjang adalah L = p x l. Bila kamu mengetahui ukuran panjang dan lebar persegi panjang, maka kamu dapat menentukan luasnya")


def keliling_persegi_panjang():
  st.subheader("Mencari Keliling")

  panjang_pp_keliling = st.number_input("Masukkan Panjang :", key = 1)
  lebar_pp_keliling = st.number_input("Masukkan Lebar :", key = 2)

  result_keliling = (2*panjang_pp_keliling) + (2*lebar_pp_keliling)

  f=codecs.open("./components/htmlFiles/keliling-pp.html", 'r')
  page3 = f.read().format(panjang = panjang_pp_keliling*2, lebar = lebar_pp_keliling*2)
  components.html(page3,width=390,height=200,scrolling=False)


  if st.button("Keliling Persegi Panjang"):


      rumusbangundatar("Keliling", "Persegi Panjang", "2P x 2L")


      resultbangundatar("Keliling", "Persegi Panjang", result_keliling)
      
      penjelasan("Keliling persegi panjang didefinisikan sebagai jumlah semua empat sisinya. Dalam kasus persegi panjang, sisi-sisi yang berlawanan dari sebuah persegi panjang adalah sama. Jadi kelilingnya akan menjadi dua kali lebar persegi panjang ditambah panjang persegi panjang.")

def persegi_panjang():    
    luas_persegi_panjang()
    keliling_persegi_panjang()
   
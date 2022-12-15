import streamlit as st
import codecs
import streamlit.components.v1 as components
from custom_module.custom import *



def luas_segitiga():
  st.header("BANGUN DATAR SEGITIGA")

  st.subheader("Mencari Luas")

  alas_segitiga = st.number_input("Masukkan Alas :")
  tinggi_segitiga = st.number_input("Masukkan Tinggi :")

  f=codecs.open("./components/htmlFiles/luas-segitiga.html", 'r')
  page7 = f.read().format(alas = alas_segitiga, tinggi = tinggi_segitiga)
  components.html(page7,width=300,height=200,scrolling=False)

  result_luas = (1/2) * alas_segitiga * tinggi_segitiga 

  if st.button("Luas Segitiga"):

      rumusbangundatar("Luas", "Segitiga", "(1/2) x a x t")

      resultbangundatar("Luas", "Segitiga", result_luas)

      penjelasan("Luas segitiga didefinisikan sebagai total ruang yang ditempati oleh ketiga sisi segitiga pada bidang 2 dimensi.")


def keliling_segitiga():
  st.subheader("Mencari Keliling")

  a = st.number_input("Masukkan sisi A :")
  b = st.number_input("Masukkan sisi B :")
  c = st.number_input("Masukkan sisi C :")

  f=codecs.open("./components/htmlFiles/keliling-segitiga.html", 'r')
  page8 = f.read().format(a = a, b= b, c=c)
  components.html(page8,width=300,height=200,scrolling=False)


  result_keliling = a + b + c

  if st.button("Keliling Segitiga"):


      rumusbangundatar("Keliling", "Segitiga", "a + b + c")

      resultbangundatar("Keliling", "Segitiga", result_keliling)

      penjelasan("Keliling segitiga adalah nilai total dari panjang sisi yang dimiliki segitiga. Dengan demikian, rumus keliling segitiga adalah K =a + b + c atau penjumlahan total dari semua sisi segitiga tersebut.")

def segitiga():
    import streamlit as st

    luas_segitiga()
    keliling_segitiga()
   
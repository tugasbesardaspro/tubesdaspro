import streamlit as st
import pandas as pd
import numpy as np

data = {
  "+" : "Tambah",
  "-" : "Kurang",
  "x atau *" : "Kali",
  "/":"Bagi"
}

st.header("Kamus Operator dan Simbol Matematika")

my_set = (
    ["+", "tambah", "1 + 1 = 2"],  
    ["-", "Kurang", "1 - 1 = 0"],   
    ["* atau  x ", "Kali", "1 * 1 = 1"],   
    ["/", "Bagi", "1 / 1 = 1"],   
    ["^", "Pangkat", "3^2 = 9"],   
    ["<", "Lebih Kecil", "1 < 2"],   
    [">", "Lebih Besar", "2 > 1"],   
    ["=", "Sama dengan", "1 = 1"],   
    ["≠", "Tidak sama dengan", "1 ≠ 2"],   
    ["≤", "Lebih Kecil atau sama dengan", "1 ≤ 3 = 1 , 2 , 3"],   
    ["≥", "Lebih besar atau sama dengan", "3 ≥ 1 = 3 , 2 , 1"],   
    ["Mod", "Hasil bagi", "5 Mod 2 = 1"],   
    ["√", "Akar pangkat 2", " √4 = 2"],   
    ["π", "Pi", "3,14"],   
    ["!", "Faktorial", "5! = 1 x 2 x 3 x 4 x 5 = 120"],   
    ["%", "Persen", "10% × 30 = 3"],   
    ["‰", "Per-mil", "10 ‰ × 30 = 0,3"],   
    ["ppm", "Per-juta", "10ppm × 30 = 0,0003"],   
    ["ppb", "Per-miliar", "10ppb × 30 = 3 × 10 -7"],   
    ["ppt", "Per-triliun", "10ppt × 30 = 3 × 10-10"],   
)

# Convert the set to a dataframe
df = pd.DataFrame(my_set)

headers = ["Simbol Operator", "Nama Operator", "Contoh / Penjelasan"]

# Tentukan lebar kolom dan baris yang diinginkan
column_width = 20
row_height = 30



df.columns = headers
df.index = np.arange(1,len(df)+1)

st.table(df)
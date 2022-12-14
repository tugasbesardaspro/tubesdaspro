import streamlit as st

#Button
def btnhasil(count):
    return st.button("Hasil", key=count)

#Bangun Datar
def resultbangundatar(types, category, param):
    return st.success(f"{types} {category} adalah : {param} Cm")
def rumusbangundatar(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")

#Suhu
def resultsuhu(types, category, param):
    return st.success(f"{types} {category} adalah : {param}")
def rumussuhu(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")

#Operator
def resultoperator(types, category, param):
    return st.info(f"{types} {category} adalah : {param}")
def rumusoperator(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")

#Kecepatan
def rumuskecepatan(types, category, param):
    return st.info(f"Rumus {types} {category} : {param}")
def resulkecepatan(types, category, param):
    return st.success(f"{types} {category} adalah : {param}")
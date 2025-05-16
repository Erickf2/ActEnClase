import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mi primera app", layout="centered")

st.title("Mi primer test con Streamlit")
st.write("Este es un ejemplo básico para probar un deploy con GitHub.")

# Input de usuario
nombre = st.text_input("¿Cómo te llamas?")
edad = st.slider("¿Cuántos años tienes?", 0, 100, 25)

# Botón para mostrar mensaje
if st.button("Enviar"):
    st.success(f"Hola, {nombre}. Tienes {edad} años.")

# Mostrar un DataFrame de ejemplo
st.subheader("Ejemplo de DataFrame")
df = pd.DataFrame({
    'Columna A': np.random.randint(0, 100, 10),
    'Columna B': np.random.rand(10)
})
st.dataframe(df)

# Mostrar un gráfico
st.subheader("Gráfico de ejemplo")
st.line_chart(df)

# Mostrar imagen opcional (de una URL)
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=250)
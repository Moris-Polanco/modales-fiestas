import openai
import streamlit as st
import os
import re

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Crear una función para hacer una llamada independiente a la API
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Pida el título del libro
st.header("Generador de libros de buenos modales")
title = st.text_input("Introduce el título del libro:")

# Pida el número de capítulos
num_chapters = st.number_input("Introduce el número de capítulos:")

# Generar el libro
if st.button("Generar libro"):
    st.header(title)
    for i in range(num_chapters):
        prompt = f"Escribe el contenido del capítulo {i+1}:"
        chapter = generate_text(prompt)
        st.write(chapter)

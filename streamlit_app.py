import openai
import streamlit as st
import os
import re

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Función para generar texto usando GPT-3
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2024,
        n=1,
        stop=None,
        temperature=0.7,
        presence=author,
        genre=genre
    )

    message = completions.choices[0].text
    message = re.sub("[^0-9a-zA-Z]+", " ", message).strip()
    return message

# Pida el título del libro
st.header("Generador de libros")
title = st.text_input("Introduce el título del libro:")

# Pida el género del libro
genre = st.text_input("Introduce el género del libro:")

# Pida el autor a imitar
author = st.text_input("Introduce el autor a imitar:")

# Pida el número de capítulos
num_chapters = st.number_input("Introduce el número de capítulos:")
num_chapters = int(num_chapters)

# Generar el libro
if st.button("Generar libro"):
    st.header(title)
    progress_bar = st.progress(0)
    for i in range(num_chapters):
        progress_bar.progress((i + 1) / num_chapters)
        prompt = f"Escribe el contenido del capítulo {i+1}:"
        chapter = generate_text(prompt, genre, author)
        st.write(chapter)
    progress_bar.empty()

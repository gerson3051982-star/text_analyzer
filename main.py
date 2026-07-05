# Importar las funciones del módulo text_analyzer

from analizer.text_analyzer import count_words, count_characters, count_sentences, longest_word



text = "Hola mundo, esta es una prueba del analizadores de texto. En esta prueba, vamos a contar las palabras, los caracteres, las oraciones y la palabra más larga."
# Pedir al usuario que ingrese un texto
print(f"Numero de palabras: {count_words(text)}")
print(f"Numero de caracteres: {count_characters(text)}")
print(f"Numero de oraciones: {count_sentences(text)}")
print(f"La palabra más larga es: {longest_word(text)}")

# 


    
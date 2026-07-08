import sys
import os
#Agregar la ruta padre para poder importar el modulo text_analyzer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from analizer.text_analyzer import count_words, count_characters, count_sentences, longest_word



def test_count_words():
    text = "hola mundo"
    assert count_words(text) == 2

def test_count_characters():
    text = "hola"
    assert count_characters(text) == 4

def test_count_sentences():
    text = "hola mundo. Esto es una prueba!" 
    assert count_sentences(text) == 2

def test_longest_word():
    text = "hola mundo de programación en java"
    assert longest_word(text) == "programación"


if __name__ == "__main__":
    print("Ejecutando pruebas ...")

    # Ejecutar las pruebas
    test_count_words()
    print("Prueba de conteo ejecutada correctamente")
    test_count_characters()
    print("Prueba de caracteres ejecutada correctamente")
    test_count_sentences()
    print("Prueba de oraciones ejecutada correctamente")
    test_longest_word()
    print("Prueba de palabra mas larga ejecutada correctamente")

    print("Pruebas ejecutadas correctamente")

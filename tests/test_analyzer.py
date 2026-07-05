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
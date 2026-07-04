def count_words(text):
    """Función que cuenta las palabras de un texto"""
    words = text.split()
    return len(words)   

def count_characters(text):
    """Función que cuenta los caracteres de un texto"""
    return len(text)    

def count_sentences(text):
    """Función que cuenta las oraciones de un texto"""
    sentences = text.count(".") + text.count("!") + text.count("?")
    return sentences 

def longest_word(text):
    """Función que encuentra la palabra más larga de un texto"""
    if not text or not text.strip():
        return "No se recibió texto válido"
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def count_paragraphs(text):
    """Función que cuenta los párrafos de un texto"""
    return text.count('\n\n') + 1   

def count_vowels(text):
    """Función que cuenta las vocales de un texto"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count    

def count_consonants(text):
    """Función que cuenta las consonantes de un texto"""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count    

def count_spaces(text):
    """Función que cuenta los espacios de un texto"""
    return text.count(' ')    

def count_numbers(text):
    """Función que cuenta los números de un texto"""
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count    

def count_special_characters(text):
    """Función que cuenta los caracteres especiales de un texto"""
    special_characters = "!@#$%^&*()_+=-`~[]{}|\;:'",.<>/?"
    count = 0
    for char in text:
        if char in special_characters:
            count += 1
    return count    

def count_words_by_length(text):
    """Función que cuenta las palabras de un texto por longitud"""
    words = text.split()
    word_counts = {}
    for word in words:
        length = len(word)
        if length in word_counts:
            word_counts[length] += 1
        else:
            word_counts[length] = 1
    return word_counts

def count_words_by_vowel(text):
    """Función que cuenta las palabras de un texto por vocal"""
    words = text.split()
    word_counts = {}
    for word in words:
        count = count_vowels(word)
        if count in word_counts:
            word_counts[count] += 1
        else:
            word_counts[count] = 1
    return word_counts

def count_words_by_consonant(text):
    """Función que cuenta las palabras de un texto por consonante"""
    words = text.split()
    word_counts = {}
    for word in words:
        count = count_consonants(word)
        if count in word_counts:
            word_counts[count] += 1
        else:
            word_counts[count] = 1
    return word_counts

def count_words_by_length_and_vowel(text):
    """Función que cuenta las palabras de un texto por longitud y vocal"""
    words = text.split()
    word_counts = {}
    for word in words:
        length = len(word)
        vowel_count = count_vowels(word)
        if length in word_counts:
            if vowel_count in word_counts[length]:
                word_counts[length][vowel_count] += 1
            else:
                word_counts[length][vowel_count] = 1
        else:
            word_counts[length] = {vowel_count: 1}
    return word_counts
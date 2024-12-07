from collections import Counter
import string

def count_unique_words(input_string):
    
    translator = str.maketrans('', '', string.punctuation)
    
    cleaned_string = input_string.translate(translator).lower()
    words = cleaned_string.split()
    word_count = Counter(words)
    
    return len(word_count)

input_string = "Привет, мир! Привет, как дела? Мир, как ты?"
unique_word_count = count_unique_words(input_string)

print(f"Количество уникальных слов: {unique_word_count}")
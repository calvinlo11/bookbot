def num_of_words(word_count):
    num = len(word_count.split())
    return f"{num} words found in the document"

def count_characters(text):
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

    
    return letters

def sort_function(sort_numbers):
    return sort_numbers()
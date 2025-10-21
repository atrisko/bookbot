def count_words(text):
    words = text.split()
    number = len(words)
    return number

def count_characters(text):
    
    characters = {}
    
    text = text.lower()

    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
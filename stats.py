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

def sort_on(items):
    return items["num"]

def sorted_character_count(characters):
    items = [
        {"char": ch, "num": count}
        for ch, count in characters.items()
        if ch.isalpha()
    ]
    items.sort(key=sort_on, reverse=True)
    return items

        


    

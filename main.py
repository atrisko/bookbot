from stats import count_words, count_characters, sorted_character_count


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


def main():
  text = get_book_text("./books/frankenstein.txt")
  words = count_words(text)
  characters = sorted_character_count(count_characters(text))

  print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {words} total words")
  print("--------- Character Count -------")
  for item in characters:
    print(f"{item['char']}: {item['num']}")
  print("============= END ===============")
  

  
  

main()

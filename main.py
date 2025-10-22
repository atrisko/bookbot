import sys
from stats import count_words, count_characters, sorted_character_count


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


def main():

  if len(sys.argv) != 2:
    print("Usage: python main.py <path-to-book>")
    sys.exit(1)
  else:
    path = sys.argv[1]
    text = get_book_text(path)
    words = count_words(text)
    characters = sorted_character_count(count_characters(text))
  print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------\nFound {words} total words")
  print("--------- Character Count -------")
  for item in characters:
    print(f"{item['char']}: {item['num']}")
  print("============= END ===============")
  

  
  

main()

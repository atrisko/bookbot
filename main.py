import sys
from stats import count_words, count_characters, sorted_character_count


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


def main(book_path):
  text = get_book_text(book_path)
  words = count_words(text)
  characters = sorted_character_count(count_characters(text))
  print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {words} total words")
  print("--------- Character Count -------")
  for item in characters:
    print(f"{item['char']}: {item['num']}")
  print("============= END ===============")
  

  
  

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])

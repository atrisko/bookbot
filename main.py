from stats import count_words, count_characters


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


def main():
  text = get_book_text("./books/frankenstein.txt")
  words = count_words(text)
  print(f"Found {words} total words")

  characters = count_characters(text)
  print(characters)

main()
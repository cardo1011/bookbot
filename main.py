from stats import word_count
from stats import count_char_in
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as text:
        file_contents = text.read()
    return file_contents

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    string_of_text_from_the_book = get_book_text(sys.argv[1])
    book_word_count = len(word_count(string_of_text_from_the_book))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count ------- ")

    character_count_dict = count_char_in(string_of_text_from_the_book)

    sorted_char_count_list_of_dictionaries =sort_dict(character_count_dict)

    for element in sorted_char_count_list_of_dictionaries:
        char = element["char"]
        num = element["num"]

        print(
            f"{char}: {num}"
        )


main()

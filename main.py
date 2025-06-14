from stats import word_count
from stats import count_char_in
# from stats import sort_char_count

def get_book_text(filepath):
    with open(filepath) as text:
        file_contents = text.read()
    return file_contents

def main():
    string_of_text_from_the_book = get_book_text("books/frankenstein.txt")
    book_word_count = len(word_count(string_of_text_from_the_book))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} words found in the document")
    print("--------- Character Count ------- ")

    character_count = count_char_in(string_of_text_from_the_book)
    # character_count.sort(reverse=True, key=sort_char_count)

    print(character_count)


main()

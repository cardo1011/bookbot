def word_count(text_as_string):
    # split all the words in the text into a list
    word_list = text_as_string.split()
    return word_list

def count_char_in(text_as_string):
    # setting all characters in a string to lowercase
    all_text_to_lower_case = text_as_string.lower()

    # initializing a dict
    char_count = {}

    # iterating through each of the lowercase string
    for char in all_text_to_lower_case:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        # decided to exc
        elif char == " " or char == "\n" or char == '™':
            pass
        else:
            char_count[char] = 1
    return char_count


# def sort_char_count(dict):
#     characters = {"char"}
#     for char in dict:
        
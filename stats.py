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
        else:
            char_count[char] = 1
    return char_count


def sort_on(list_of_dictionaries):
    return list_of_dictionaries["num"]

def sort_dict(dict):
    char_dict_list =[]
    
    for i in dict:
        if i.isalpha():
            char_dict_list.append(
                {"char": i, "num": dict[i]}
            )

    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list




    
        
def create_new_string(string):
    # Get the first character
    first_character = string[0]

    # get the middle character
    middle_index = len(string) // 2
    middle_character = string[middle_index]

    # get the last character
    last_character = string[-1]

    # Combine them with the 3 dashes in between
    my_brand_new_string = f"{first_character}---{middle_character}---{last_character}"

    return my_brand_new_string

test_string = "Glanmire"
result = create_new_string(test_string)
print(result)

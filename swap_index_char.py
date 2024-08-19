

def swap_even_odd(string):
    new_char_list = list(string)
    for i in range(0, len(string) - 1, 2):
        new_char_list[i], new_char_list[i+1] = new_char_list[i+1], new_char_list[i]
    return "".join(new_char_list)

print(swap_even_odd("abcdefghijklmnopqrstuvwxyz"))

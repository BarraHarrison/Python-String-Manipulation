greeting_string = "hello"
alphabet_string = "abcdefghikjlmnopqrstuvwxyz"

char_list = list(greeting_string)
char_list[0],char_list[4]=char_list[4],char_list[0]
swap_first_last = "".join(char_list)
print(swap_first_last)

second_char_list = list(alphabet_string)
second_char_list[0],second_char_list[25]=second_char_list[25],second_char_list[0]
alphabet_swap = "".join(second_char_list)
print(alphabet_swap)
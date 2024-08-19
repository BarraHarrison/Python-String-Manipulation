man = "Barra"
woman = "Kristen"


char_list = list(man)
char_list[0],char_list[3]=char_list[3],char_list[0]
new_man = "".join(char_list)
print(new_man)

list_char = list(woman)
list_char[0],list_char[6]=list_char[6],list_char[0]
new_woman = "".join(list_char)
print(new_woman)
greeting_words = ("hello world")
traffic_phrase = ("Green means go")

words = greeting_words.split()
swap_greeting_words = " ".join([words[1], words[0]])
print(swap_greeting_words)

traffic_words = traffic_phrase.split()
swap_traffic_phrase = " ".join([traffic_words[2], traffic_words[1], traffic_words[0]])
print(swap_traffic_phrase)
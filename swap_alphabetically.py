def swap_words_alphabetically(string):
    # Split the string into two words
    words = string.split()

    # Ensure the string contains exactly two words
    if len(words) != 2:
        raise ValueError("The string must contain exactly two words")

    # Compare and swap if necessary
    if words[0] > words[1]:
        words[0], words[1] = words[1], words[0]

    # Join the words back into a single string
    return " ".join(words)

print(swap_words_alphabetically("Tea Coffee"))
print(swap_words_alphabetically("Man Woman"))
print(swap_words_alphabetically("True False"))
print(swap_words_alphabetically("Red Blue"))
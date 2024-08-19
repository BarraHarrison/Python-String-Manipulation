def word_frequency_counter(text):
    # Remove punctuation from the text
    for char in "-.,\n":
        text = text.replace(char, " ")
    
    # Convert text to lowercase
    text = text.lower()
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

# Example text
text = "Hello world! Welcome to the world of Python. Python is great, and the world of programming loves Python."

# Call the function and print the word frequencies
frequencies = word_frequency_counter(text)
print(frequencies)

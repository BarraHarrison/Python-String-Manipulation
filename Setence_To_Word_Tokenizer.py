def sentence_to_word_tokenizer(paragraph):
    # Step 1: Split the paragraph into sentences
    sentences = paragraph.split('.')
    
    # Create a list to hold the tokenized sentences
    tokenized_sentences = []
    
    # Step 2: Iterate over each sentence
    for sentence in sentences:
        # Strip leading and trailing whitespace
        sentence = sentence.strip()
        
        # Skip empty sentences
        if not sentence:
            continue
        
        # Step 3: Split the sentence into words
        words = sentence.split()
        
        # Append the list of words to the tokenized_sentences list
        tokenized_sentences.append(words)
    
    return tokenized_sentences

# Example usage
paragraph = """
Python is a powerful programming language. It is widely used in web development, data science, artificial intelligence, and more.
This sentence to word tokenizer will split this paragraph into sentences and then into words. Let's see how it works!
"""

# Call the function and print the tokenized sentences
tokenized_output = sentence_to_word_tokenizer(paragraph)
for i, sentence in enumerate(tokenized_output):
    print(f"Sentence {i + 1}: {sentence}")

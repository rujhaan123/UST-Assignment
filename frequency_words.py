# frequency_words.py

def word_frequency(text):
    # Preprocess the input (convert to lowercase and split into words)
    words = text.lower().split()

    # Create a dictionary to count word frequencies
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Sort the dictionary by word (key) alphanumerically
    sorted_frequency = dict(sorted(frequency.items()))

    # Return the sorted frequency dictionary
    return sorted_frequency
# Ask the user to enter a line of text
text = input("Text: ")

# Split the input string into words
words = text.split()

# Creat an empty dictionary to store word counts
word_to_count = {}

# Creat loop
for word in words:
    word = word.lower()
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1


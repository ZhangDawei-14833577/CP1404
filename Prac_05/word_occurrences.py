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

# Sort the words alphabetically
sorted_words = sorted(word_to_count.keys())

# Find the longest length(for alignment)
max_length = max(len(word) for word in sorted_words)

# Print the results nearly aligned
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")



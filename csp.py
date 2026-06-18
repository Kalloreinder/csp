# CSP Game

# DRAFTING THE CONCEPT  

# Test string
my_string = "SEND + MORE = MONEY"

# Splitting the string into an array of words
my_words = my_string.split('+')
my_words += my_words.pop().split('=')

# Removing unwanted spaces in each word
for i in range(len(my_words)):
    my_words[i] = my_words[i].strip()

my_letters = [] # Array of unique letters in the words
first_letter = [] # Array of first letter of each word

# Check for each character, make sure it's a letter and that it is unique
for word in my_words:
    for letter in word:
        if letter not in my_letters and letter.isalpha():
            my_letters.append(letter)
    first_letter.append(word[0])

# Print something on screen for info
print("=" * 80)
print(f"Words to check: {my_words}")
print(f"Unique letters in words: {my_letters}")
print(f"First letter of each word: {first_letter}")
print("=" * 80)

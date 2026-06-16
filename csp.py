# CSP Game

# DRAFTING THE CONCEPT  

my_string = "SEND + MORE = MONEY"

my_words = my_string.split('+')
my_words += my_words.pop().split('=')

for i in range(len(my_words)):
    my_words[i] = my_words[i].strip()

print(my_words)

my_letters = []
first_letter = []

for word in my_words:
    for letter in word:
        if letter not in my_letters and letter.isalpha():
            my_letters.append(letter)
    first_letter.append(word[0])

print(my_letters)
print(first_letter)
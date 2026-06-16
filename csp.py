my_string = "SEND + MORE = MONEY"
my_letters = []

for letter in my_string:
    if letter not in my_letters and letter.isalpha():
        my_letters.append(letter)

print(my_letters)
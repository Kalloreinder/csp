my_string = "SEND + MORE = MONEY"
my_letters = []
first_letter = []

for letter in my_string:
    if letter not in my_letters and letter.isalpha():
        my_letters.append(letter)

first_letter.append(my_letters[0])
index = my_string.find('+') + 2

if index != -1:
    first_letter.append(my_string[index])

print(my_letters)
print(first_letter)
import random

print("Welcome to PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like\n"))

password_list = []

for letter in range(1, no_of_letters + 1):
    choice_letters = random.choice(letters)
    password_list.append(choice_letters)

for number in range(1, no_of_numbers + 1):
    choice_numbers = random.choice(numbers)
    password_list.append(choice_numbers)

for symbol in range(1, no_of_symbols + 1):
    choice_symbols = random.choice(symbols)
    password_list.append(choice_symbols)

random.shuffle(password_list)

password = ""
for item in password_list:
    password += item

print(password)
# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

easy_password = ""
# Get randomize letters
for idx in range(0,nr_letters):
    easy_password += letters[random.randint(0, len(letters)-1)] # easy_password += random.choice(letters)
# Get randomize symbols
for idx in range(0,nr_symbols):
    easy_password += symbols[random.randint(0, len(symbols)-1)] # easy_password += random.choice(symbols)
# Get randomize numbers
for idx in range(0,nr_numbers):
    easy_password += numbers[random.randint(0, len(numbers)-1)]  # easy_password += random.choice(numbers)

# Easy level (in order of input)
print(f"Here is your easy password: {easy_password}")

# Hard level (randomize)
password_list = []

# Get randomize letters
for idx in range(0,nr_letters):
    password_list.append(random.choice(letters))
# Get randomize symbols
for idx in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
# Get randomize numbers
for idx in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
hard_password = ''.join(password_list)

print(f"Here is your hard password: {hard_password}")
   
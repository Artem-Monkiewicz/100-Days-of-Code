import string
import random

letters = string.ascii_letters # biblio with all letters
numbers = string.digits # biblio with all numbers
symbols = string.punctuation # biblio with all symbols

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy
password_list = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers)
pass_str = ''.join(password_list)
print(password_list)

#Shuffle adding
random.shuffle(password_list)
print(password_list)

pass_end = ""
for char in password_list:
    pass_end += char

print(f"Your password is: {pass_end}")
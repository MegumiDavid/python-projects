#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_selected = []
for c in range (nr_letters):
  letters_selected.append(letters[random.randint(0,len(letters)-1)])

print(letters_selected)

numbers_selected = []
for c in range (nr_numbers):
  numbers_selected.append(numbers[random.randint(0,len(numbers)-1)])

print(numbers_selected)

symbols_selected = []
for c in range (nr_symbols):
  symbols_selected.append(symbols[random.randint(0,len(symbols)-1)])

print(symbols_selected)

all = [letters_selected,numbers_selected,symbols_selected]
password = []
for lista in all:
  password.extend(lista)

print(password)

for character in password:
  print(character, end="")
print()

random.shuffle(password)
print(password)
for characters in (password):
  print(characters, end="")



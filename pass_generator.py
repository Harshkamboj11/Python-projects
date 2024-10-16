import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '\\', '|', '`', '~']

print("welcome to password generator!! ")
letter = int(input("how many letters you want in your password?\n"))
number = int(input("how many numbers you want in your password?\n"))
symbol = int(input("how many symbols you want in your password?\n"))

password = ""

for i in range(1,letter+1):
    char = random.choice(letters)
    password = password + char

for j in range(1,number+1):
    num = random.choice(numbers)
    password = password + num

for k in range(1,symbol+1):
    sym = random.choice(symbols)
    password = password + sym

print(f"the generated password is {password}")
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print('Welcome to PyPassowrd Generator')
num_letters = int(input('How many letters would you like in your passowrd? \n'))
num_symbols = int(input('How many symbols would you like? \n'))
num_numbers = int(input('How many numbers would you like? \n'))

draft_password = []

for char in range(0, num_letters):
    draft_password += random.choice(letters)

for char in range(0, num_symbols):
    draft_password += random.choice(symbols)

for char in range(0, num_numbers):
    draft_password += random.choice(numbers)    

random.shuffle(draft_password)

password = ''
for char in draft_password:
    password += char

# the method below works but the method above is much better
# for char in range(0, len(draft_password)):
#     password += random.choice(draft_password)

print(f'Your password is {password}')

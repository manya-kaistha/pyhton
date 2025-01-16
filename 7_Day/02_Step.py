import random

word_list = ['arrow', 'balloon', 'camel']

chosen_word = random.choice(word_list)

placeholder = ''
for letter in chosen_word:
    placeholder += '_'

print(placeholder)

guessed_letter = input("Guess a letter: ").lower()

display = ''
for letter in chosen_word:
    if letter == guessed_letter:
        display += letter
    else:
        display += '_'

print(display)
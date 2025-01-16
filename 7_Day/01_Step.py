import random

word_list = ['arrow', 'balloon', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)

guessed_letter = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guessed_letter:
        print('Right')
    else:
        print('Wrong')
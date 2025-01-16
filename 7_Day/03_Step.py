import random

word_list = ['arrow', 'balloon', 'camel']

chosen_word = random.choice(word_list)

placeholder = ''
for letter in chosen_word:
    placeholder += '_'

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    display = ''

    for letter in chosen_word:
        if letter == guessed_letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if '_' not in display:
        game_over = True
        print('You Win!')

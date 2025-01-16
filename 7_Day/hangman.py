import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = [
    "abandon", "abundant", "adapt", "adverse", "aggravate", "ambiguous", "anxious", "apprehensive", "astonish", "beneficial",
    "bizarre", "candid", "capable", "cautious", "cease", "coherent", "commence", "complicate", "contribute", "conclude",
    "conform", "consistent", "convince", "cumbersome", "deficient", "deliberate", "denounce", "depress", "desolate", "diligent",
    "discreet", "distinct", "eloquent", "endorse", "engaging", "envious", "evaluate", "exhaust", "exquisite", "fluctuate",
    "formulate", "fragile", "futile", "grasp", "habitual", "hesitate", "imply", "inadequate", "incline", "indicate"
]



chosen_word = random.choice(word_list)

placeholder = ''
for letter in chosen_word:
    placeholder += '_'

print(placeholder)

game_over = False
correct_letters = []
lives = 6

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
    if guessed_letter not in correct_letters:
        lives -= 1

    print(display)
    print(f"You have {lives} lives left.")
    print(HANGMANPICS[(-lives)-1])

    if '_' not in display:
        game_over = True
        print('You Win!')
    elif lives == 0:
        game_over = True
        print('You Lose!')
        print(f"The word was {chosen_word}")

import random
import hangman_art
import hangman_words
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(hangman_art.logo)

random_word = random.choice(hangman_words.word_list)
length = len(random_word)

random_word_list = []

for i in random_word:
    random_word_list += i
print(random_word_list)

display = []

for letter in random_word:
    display += "_"
print(display)
display_num = display.count("_")

life = 7

while life != 0 or display.count("_") != 0:
    guess = input("Guess a letter: ")
    for i in range(0, length):
        if random_word_list[i] == guess:
            if (guess in display):
                print(f"You have already guessed {guess}")
            display[i] = random_word_list[i]
    if guess not in display:
        print(f"You guessed {guess}, thats not in the word. You lose a life.")
        life -= 1
    if life < 7:
        print(stages[life])
    print(f"{' '.join(display)}")
    if display.count("_") == 0:
        print("You win!!")
        break
    elif life == 0:
        print("You lose!!")
        break

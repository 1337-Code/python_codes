import random


def easy():
    correct_guess = False
    lives = 10
    number_to_guess = random.randint(1, 100)
    while correct_guess == False:
        guessed_number = int(input("Make a guess: "))
        if lives == 0:
            print("You ran out of lives. YOU LOSE!!")
            correct_guess = True
        elif guessed_number > number_to_guess:
            lives -= 1
            print("Too High.")
            print("Guess again")
            print(f"You have {lives} number of attempts left.")
            correct_guess == False
        elif guessed_number < number_to_guess:
            lives -= 1
            print("Too Low.")
            print("Guess again")
            print(f"You have {lives} number of attempts left.")
            correct_guess == False
        elif guessed_number == number_to_guess:
            print(f" {guessed_number} is the correct number. YOU WON!!")
            correct_guess = True


def hard():
    correct_guess = False
    lives = 5
    number_to_guess = random.randint(1, 100)
    while correct_guess == False:
        guessed_number = int(input("Make a guess: "))
        if lives == 0:
            print("You ran out of lives. YOU LOSE!!")
            correct_guess = True
        elif guessed_number > number_to_guess:
            lives -= 1
            print("Too High.")
            print("Guess again")
            print(f"You have {lives} number of attempts left.")
            correct_guess == False
        elif guessed_number < number_to_guess:
            lives -= 1
            print("Too Low.")
            print("Guess again")
            print(f"You have {lives} number of attempts left.")
            correct_guess == False
        elif guessed_number == number_to_guess:
            print(f" {guessed_number} is the correct number. YOU WON!!")
            correct_guess = True


print("Welcome to the Number Guessing Game!!")
print("I'm thinking of the number between 1 and 100")
difficulty = input("Choose a difficulty: 'Easy' or 'Hard'").lower()

if difficulty == "hard":
    hard()
elif difficulty == "easy":
    easy()

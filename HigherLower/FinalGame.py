import art
import game_data
import random
import os

end_of_game = False

SCORE = 0


def clear():
    return os.system('cls')


database = game_data.data
A = random.choice(database)
B = random.choice(database)


while end_of_game == False:
    clear()
    print(art.logo)
    A = B
    B = random.choice(database)
    if SCORE > 0:
        print("You are correct.")
        print(f"Your current score is {SCORE}.\n")

    print(f"Compare A : {A['name']}, {A['description']} from {A['country']}.")

    print(art.vs)

    print(f"Against B: : {B['name']}, {B['description']} from {B['country']}.")

    user_choice = input("Who has more followers? A or B: ").lower()

    if A['follower_count'] > B['follower_count']:
        correct_choice = "a"
    else:
        correct_choice = "b"

    if user_choice == correct_choice:
        SCORE += 1
        end_of_game = False
    else:
        print("You lose.")
        print(f"Your final score is {SCORE}.")
        end_of_game = True

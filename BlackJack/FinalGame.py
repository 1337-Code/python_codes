import random
import art
import os

end_of_game = False
user_defeat = False


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def comparision():
    if user_cards_sum < 21 and computer_cards_sum < 21:
        if user_cards_sum > computer_cards_sum:
            return 1
        else:
            return 2
    elif user_cards_sum > 21:
        return 3
    elif computer_cards_sum > 21:
        return 4
    elif user_cards_sum == 21:
        return 5
    elif computer_cards_sum == 21:
        return 6
    else:
        return 7


def hit():
    user_cards.append(random.choice(cards))
    if random.choice(computer_choices) == True:
        x = random.choice(computer_choices_number)
        for i in range(0, x):
            computer_cards.append(random.choice(cards))


def result(x):
    if x == 1:
        print("You won!!")
    elif x == 2:
        print("You lose!!")
    elif x == 3:
        print("You went over, You lose!!")
    elif x == 4:
        print("Opponent went over, You won!!")
    elif x == 5:
        print("You won!! BLACKJACK")
    elif x == 6:
        print("You lose!! Opponent's BLACKJACK")
    else:
        print("Draw")


def play_again():
    choice_to_play_again = input("Do you want to play again??").lower()
    if choice_to_play_again == "n":
        exit()


computer_choices = [True, False]
computer_choices_number = [1, 2]

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while end_of_game == False:
    if (input("Do you want to play Blackjack?: ")).lower() == "y":
        clearConsole()
    else:
        exit()
    print(art.logo)
    user_cards = [random.choice(cards), random.choice(cards)]
    user_cards_sum = sum(user_cards)
    computer_cards = [random.choice(cards), random.choice(cards)]
    computer_cards_sum = sum(computer_cards)
    print(
        f"Your cards are {user_cards}, and current score is: {user_cards_sum} ")
    print(f"Computer's first card is {computer_cards[0]}")
    x = comparision()
    if x == 3 or x == 4 or x == 5 or x == 6:
        print(
            f"Your final hand is: {user_cards}, and score is: {user_cards_sum} ")
        print(f"Computer's cards are {computer_cards}")
        result(x)
        play_again()

    while user_defeat == False:
        dec1 = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        if dec1 == "y":
            hit()
            user_cards_sum = sum(user_cards)
            computer_cards_sum = sum(computer_cards)
            if 11 in user_cards and user_cards_sum > 21:
                t = user_cards.index(11)
                user_cards[t] = 1
            user_cards_sum = sum(user_cards)

            if 11 in computer_cards and computer_cards_sum > 21:
                q = computer_cards.index(11)
                computer_cards[q] = 1
            computer_cards_sum = sum(computer_cards)
            print(
                f"Your final hand is: {user_cards}, and score is: {user_cards_sum} ")
            print(f"Computer's first card is {computer_cards[0]}")
            x = comparision()
            if x == 3 or x == 4 or x == 5 or x == 6:
                print(
                    f"Your final hand is: {user_cards}, and score is: {user_cards_sum} ")
                print(f"Computer's cards are {computer_cards}")
                result(x)
                user_defeat = True
                play_again()
            else:
                user_defeat = False
        elif dec1 == "n":
            user_cards_sum = sum(user_cards)
            computer_cards_sum = sum(computer_cards)
            n = comparision()
            print(
                f"Your final hand is: {user_cards}, and score is: {user_cards_sum} ")
            print(
                f"Computer's cards are {computer_cards} and Computer's score is {computer_cards_sum}")
            result(n)
            user_defeat = True
            play_again()

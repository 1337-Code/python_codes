import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if input("Do you want to start the BlackJack game? Y or N: ").lower() == "y":

    print(art.logo)
    user_cards = [random.choice(cards), random.choice(cards)]
    user_cards_sum = sum(user_cards)
    computer_cards = [random.choice(cards), random.choice(cards)]
    print(
        "Your cards are {user_cards}, and current score is: {user_cards_sum} ")
    print(f"Computer's first card is {computer_cards[0]}")


elif input("Do you want to start the BlackJack game? Y or N:").lower() == "n":
    exit()

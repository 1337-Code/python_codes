import random

print("Welcome to the RockPaperScissors game!!!")
player_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n>> "))


if player_choice == 0:
    print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif player_choice == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

computer_choice = random.randint(0,2)
print("Computer chose :")


if computer_choice == 0:
    print( '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer_choice == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


if (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print(f"You won!")
elif (player_choice == 2 and computer_choice == 0) or (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2):
    print("You lost")
else :
    print(f"Both chose the same, its a draw!")

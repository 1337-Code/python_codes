import art
import items
import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()
end_of_bid = False
print(art.logo)

Bidders = {}
Bid_opposite = {}

while end_of_bid == False:
    print("Welcome to the Secret Auction program.")
    name = input("What is your name?:")
    bid = int(input("What is your Bid?:"))
    other_bidders = input(
        ("Are there any other bidders?'Yes' or 'No'").lower())
    Bidders[name] = bid
    Bid_opposite[bid] = name

    if other_bidders == "yes":
        end_of_bid = False
    else:
        end_of_bid = True
    clearConsole()

for key in Bidders:
    bid_amount = Bidders[key]
    max = 0
    if bid_amount > max:
        max = bid_amount

print(f"The winner is {Bid_opposite[max]} with bid of {max}.")

print(Bidders)

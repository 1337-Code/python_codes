print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
nT = int(lower_name1.count("t")) + int(lower_name2.count("t"))
nR = int(lower_name1.count("r")) + int(lower_name2.count("r"))
nU = int(lower_name1.count("u")) + int(lower_name2.count("u"))
nE = int(lower_name1.count("e")) + int(lower_name2.count("e"))
nL = int(lower_name1.count("l")) + int(lower_name2.count("l"))
nO = int(lower_name1.count("o")) + int(lower_name2.count("o"))
nV = int(lower_name1.count("v")) + int(lower_name2.count("v"))
nE = int(lower_name1.count("e")) + int(lower_name2.count("e"))

first_digit = nT + nR + nU + nE
second_digit = nL + nO + nV + nE

score = str(first_digit) + str(second_digit)

if int(score)<10 or int(score)>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score)>40 and int(score)<50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}.")
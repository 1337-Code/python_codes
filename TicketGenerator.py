print("Welcome to our RollerCoaster!!")
height = int(input("What is your height(in cm)??"))
bill = 0
if height >= 120 :
    print("You can ride.")
    age = int(input("What is your age?"))
    if age <= 12 :
        bill = 5
        print("Your ticket cost is $5")
    elif age <= 18:
        bill = 7
        print("Your ticket cost is $7")
    elif age <= 22:
        bill = 9
        print("Your ticket cost is $9")
    elif age>45 and age<55:
        bill=0
    else :
        bill = 12
        print("Your ticket cost is $12")
    want_pic = input("Do you want pictures? Y or N ?")
    if want_pic == "Y":
        bill +=3
        print(f"Your total bill is ${bill}")
    if want_pic == "N":
        print(f"Your total bill is ${bill}")
else :
    print("You can't ride.")
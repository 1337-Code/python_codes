print("Welcome to the TipCalculator!!")
Bill = input("What is your total bill?$")
Percentage_tip = input("What percentage Tip would you like to give?: 10,12 or 15?")
NetBill = int(Bill)*((int(Percentage_tip)+100)/100)
peoplenumber = input("How many people to split the bill?")
split = NetBill/int(peoplenumber)
print(f"Each person have to pay:{round(split,2)}")
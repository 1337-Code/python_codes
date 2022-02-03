year = int(input("Which year do you want to check? "))
r1 = year%4
r2 = year%100
r3 = year%400

if r1==0:
    if r2 == 0:
        if r3 == 0:
            print("leap year")
        else:
            print("Not leap year.")
    else:
        print("leap year.")
else:
    print("Not leap year.")
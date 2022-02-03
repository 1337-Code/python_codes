import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PasswordGenerator!!")

letter_num = int(input("How many letters would you like in your password?")) 

symbols_num = int(input("How many symbols would you like in the passsword?")) 

digits_num = int(input("How many numbers would you like in the passsword?"))  

pass1=[]

for x in range(1, letter_num+1):
    x = random.choice(letters)
    pass1 +=x
for y in range(1,symbols_num+1):
    y = random.choice(symbols)
    pass1 +=y
for z in range(1,digits_num+1):
    z = random.choice(numbers)
    pass1 +=z
random.shuffle(pass1)

password =""
for char in pass1:
    password +=char

print(f"Here is your password : {password}")


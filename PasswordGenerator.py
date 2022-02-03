#import random
#import string
#letters=string.ascii_letters
#symbols="!#$&()*+"
#numbers="0123456789"
#a,b,c=5,2,3
#array=random.choices(letters,k=a)+random.choices(symbols,k=b)+random.choices(numbers,k=c)
#print("".join(array))
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PasswordGenerator!!")

letter_num = int(input("How many letters would you like in your password?")) 

symbols_num = int(input("How many symbols would you like in the passsword?")) 

digits_num = int(input("How many numbers would you like in the passsword?"))  

list_of_letter = []
for i in range(1,letter_num + 1 ):
    n=random.randint(1,52)
    list_of_letter.append(n)
list_of_letter_act = []
for x in list_of_letter:
    lett = letters[int(x)]
    list_of_letter_act.append(lett)
print(list_of_letter_act)


list_of_symbols = []
for i in range(1,symbols_num + 1):
    n=random.randint(1,10)
    list_of_symbols.append(n)
print(list_of_symbols)

list_of_symbols_act = []

for y in range(len(list_of_symbols)):
    symb = symbols[int(y)]
    list_of_symbols_act.append(symb)
print(list_of_symbols_act)


list_of_digits = []
for i in range(1, digits_num +1):
    n=random.randint(1,9)
    list_of_digits.append(n)
print(list_of_digits)
list_of_digits_act = []
for z in list_of_digits:
    dig = numbers[int(z)]
    list_of_digits_act.append(dig)
print(list_of_digits_act)


total1 = list_of_letter_act.extend(list_of_symbols_act).extend(list_of_digits_act)
totalpassword = random.shuffle(total1)
yoman = "".join(totalpassword)
print(f"Here is your password: {yoman}")






import random
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbols_num = int(input("How many symbols would you like in the passsword?")) 
list_of_symbols = []
for i in range(1,symbols_num + 1):
    n=random.randint(1,9)
    list_of_symbols.append(n)
print(list_of_symbols)

list_of_symbols_act = []

for y in range(len(list_of_symbols)):
    symb = list_of_symbols[int(y)]
    list_of_symbols_act.append(symb)
print(list_of_symbols_act)



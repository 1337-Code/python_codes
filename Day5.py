#fruits = ["Apple", "Pear", "Mango"]
# for fruit in fruits:
#    print(fruit)
#    print(fruit + " Jam")
#    print(fruit + "Jelly")
#    print(fruits)
#print (fruits)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(len(letters))

list_of_letter = []
for i in range(0, 6):
    n = random.randint(1, 52)
    list_of_letter.append(n)

list_of_letter_act = []
for x in list_of_letter:
    lett = letters[int(x)]
    list_of_letter_act.append(lett)
print(list_of_letter_act)

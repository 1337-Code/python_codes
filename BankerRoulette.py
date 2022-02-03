import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
n2 = len(names)
act_num = n2 - 1 
choice = random.randint(0,act_num)
victim = names[choice]
print(f"{victim} is going to buy the meal today!")
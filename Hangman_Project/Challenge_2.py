import random
words = ["police", "car", "juice", "star", "stick", "man", "pen", "zebra"]
random_word = random.choice(words)

display = []

for letter in random_word:
    display += "_"
print(display)

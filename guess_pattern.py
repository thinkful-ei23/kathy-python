import pygame
from random import randint

# list of numbers relating to CS Unit 1 patterns
dicPatt = {1: 1211, 2: 2121, 3: 2211,
           + 4: 2122, 5: 2221, 6: 1221,
           + 7: 2111, 8: 1121}

dicImage = {1: 1, 2: 2, 3: 3,
            + 4: 4, 5: 5, 6: 6,
            + 7: 7, 8: 8}


start = 1
end = 8
value = randint(start, end)

num = dicPatt[value]
pic = dicImage[value]
# button to click, 1 = quarter note, 2 = pair of eighth notes

# don't print num in the game
print(num)
print("I'm thinking of a pattern...")

guess = None

while guess != num:
    text = input("Guess the pattern: ")
    guess = int(text)

    if guess != num:
        print("Try again")


print("Congratulations! You guessed the right pattern:", dicImage[value])


# iterate over list and else
# for i in dicPatt:
#   print(i)
# else:
#   print("None left.")

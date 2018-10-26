from random import randint

# ----------------------------------VARIABLES
# list of numbers relating to CS Unit 1 patterns
dicPatt = {1: 1211, 2: 2121, 3: 2211,
           + 4: 2122, 5: 2221, 6: 1221,
           + 7: 2111, 8: 1121}
start = 1
end = 8
value = randint(start, end)
num = dicPatt[value]

# don't print num in the game
print(num)
# ----------------------------------GAME INTRO
print("You have a door in front of you, a red door.  You turn the knob and walk into the room.  There is a sign inside the room. It says...")
k = "Welcome to the RED room!"
print(k)
player_name = input("Welcome, Player. What's your name? >")
player_name.upper()
print("Hello {}, my name is Py. Do you want to play a game?".format(player_name))
input("yes or no >")
print(" Great! {} , let's play {}".format(player_name, "Read My Mind"))
print("I'm thinking of a pattern and you need to guess the pattern. It is 4 beats long with quarter notes and pairs of eighth notes. Type a 1 for a quarter note and 2 for a pair of eighth notes. Ready to read my mind? ")

guess = None

while guess != num:
    text = input("Guess the pattern: ")
    guess = int(text)

    if guess != num:
        print("Try again")

print("Congratulations! You guessed the right pattern:")
print("Do You want to play again? >")
input("yes or no >")

# input("yes or no >")
#     if (input == no):
#         print("Are you sure you want to quit?")
#         input("yes or no >")
#         if(input == no):
#                 print("Let's play!")
#             else if(input == yes):
#                 print("See you later, alligator!")

#     else (input == yes):

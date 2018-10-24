from random import randint

game = "What number am I thinking"
print(game)

player_name = input("What's your name? >")

print("Hello {}, are you ready to play?".format(player_name.upper()))
input("yes or no >")
# if yes:
#print("Which game? >")

print("Guess my number between 1 and 10")
#num = random.randrange(1, 10)
#print(num)
#
if 5 < 3:
    print("Things might be a little off...")
elif 5 == 3:
    print("Maybe we should stay inside.")
else:
    print("Yep, math works today.")

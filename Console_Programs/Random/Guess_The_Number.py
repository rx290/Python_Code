import random as r

num = int(r.randrange(0, 20))
print("Hey user i've generated a random number and you've to guess it! \nThe number lies in range from 0 - 20.")
guess = int(input("Your Guess: "))
if (((guess - num) > 0) and ((int(guess) - num) < 3)):
    print("Pretty Close bruh!")
elif ((guess - num) == 0):
    print("Damn, A champion has emerged among us!")
else:
    print("Number you're guessing is far away from my number bruh!")
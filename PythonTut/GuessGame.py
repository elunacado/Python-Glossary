secret = "navaja"
guess = ""
guesscount = 0
guessLimit = 3
outofguesses = False;

while guess != secret and not (outofguesses):
    if guesscount < guessLimit:
        guess = input("Lana sube lana baja: ")
        guesscount += 1
    else:
        outofguesses=True

if outofguesses:
    print("Loser")
else:
    print("Winner Winner Chicken Dinner")

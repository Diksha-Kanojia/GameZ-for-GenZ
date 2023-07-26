def rps():
    r=["Rock","Paper","Scissors"]

    print("ROCK!")
    print("PAPER!")
    print("SCISSORS!")
    print("SHOOT!")
    w=input("Enter your choice (Rock/Paper/Scissors)").title()
    w1=random.choice(r)
    print(w1)

    if w1=="Rock":
        if w=="Paper":
            print("You win!!")
        elif w=="Rock":
            print("It's a tie. Better luck next time :)")
        elif w=="Scissors":
            print("The Computer wins!! Better luck next time :)")
        else:
            print("I didnt understand your input please try again")

    if w1=="Paper":
        if w=="Scissors":
            print("You win!!")
        elif w=="Paper":
            print("It's a tie. Better luck next time :)")
        elif w=="Rock":
            print("The Computer wins!! Better luck next time :)")
        else:
            print("I didnt understand your input please try again")

    if w1=="Scissors":
        if w=="Rock":
            print("You win!!")
        elif w=="Scissors":
            print("It's a tie. Better luck next time :)")
        elif w=="Paper":
            print("The Computer wins!! Better luck next time :)")
        else:
            print("I didnt understand your input please try again")
            
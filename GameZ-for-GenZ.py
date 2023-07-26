import random


def hangmanavengers():
    name = random.choice(["ironman" , "thor" , "blackwidow" , "captainamerica" , "hulk" , "rocket" , "starlord" , "groot" , "antman","hawkeye","loki","spiderman","thanos"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(name) > 0:
        main = ""
        missed = 0

        for letter in name:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == name:
            print(main)
            print("we won")
            print("           _       _    _   _   _            _  _   _       _      _  ")
            print(" /\  \  / |_ |\ | |  _ |_  |_| |_       /\  |_ |_  |_ |\/| |_| |  |_  ")
            print("/  \  \/  |_ | \| |||  |_  | \  _|     /  \  _| _| |_ |  | |_| |_ |_  ")
            break
        print("guess the name" , main)
        
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("enter a valid character")
            guess = input()

        if guess not in name:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print("      _,-,_    ")
                print("     |  | |  |          ")
                print("   _ |  | |  |-,        ")
                print("  \ \|  | |  | |        ")
                print("   \           /        ")
                print("    \         /         ")
                print("     \       |          ")
                print("      |      |          ")
            if turns == 8:
                print("8 turns left")
                print("      _,-,_          ")
                print("     |  | |  |         ")
                print("   _ |  | |  |-,       ")
                print("  \ \|  | |  | |       ")
                print("   \O          /       ")
                print("    \         /        ")
                print("     \       |         ")
                print("      |      |         ")
                print("THANOS HAS FOUND THE POWER STONE")
            if turns == 7:
                print("7 turns left")
                print("      _,-,_          ")
                print("     |  | |  |         ")
                print("   _ |  | |  |-,       ")
                print("  \ \|  | |  | |       ")
                print("   \O O        /       ")
                print("    \         /        ")
                print("     \       |         ")
                print("      |      |         ")
                print("THANOS HAS FOUND THE SPACE STONE")
            if turns == 6:
                print("6 tunrs left")
                print("      _,-,_          ")
                print("     |  | |  |         ")
                print("   _ |  | |  |-,       ")
                print("  \ \|  | |  | |       ")
                print("   \O O  O     /       ")
                print("    \         /        ")
                print("     \       |         ")
                print("      |      |         ")
                print("THANOS HAS FOUND THE REALITY STONE")
            if turns == 5:
                print("5 tunrs left")
                print("      _,-,_          ")
                print("     |  | |  |         ")
                print("   _ |  | |  |-,       ")
                print("  \ \|  | |  | |       ")
                print("   \O O  O O   /       ")
                print("    \         /        ")
                print("     \       |         ")
                print("      |      |         ")
                print("THANOS HAS FOUND THE SOUL STONE")
            if turns == 4:
                print("4 tunrs left")
                print("      _,-,_          ")
                print("     |  | |  |         ")
                print("   _ |  | |  |-,       ")
                print("  \ \|  | |  | |       ")
                print("   \O O  O O O /       ")
                print("    \         /        ")
                print("     \       |         ")
                print("      |      |         ")
                print("THANOS HAS FOUND THE TIME STONE")
            if turns == 3:
                print("3 tunrs left")
                print("      _,-,_          ")
                print("     |  | |  |         ")
                print("   _ |  | |  |-,       ")
                print("  \ \|  | |  | |       ")
                print("   \O O  O O  O/       ")
                print("    \         /        ")
                print("     \   O   |         ")
                print("      |      |         ")
                print("THANOS HAS FOUND THE MIND STONE")
            if turns == 2:
                print("2 turns left")
                print("             __        ")
                print("     __     / /        ")
                print("     \ \   / /         ")
                print("      \o\ /o/_         ")
                print("      |      /\        ")
                print("      |      o/\       ")
                print("      \  o    o/\      ")
                print("       \_____o/      ")
                print(" NOW THANOS HAS ALL THE 6 STONES")
            if turns == 1:
                print("1 turn left")
                print("       \ | / __        ")
                print("     __     / /        ")
                print("     \ \   / /         ")
                print("      \o\ /o/_         ")
                print("      |      /\        ")
                print("      |      o/\       ")
                print("      \  o    o/\      ")
                print("       \_____o/      ")
                print("THANOS HAS SNAPPED")
            if turns == 0:
                print("AVENGERS WERE UNABLE TO STOP THANOS")
                print("  _____                  _   __                     __")
                print("    |   |_ |  / \  |\ | | | |_     \    /  |  |\ | |_  ")
                print("    |   |  | /   \ | \| |_|  _|     \/\/   |  | \|  __| ")
                break



#madlibs game

def madlibs1():
    a1 = input("Enter a noun:")
    a2 = input("Enter a noun:")
    a3 = input("Relative's name:")
    a4 = input("Enter a plural noun:")
    a5 = input("Enter a plural noun:")
    a6 = input("Enter a plural noun:")
    a7 = input("Enter an adverb ending in -ly:")
    a8 = input("Enter an exclamation:")
    a9= input("Enter a verb ending in -ing:")
    a10 = input("Enter an adjective:")
    a11 = input("Enter a large number:")
    a12 = input("Enter a celebrity name:")
    a13 = input("Enter an adjective:")
    a14=input("Enter a verb:")
    a15=input("Enter something slimy:")
    a16=input("Enter a noun:")
    a17 = input("Enter a plural body part:")
    a18 = input("Enter a past - tense verb:")
    print("I was going to be rich! I had just invented the first electric "+a1+". Using a(n) "+a2+" from "+a3+"’s toolbox, I built it out of old "+a4+", metal "+a5+", and rubber "+a6+". The first time I turned it on, the machine worked "+a7+". I couldn’t believe it! “"+a8+"” I yelled, "+a8+" up and down. I invited a(n) "+a9+" billionaire to check out my invention. I couldn’t wait to sell it for "+a10+" million dollars and live like "+a11+". But when I turned it on, something went terribly "+a12+". The machine started "+a13+" and began to "+a14+". Suddenly it spewed "+a15+" and shot slices of "+a16+" in all directions. The billionaire started screaming at the top of his "+a17+" and "+a18+" out of my lab. Good thing I still get my weekly allowance.")

def madlibs2():
    a1 = input("Enter a proper noun (person's name):")
    a2 = input("Enter a noun:")
    a3 = input("Enter an adjective(feeling):")
    a4 = input("Enter a verb:")
    a5 = input("Enter an adjective(feeling):")
    a6 = input("Enter an animal:")
    a7 = input("Enter a verb:")
    a8 = input("Enter a colour:")
    a9= input("Enter a verb ending in -ing:")
    a10 = input("Enter an adverb ending in -ly:")
    a11 = input("Enter a number:")
    a12 = input("Enter a measure of time:")
    a13 = input("Enter a colour:")
    a14=input("Enter a animal:")
    a15=input("Enter a number:")
    a16=input("Enter a silly word:")
    a17 = input("Enter a noun:")
    print("This weekend I am going camping with "+a1+". I packed my lantern, sleeping bag, and "+a2+". I am so "+a3+" to "+a4+" in a tent. I am "+a5+" we might see a "+a6+", they are kind of dangerous. We are going to hike, fish, and "+a7+". I have heard that the "+a8+" lake is great for "+a9+". Then we will "+a10+" hike through the forest for "+a11+" "+a12+". If I see a "+a13+" "+a14+" while hiking, I am going to bring it home as a pet! At night we will tell "+a15+" "+a16+" stories and roast "+a17+" around the campfire!!")

def madlibs3():
    a1 = input("Enter a proper noun:")
    a2 = input("Enter an adjective:")
    a3 = input("Enter a colour:")
    a4 = input("Enter an animal:")
    a5 = input("Enter a place:")
    a6 = input("Enter an adjective:")
    a7 = input("Enter a magical creature (plural):")
    a8 = input("Enter an adjective:")
    a9= input("Enter a magical creature (plural)")
    a10 = input("Enter a room in a house:")
    a11 = input("Enter a noun:")
    a12 = input("Enter a noun:")
    a13 = input("Enter a noun:")
    a14=input("Enter an adjective:")
    a15=input("Enter a plural noun:")
    a16=input("Enter a number:")
    a17 = input("Enter a measure of time:")
    a18 = input("Enter a verb ending in -ing:")
    a19=input("Enter an adjective:")
    a20=input("Enter a noun:")
    print("Dear "+a1+", \nI am writing to you from a "+a2+" castle in an enchanted forest. I found myself here one day after going for a ride on a "+a3+" "+a4+" in "+a5+". There are "+a6+" "+a7+" and "+a8+" "+a9+" here! In the "+a10+" there is a pool full of "+a11+". I fall asleep each night on a "+a12+" of "+a13+" and dream of "+a14+" "+a15+". It feels as though I have lived here for "+a16+" "+a17+". I hope one day you can visit, although the only way to get here now is "+a18+" on a "+a19+" "+a20+" !! ")


def madlibs():
    import random
    print("Welcome to MADLIBS!! Here's fun paragraph for you but first you need to fill in the following inputs~")
    while True:
        print("Answer the following but make sure you make it funny!!")
    a=[1,2,3]
    w=random.choice(a)
    if w==1:
        madlibs1()
    elif w==2:
        madlibs2()
    else:
        madlibs3()


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
            


def connect4():
    board = {
        'A1': ' ', 'B1': ' ', 'C1': ' ', 'D1': ' ', 'E1': ' ', 'F1': ' ', 'G1': ' ',
        'A2': ' ', 'B2': ' ', 'C2': ' ', 'D2': ' ', 'E2': ' ', 'F2': ' ', 'G2': ' ',
        'A3': ' ', 'B3': ' ', 'C3': ' ', 'D3': ' ', 'E3': ' ', 'F3': ' ', 'G3': ' ',
        'A4': ' ', 'B4': ' ', 'C4': ' ', 'D4': ' ', 'E4': ' ', 'F4': ' ', 'G4': ' ',
        'A5': ' ', 'B5': ' ', 'C5': ' ', 'D5': ' ', 'E5': ' ', 'F5': ' ', 'G5': ' ',
        'A6': ' ', 'B6': ' ', 'C6': ' ', 'D6': ' ', 'E6': ' ', 'F6': ' ', 'G6': ' ',
    }

    player = 1
    total_moves = 0
    end_check = 0


    # *** Game Logic ***
    def check():
    # Check all possible horizontal winning combinations for 'X

        # Checking for Row 6
        if board['A6'] == 'X' and board['B6'] == 'X' and board['C6'] == 'X' and board['D6'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B6'] == 'X' and board['C6'] == 'X' and board['D6'] == 'X' and board['E6'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1 

        if board['C6'] == 'X' and board['D6'] == 'X' and board['E6'] == 'X' and board['F6'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D6'] == 'X' and board['E6'] == 'X' and board['F6'] == 'X' and board['G6'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Row 5
        if board['A5'] == 'X' and board['B5'] == 'X' and board['C5'] == 'X' and board['D5'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B5'] == 'X' and board['C5'] == 'X' and board['D5'] == 'X' and board['E5'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1 

        if board['C5'] == 'X' and board['D5'] == 'X' and board['E5'] == 'X' and board['F5'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D5'] == 'X' and board['E5'] == 'X' and board['F5'] == 'X' and board['G5'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Row 4
        if board['A4'] == 'X' and board['B4'] == 'X' and board['C4'] == 'X' and board['D4'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B4'] == 'X' and board['C4'] == 'X' and board['D4'] == 'X' and board['E4'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1 

        if board['C4'] == 'X' and board['D4'] == 'X' and board['E4'] == 'X' and board['F4'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D4'] == 'X' and board['E4'] == 'X' and board['F4'] == 'X' and board['G4'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Row 3
        if board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'X' and board['D3'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B3'] == 'X' and board['C3'] == 'X' and board['D3'] == 'X' and board['E3'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1 

        if board['C3'] == 'X' and board['D3'] == 'X' and board['E3'] == 'X' and board['F3'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D3'] == 'X' and board['E3'] == 'X' and board['F3'] == 'X' and board['G3'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Row 2
        if board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'X' and board['D2'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B2'] == 'X' and board['C2'] == 'X' and board['D2'] == 'X' and board['E2'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1 

        if board['C2'] == 'X' and board['D2'] == 'X' and board['E2'] == 'X' and board['F2'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D2'] == 'X' and board['E2'] == 'X' and board['F2'] == 'X' and board['G2'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Row 1
        if board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'X' and board['D1'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B1'] == 'X' and board['C1'] == 'X' and board['D1'] == 'X' and board['E1'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1 

        if board['C1'] == 'X' and board['D1'] == 'X' and board['E1'] == 'X' and board['F1'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D1'] == 'X' and board['E1'] == 'X' and board['F1'] == 'X' and board['G1'] == 'X': 
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

    # Check all possible vertical winning combinations for 'X'
        # Checking for Column A 
        if board['A6'] == 'X' and board['A5'] == 'X' and board['A4'] == 'X' and board['A3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['A5'] == 'X' and board['A4'] == 'X' and board['A3'] == 'X' and board['A2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['A4'] == 'X' and board['A3'] == 'X' and board['A2'] == 'X' and board['A1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Column B
        if board['B6'] == 'X' and board['B5'] == 'X' and board['B4'] == 'X' and board['B3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B5'] == 'X' and board['B4'] == 'X' and board['B3'] == 'X' and board['B2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B4'] == 'X' and board['B3'] == 'X' and board['B2'] == 'X' and board['B1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Column C
        if board['C6'] == 'X' and board['C5'] == 'X' and board['C4'] == 'X' and board['C3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C5'] == 'X' and board['C4'] == 'X' and board['C3'] == 'X' and board['C2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C4'] == 'X' and board['C3'] == 'X' and board['C2'] == 'X' and board['C1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Column D
        if board['D6'] == 'X' and board['D5'] == 'X' and board['D4'] == 'X' and board['D3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D5'] == 'X' and board['D4'] == 'X' and board['D3'] == 'X' and board['D2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D4'] == 'X' and board['D3'] == 'X' and board['D2'] == 'X' and board['D1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Column E
        if board['E6'] == 'X' and board['E5'] == 'X' and board['E4'] == 'X' and board['E3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['E5'] == 'X' and board['E4'] == 'X' and board['E3'] == 'X' and board['E2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['E4'] == 'X' and board['E3'] == 'X' and board['E2'] == 'X' and board['E1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Column F
        if board['F6'] == 'X' and board['F5'] == 'X' and board['F4'] == 'X' and board['F3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['F5'] == 'X' and board['F4'] == 'X' and board['F3'] == 'X' and board['F2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['F4'] == 'X' and board['F3'] == 'X' and board['F2'] == 'X' and board['F1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        # Checking for Column G
        if board['G6'] == 'X' and board['G5'] == 'X' and board['G4'] == 'X' and board['G3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['G5'] == 'X' and board['G4'] == 'X' and board['G3'] == 'X' and board['G2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['G4'] == 'X' and board['G3'] == 'X' and board['G2'] == 'X' and board['G1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

    # Check for all diagonal winning combinations for 'X'
        #/*
        if board['A6'] == 'X' and board['B5'] == 'X' and board['C4'] == 'X' and board['D3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B6'] == 'X' and board['C5'] == 'X' and board['D4'] == 'X' and board['E3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C6'] == 'X' and board['D5'] == 'X' and board['E4'] == 'X' and board['F3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D6'] == 'X' and board['E5'] == 'X' and board['F4'] == 'X' and board['G3'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        #/**
        if board['A5'] == 'X' and board['B4'] == 'X' and board['C3'] == 'X' and board['D2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B5'] == 'X' and board['C4'] == 'X' and board['D3'] == 'X' and board['E2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C5'] == 'X' and board['D4'] == 'X' and board['E3'] == 'X' and board['F2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D5'] == 'X' and board['E4'] == 'X' and board['F3'] == 'X' and board['G2'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        #/***
        if board['A4'] == 'X' and board['B3'] == 'X' and board['C2'] == 'X' and board['D1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B4'] == 'X' and board['C3'] == 'X' and board['D2'] == 'X' and board['E1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C4'] == 'X' and board['D3'] == 'X' and board['E2'] == 'X' and board['F1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D4'] == 'X' and board['E3'] == 'X' and board['F2'] == 'X' and board['G1'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        #\*
        if board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'X' and board['D4'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B1'] == 'X' and board['C2'] == 'X' and board['D3'] == 'X' and board['E4'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C1'] == 'X' and board['D2'] == 'X' and board['E3'] == 'X' and board['F4'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D1'] == 'X' and board['E2'] == 'X' and board['F3'] == 'X' and board['G4'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        #\**
        if board['A2'] == 'X' and board['B3'] == 'X' and board['C4'] == 'X' and board['D5'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B2'] == 'X' and board['C3'] == 'X' and board['D4'] == 'X' and board['E5'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C2'] == 'X' and board['D3'] == 'X' and board['E4'] == 'X' and board['F5'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D2'] == 'X' and board['E3'] == 'X' and board['F4'] == 'X' and board['G5'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        #\***
        if board['A3'] == 'X' and board['B4'] == 'X' and board['C5'] == 'X' and board['D6'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['B3'] == 'X' and board['C4'] == 'X' and board['D5'] == 'X' and board['E6'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['C3'] == 'X' and board['D4'] == 'X' and board['E5'] == 'X' and board['F6'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

        if board['D3'] == 'X' and board['E4'] == 'X' and board['F5'] == 'X' and board['G6'] == 'X':
            print("FOUR IN A ROW PLAYER ONE ROW!")
            return 1

    # Check all possible horizontal winning combinations for 'O'
        # Checking for Row 6

        if board['A6'] == 'O' and board['B6'] == 'O' and board['C6'] == 'O' and board['D6'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B6'] == 'O' and board['C6'] == 'O' and board['D6'] == 'O' and board['E6'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1 

        if board['C6'] == 'O' and board['D6'] == 'O' and board['E6'] == 'O' and board['F6'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D6'] == 'O' and board['E6'] == 'O' and board['F6'] == 'O' and board['G6'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Row 5
        if board['A5'] == 'O' and board['B5'] == 'O' and board['C5'] == 'O' and board['D5'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B5'] == 'O' and board['C5'] == 'O' and board['D5'] == 'O' and board['E5'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1 

        if board['C5'] == 'O' and board['D5'] == 'O' and board['E5'] == 'O' and board['F5'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D5'] == 'O' and board['E5'] == 'O' and board['F5'] == 'O' and board['G5'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Row 4
        if board['A4'] == 'O' and board['B4'] == 'O' and board['C4'] == 'O' and board['D4'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B4'] == 'O' and board['C4'] == 'O' and board['D4'] == 'O' and board['E4'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1 

        if board['C4'] == 'O' and board['D4'] == 'O' and board['E4'] == 'O' and board['F4'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D4'] == 'O' and board['E4'] == 'O' and board['F4'] == 'O' and board['G4'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Row 3
        if board['A3'] == 'O' and board['B3'] == 'O' and board['C3'] == 'O' and board['D3'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B3'] == 'O' and board['C3'] == 'O' and board['D3'] == 'O' and board['E3'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1 

        if board['C3'] == 'O' and board['D3'] == 'O' and board['E3'] == 'O' and board['F3'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D3'] == 'O' and board['E3'] == 'O' and board['F3'] == 'O' and board['G3'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Row 2
        if board['A2'] == 'O' and board['B2'] == 'O' and board['C2'] == 'O' and board['D2'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B2'] == 'O' and board['C2'] == 'O' and board['D2'] == 'O' and board['E2'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1 

        if board['C2'] == 'O' and board['D2'] == 'O' and board['E2'] == 'O' and board['F2'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D2'] == 'O' and board['E2'] == 'O' and board['F2'] == 'O' and board['G2'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Row 1
        if board['A1'] == 'O' and board['B1'] == 'O' and board['C1'] == 'O' and board['D1'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B1'] == 'O' and board['C1'] == 'O' and board['D1'] == 'O' and board['E1'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1 

        if board['C1'] == 'O' and board['D1'] == 'O' and board['E1'] == 'O' and board['F1'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D1'] == 'O' and board['E1'] == 'O' and board['F1'] == 'O' and board['G1'] == 'O': 
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

    # Check all possible vertical winning combinations for 'O'
        # Checking for Column A 
        if board['A6'] == 'O' and board['A5'] == 'O' and board['A4'] == 'O' and board['A3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['A5'] == 'O' and board['A4'] == 'O' and board['A3'] == 'O' and board['A2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['A4'] == 'O' and board['A3'] == 'O' and board['A2'] == 'O' and board['A1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Column B
        if board['B6'] == 'O' and board['B5'] == 'O' and board['B4'] == 'O' and board['B3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B5'] == 'O' and board['B4'] == 'O' and board['B3'] == 'O' and board['B2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B4'] == 'O' and board['B3'] == 'O' and board['B2'] == 'O' and board['B1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Column C
        if board['C6'] == 'O' and board['C5'] == 'O' and board['C4'] == 'O' and board['C3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C5'] == 'O' and board['C4'] == 'O' and board['C3'] == 'O' and board['C2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C4'] == 'O' and board['C3'] == 'O' and board['C2'] == 'O' and board['C1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Column D
        if board['D6'] == 'O' and board['D5'] == 'O' and board['D4'] == 'O' and board['D3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D5'] == 'O' and board['D4'] == 'O' and board['D3'] == 'O' and board['D2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D4'] == 'O' and board['D3'] == 'O' and board['D2'] == 'O' and board['D1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Column E
        if board['E6'] == 'O' and board['E5'] == 'O' and board['E4'] == 'O' and board['E3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['E5'] == 'O' and board['E4'] == 'O' and board['E3'] == 'O' and board['E2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['E4'] == 'O' and board['E3'] == 'O' and board['E2'] == 'O' and board['E1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Column F
        if board['F6'] == 'O' and board['F5'] == 'O' and board['F4'] == 'O' and board['F3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['F5'] == 'O' and board['F4'] == 'O' and board['F3'] == 'O' and board['F2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['F4'] == 'O' and board['F3'] == 'O' and board['F2'] == 'O' and board['F1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        # Checking for Column G
        if board['G6'] == 'O' and board['G5'] == 'O' and board['G4'] == 'O' and board['G3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['G5'] == 'O' and board['G4'] == 'O' and board['G3'] == 'O' and board['G2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['G4'] == 'O' and board['G3'] == 'O' and board['G2'] == 'O' and board['G1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

    # Check for all diagonal winning combinations for 'O'
        #/*
        if board['A6'] == 'O' and board['B5'] == 'O' and board['C4'] == 'O' and board['D3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B6'] == 'O' and board['C5'] == 'O' and board['D4'] == 'O' and board['E3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C6'] == 'O' and board['D5'] == 'O' and board['E4'] == 'O' and board['F3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D6'] == 'O' and board['E5'] == 'O' and board['F4'] == 'O' and board['G3'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        #/**
        if board['A5'] == 'O' and board['B4'] == 'O' and board['C3'] == 'O' and board['D2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B5'] == 'O' and board['C4'] == 'O' and board['D3'] == 'O' and board['E2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C5'] == 'O' and board['D4'] == 'O' and board['E3'] == 'O' and board['F2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D5'] == 'O' and board['E4'] == 'O' and board['F3'] == 'O' and board['G2'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        #/***
        if board['A4'] == 'O' and board['B3'] == 'O' and board['C2'] == 'O' and board['D1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B4'] == 'O' and board['C3'] == 'O' and board['D2'] == 'O' and board['E1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C4'] == 'O' and board['D3'] == 'O' and board['E2'] == 'O' and board['F1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D4'] == 'O' and board['E3'] == 'O' and board['F2'] == 'O' and board['G1'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        #\*
        if board['A1'] == 'O' and board['B2'] == 'O' and board['C3'] == 'O' and board['D4'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B1'] == 'O' and board['C2'] == 'O' and board['D3'] == 'O' and board['E4'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C1'] == 'O' and board['D2'] == 'O' and board['E3'] == 'O' and board['F4'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D1'] == 'O' and board['E2'] == 'O' and board['F3'] == 'O' and board['G4'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        #\**
        if board['A2'] == 'O' and board['B3'] == 'O' and board['C4'] == 'O' and board['D5'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B2'] == 'O' and board['C3'] == 'O' and board['D4'] == 'O' and board['E5'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C2'] == 'O' and board['D3'] == 'O' and board['E4'] == 'O' and board['F5'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D2'] == 'O' and board['E3'] == 'O' and board['F4'] == 'O' and board['G5'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        #\***
        if board['A3'] == 'O' and board['B4'] == 'O' and board['C5'] == 'O' and board['D6'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['B3'] == 'O' and board['C4'] == 'O' and board['D5'] == 'O' and board['E6'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['C3'] == 'O' and board['D4'] == 'O' and board['E5'] == 'O' and board['F6'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1

        if board['D3'] == 'O' and board['E4'] == 'O' and board['F5'] == 'O' and board['G6'] == 'O':
            print("FOUR IN A ROW PLAYER TWO ROW!")
            return 1
        return 0




    # Show possible player inputs

    print('A'+' | '+'B'+' | '+'C'+' | '+'D'+' | '+'E'+' | '+'F'+' | '+'G')
    print('--+---+---+---+---+---+--')
    print(' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' ')
    print('--+---+---+---+---+---+--')
    print(' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' ')
    print('--+---+---+---+---+---+--')
    print(' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' ')
    print('--+---+---+---+---+---+--')
    print(' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' ')
    print('--+---+---+---+---+---+--')
    print(' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' ')
    print('--+---+---+---+---+---+--')
    print(' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' '+' | '+' ')
    print('--+---+---+---+---+---+--')
    print('*********************************************************')


    #Player inputs (adding pieces)
    while True:
        print('A'+' | '+'B'+' | '+'C'+' | '+'D'+' | '+'E'+' | '+'F'+' | '+'G')
        print('--+---+---+---+---+---+--')
        print(board['A1']+' | '+board['B1']+' | '+board['C1']+' | '+board['D1']+' | '+board['E1']+' | '+board['F1']+' | '+board['G1'])
        print('--+---+---+---+---+---+--')
        print(board['A2']+' | '+board['B2']+' | '+board['C2']+' | '+board['D2']+' | '+board['E2']+' | '+board['F2']+' | '+board['G2'])
        print('--+---+---+---+---+---+--')
        print(board['A3']+' | '+board['B3']+' | '+board['C3']+' | '+board['D3']+' | '+board['E3']+' | '+board['F3']+' | '+board['G3'])
        print('--+---+---+---+---+---+--')
        print(board['A4']+' | '+board['B4']+' | '+board['C4']+' | '+board['D4']+' | '+board['E4']+' | '+board['F4']+' | '+board['G4'])
        print('--+---+---+---+---+---+--')
        print(board['A5']+' | '+board['B5']+' | '+board['C5']+' | '+board['D5']+' | '+board['E5']+' | '+board['F5']+' | '+board['G5'])
        print('--+---+---+---+---+---+--')
        print(board['A6']+' | '+board['B6']+' | '+board['C6']+' | '+board['D6']+' | '+board['E6']+' | '+board['F6']+' | '+board['G6'])
        print('--+---+---+---+---+---+--')
        end_check = check() # store the returned value in end_check
        if total_moves == 42:
            print("Game Over! Tie!")
            break
        elif end_check == 1:
            print("Game Over!")
            break


        while True:
            if player == 1:
                p1_input = input("Player One: ")
                if p1_input.upper() == 'A':
                    if board['A6'] == ' ':
                        board['A6'] = 'X'
                        player =2
                        break
                    if board['A6'] != ' ' and board['A5'] == ' ':
                        board['A5'] = 'X'
                        player = 2
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] == ' ':
                        board['A4'] = 'X'
                        player = 2
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] != ' ' and board['A3'] == ' ':
                        board['A3'] = 'X'
                        player = 2
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] != ' ' and board['A3'] != ' ' and board['A2'] == ' ':
                        board['A2'] = 'X'
                        player = 2
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] != ' ' and board['A3'] != ' ' and board['A2'] != ' ' and board['A1'] == ' ':
                        board['A1'] = 'X'
                        player = 2
                        break

                elif p1_input.upper() == 'B':
                    if board['B6'] == ' ':
                        board['B6'] = 'X'
                        player =2
                        break
                    if board['B6'] != ' ' and board['B5'] == ' ':
                        board['B5'] = 'X'
                        player = 2
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] == ' ':
                        board['B4'] = 'X'
                        player = 2
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] != ' ' and board['B3'] == ' ':
                        board['B3'] = 'X'
                        player = 2
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] != ' ' and board['B3'] != ' ' and board['B2'] == ' ':
                        board['B2'] = 'X'
                        player = 2
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] != ' ' and board['B3'] != ' ' and board['B2'] != ' ' and board['B1'] == ' ':
                        board['B1'] = 'X'
                        player = 2
                        break

                elif p1_input.upper() == 'C':
                    if board['C6'] == ' ':
                        board['C6'] = 'X'
                        player =2
                        break
                    if board['C6'] != ' ' and board['C5'] == ' ':
                        board['C5'] = 'X'
                        player = 2
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] == ' ':
                        board['C4'] = 'X'
                        player = 2
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] != ' ' and board['C3'] == ' ':
                        board['C3'] = 'X'
                        player = 2
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] != ' ' and board['C3'] != ' ' and board['C2'] == ' ':
                        board['C2'] = 'X'
                        player = 2
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] != ' ' and board['C3'] != ' ' and board['C2'] != ' ' and board['C1'] == ' ':
                        board['C1'] = 'X'
                        player = 2
                        break

                elif p1_input.upper() == 'D':
                    if board['D6'] == ' ':
                        board['D6'] = 'X'
                        player =2 
                        break
                    if board['D6'] != ' ' and board['D5'] == ' ':
                        board['D5'] = 'X'
                        player = 2
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] == ' ':
                        board['D4'] = 'X'
                        player = 2
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] != ' ' and board['D3'] == ' ':
                        board['D3'] = 'X'
                        player = 2
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] != ' ' and board['D3'] != ' ' and board['D2'] == ' ':
                        board['D2'] = 'X'
                        player = 2
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] != ' ' and board['D3'] != ' ' and board['D2'] != ' ' and board['D1'] == ' ':
                        board['D1'] = 'X'
                        player = 2
                        break

                elif p1_input.upper() == 'E':
                    if board['E6'] == ' ':
                        board['E6'] = 'X'
                        player =2 
                        break
                    if board['E6'] != ' ' and board['E5'] == ' ':
                        board['E5'] = 'X'
                        player = 2
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] == ' ':
                        board['E4'] = 'X'
                        player = 2
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] != ' ' and board['E3'] == ' ':
                        board['E3'] = 'X'
                        player = 2
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] != ' ' and board['E3'] != ' ' and board['E2'] == ' ':
                        board['E2'] = 'X'
                        player = 2
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] != ' ' and board['E3'] != ' ' and board['E2'] != ' ' and board['E1'] == ' ':
                        board['E1'] = 'X'
                        player = 2
                        break

                elif p1_input.upper() == 'F':
                    if board['F6'] == ' ':
                        board['F6'] = 'X'
                        player =2
                        break
                    if board['F6'] != ' ' and board['F5'] == ' ':
                        board['F5'] = 'X'
                        player = 2
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] == ' ':
                        board['F4'] = 'X'
                        player = 2
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] != ' ' and board['F3'] == ' ':
                        board['F3'] = 'X'
                        player = 2
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] != ' ' and board['F3'] != ' ' and board['F2'] == ' ':
                        board['F2'] = 'X'
                        player = 2
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] != ' ' and board['F3'] != ' ' and board['F2'] != ' ' and board['F1'] == ' ':
                        board['F1'] = 'X'
                        player = 2
                        break

                elif p1_input.upper() == 'G':
                    if board['G6'] == ' ':
                        board['G6'] = 'X'
                        player =2
                        break
                    if board['G6'] != ' ' and board['G5'] == ' ':
                        board['G5'] = 'X'
                        player = 2
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] == ' ':
                        board['G4'] = 'X'
                        player = 2
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] != ' ' and board['G3'] == ' ':
                        board['G3'] = 'X'
                        player = 2
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] != ' ' and board['G3'] != ' ' and board['G2'] == ' ':
                        board['G2'] = 'X'
                        player = 2
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] != ' ' and board['G3'] != ' ' and board['G2'] != ' ' and board['G1'] == ' ':
                        board['G1'] = 'X'
                        player = 2
                        break

                else:
                    print("Invalid Input! Please Try Again!")
                    continue

            else:
                p2_input = input("Player Two: ")
                if p2_input.upper() == 'A':
                    if board['A6'] == ' ':
                            board['A6'] = 'O'
                            player =1
                            break
                    if board['A6'] != ' ' and board['A5'] == ' ':
                        board['A5'] = 'O'
                        player = 1
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] == ' ':
                        board['A4'] = 'O'
                        player = 1
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] != ' ' and board['A3'] == ' ':
                        board['A3'] = 'O'
                        player = 1
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] != ' ' and board['A3'] != ' ' and board['A2'] == ' ':
                        board['A2'] = 'O'
                        player = 1
                        break
                    if board['A6'] != ' ' and board['A5'] != ' ' and board['A4'] != ' ' and board['A3'] != ' ' and board['A2'] != ' ' and board['A1'] == ' ':
                        board['A1'] = 'O'
                        player = 1
                        break

                elif p2_input.upper() == 'B':
                    if board['B6'] == ' ':
                        board['B6'] = 'O'
                        player =1
                        break
                    if board['B6'] != ' ' and board['B5'] == ' ':
                        board['B5'] = 'O'
                        player = 1
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] == ' ':
                        board['B4'] = 'O'
                        player = 1
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] != ' ' and board['B3'] == ' ':
                        board['B3'] = 'O'
                        player = 1
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] != ' ' and board['B3'] != ' ' and board['B2'] == ' ':
                        board['B2'] = 'O'
                        player = 1
                        break
                    if board['B6'] != ' ' and board['B5'] != ' ' and board['B4'] != ' ' and board['B3'] != ' ' and board['B2'] != ' ' and board['B1'] == ' ':
                        board['B1'] = 'O'
                        player = 1
                        break

                elif p2_input.upper() == 'C':
                    if board['C6'] == ' ':
                        board['C6'] = 'O'
                        player = 1 
                        break
                    if board['C6'] != ' ' and board['C5'] == ' ':
                        board['C5'] = 'O'
                        player = 1
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] == ' ':
                        board['C4'] = 'O'
                        player = 1
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] != ' ' and board['C3'] == ' ':
                        board['C3'] = 'O'
                        player = 1
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] != ' ' and board['C3'] != ' ' and board['C2'] == ' ':
                        board['C2'] = 'O'
                        player = 1
                        break
                    if board['C6'] != ' ' and board['C5'] != ' ' and board['C4'] != ' ' and board['C3'] != ' ' and board['C2'] != ' ' and board['C1'] == ' ':
                        board['C1'] = 'O'
                        player = 1
                        break

                elif p2_input.upper() == 'D':
                    if board['D6'] == ' ':
                        board['D6'] = 'O'
                        player =1 
                        break
                    if board['D6'] != ' ' and board['D5'] == ' ':
                        board['D5'] = 'O'
                        player = 1
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] == ' ':
                        board['D4'] = 'O'
                        player = 1
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] != ' ' and board['D3'] == ' ':
                        board['D3'] = 'O'
                        player = 1
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] != ' ' and board['D3'] != ' ' and board['D2'] == ' ':
                        board['D2'] = 'O'
                        player = 1
                        break
                    if board['D6'] != ' ' and board['D5'] != ' ' and board['D4'] != ' ' and board['D3'] != ' ' and board['D2'] != ' ' and board['D1'] == ' ':
                        board['D1'] = 'O'
                        player = 1
                        break

                elif p2_input.upper() == 'E':
                    if board['E6'] == ' ':
                        board['E6'] = 'O'
                        player = 1 
                        break
                    if board['E6'] != ' ' and board['E5'] == ' ':
                        board['E5'] = 'O'
                        player = 1
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] == ' ':
                        board['E4'] = 'O'
                        player = 1
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] != ' ' and board['E3'] == ' ':
                        board['E3'] = 'O'
                        player = 1
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] != ' ' and board['E3'] != ' ' and board['E2'] == ' ':
                        board['E2'] = 'O'
                        player = 1
                        break
                    if board['E6'] != ' ' and board['E5'] != ' ' and board['E4'] != ' ' and board['E3'] != ' ' and board['E2'] != ' ' and board['E1'] == ' ':
                        board['E1'] = 'O'
                        player = 1
                        break

                elif p2_input.upper() == 'F':
                    if board['F6'] == ' ':
                        board['F6'] = 'O'
                        player = 1 
                        break
                    if board['F6'] != ' ' and board['F5'] == ' ':
                        board['F5'] = 'O'
                        player = 1
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] == ' ':
                        board['F4'] = 'O'
                        player = 1
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] != ' ' and board['F3'] == ' ':
                        board['F3'] = 'O'
                        player = 1
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] != ' ' and board['F3'] != ' ' and board['F2'] == ' ':
                        board['F2'] = 'O'
                        player = 1
                        break
                    if board['F6'] != ' ' and board['F5'] != ' ' and board['F4'] != ' ' and board['F3'] != ' ' and board['F2'] != ' ' and board['F1'] == ' ':
                        board['F1'] = 'O'
                        player = 1
                        break

                elif p2_input.upper() == 'G':
                    if board['G6'] == ' ':
                        board['G6'] = 'O'
                        player = 1 
                        break
                    if board['G6'] != ' ' and board['G5'] == ' ':
                        board['G5'] = 'O'
                        player = 1
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] == ' ':
                        board['G4'] = 'O'
                        player = 1
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] != ' ' and board['G3'] == ' ':
                        board['G3'] = 'O'
                        player = 1
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] != ' ' and board['G3'] != ' ' and board['G2'] == ' ':
                        board['G2'] = 'O'
                        player = 1
                        break
                    if board['G6'] != ' ' and board['G5'] != ' ' and board['G4'] != ' ' and board['G3'] != ' ' and board['G2'] != ' ' and board['G1'] == ' ':
                        board['G1'] = 'O'
                        player = 1
                        break

                else:
                    print("Invalid Input! Please Try Again!")
                    continue

        total_moves += 1
        print('*********************************************************')
        print()


print("HELLO HELLO HELLO!!!")
print("Welcome to GameZ for GenZ")
print("You look like you're in the mood to play some games today. We have a few options for you.")
while True:
    print("Choose from the following options \n1. Connect4 \n2. Rock-Paper-Scissors \n3. Mad Libs \n4. Avenger's hangman ")
    q=int(input("Enter the option no. of the game you want to play: "))
    if q==1:
        connect4()
    elif q==2:
        rps()
    elif q==3:
        madlibs()
    elif q==4:
        hangmanavengers()
    else:
        print("Invalid input. Please try again")
    e=input("Do you want to exit from the whole game? (Type y or n): ").lower()
    if e in "no":
        print("You were an amazing player. We will miss playing with u. BYE!")
        break
    else:
        continue

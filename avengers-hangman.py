import random


def avengers():
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
user = input("Enter your name")
print("WELCOME" , user)
print("*****")
print("try to guess the word in less than 10 tries by guessing single letter at a time ")
avengers()
print("thanks for playing")
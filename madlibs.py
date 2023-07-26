
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

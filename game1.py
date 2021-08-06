# PYTHON 3.9.5
#
#
# Author: Raleigh Johnson
#
#
#Purpose: To create a text based game that can be played.
import time


def start(nice=0,mean=0,name=""):
    # Get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    """
    Check if this is a new gamr or not.
    if it is new, get the user's name.
    if it is not, thank the player for playing again.
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome {}".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name) :
    stop = True
    while stop:
         show_score(nice,mean,name)
         pick = input("\nA stranger approaches you for a \nconversation. Will you be nice\nor mean?(N/M) \n>>>: ").lower()
         if pick  == "n":
             print("\nThe stranger walks away smiling...\n+Karma")
             nice =(nice + 1)
             stop = False
         if pick == "m":
             print("\nThe stranger glares at you \nmenacingly and storms off...\n-Karma")
             mean = (mean + 1)
             stop = False
    score(nice,mean,name)
        # pass the 3 variable to the score()
             
def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    #score function is being passed the values stored in the 3 variables
    if nice > 2: # if condition is valid, calls for win condition
        win(nice,mean,name)
    if mean > 2: #if condition is valid, calls for loss condition
        lose(nice,mean,name)
    else: #else, call nice_mena function in the variables so it can use them.
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #Substitute the {} wildcards with our variable values
    print("\nNice job {}! You win! \nEveryone loves you and you've \nmade lots of friends along the way.".format(name))
    # call again and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    #Substitute the {} wildcards with our variable values
    print("\nOh no {}! No one likes you! \nEveryone hates you and you've \nmade lots of enemies in your time.\nNow you live in a crappy apartment filled with bugs.".format(name))
    # call again and pass in our variables
    again(nice,mean,name)


def again (nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice  == "n":
            print("\nOh, Thank you for playing!")
            time.sleep(5) #Delay 5s for user to read message before closing.
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', and ( N ) for 'No':\n>>> ") 

def reset (nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)

if __name__ == "__main__":
    start()

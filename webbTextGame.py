#!/usr/bin/python3
import time
from os import system

responses1 = ["Open the curtains","open the curtains","Open curtains","open curtains"]
responses2 = ["leave room","Leave room", "Leave the room","leave the room"]
responses3 = ["Gopher","gopher","[gopher]"]

def welcome():
    print("Welcome to" , game , "!")
    print("Portions of the code were adapted from another project, worked on in conjunction with James Tomasino.\n\nhttps://github.com/brendantcc/PyChat/\n ")
def bug():
    print("so uhh there's a little bit of a bug... you can see it with the",game,"thing. heh.")
    print("So yeah... weird bug...")



def start():
    print("You start in an empty, dark room. What do you do? [open curtains]")

time.sleep(4)
game = str("Untitled Python Game")
print(game , "by Brendan Webb, for Project Time.")
print("Project started on the 2nd of May, 2019.")
# time.sleep(10)
# this above code was implemented to test the opening code
time.sleep(5)
system("clear||cls")
welcome()
bug()
start()
r1 = input()
if r1.lower() in responses1:
    print("You open the curtains to find that you're in space, aboard your friend James' spaceship, \nthe Melchizedek. What do you do? [leave room]")
    r2 = input()
    if r2.lower in responses2:       
        print("You go up to the bridge to greet James and have a conversation. What do you talk about? [gopher]")
        r3 = input()
        if r3.lower() in responses3:
            print("You and James discuss gopher, and somehow his radio show, 'Choose Your Own Adventure' comes up.")
            system("clear||cls")
            print("Thanks for playing",game," demo! This is yet to actually be named \n and i found it hard to come up with any more answers. \n Again, thanks for playing! :)")
        else:
                    print("invalid answer. restart game and try again.")

else:
    print("Sorry, that isn't a valid answer.")
    print("Please restart the game and try again.")



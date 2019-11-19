#!/usr/bin/python3
from time import sleep
from os import system

responses1 = ["open the curtains","open curtains"]
responses2 = ["leave room","leave the room"]
responses3 = ["gopher"]

def welcome():
    print("Welcome to" , game + "!")
    print("Portions of the code were adapted from another project, worked on in conjunction with James Tomasino.\n\nhttps://github.com/brendantcc/PyChat/\n ")



def start():
    print("You start in an empty, dark room. What do you do? valid answers:", responses1 , )

sleep(4)
game = str("Untitled Python Game")
print(game , "by Brendan Webb")
print("Project started on the 2nd of May, 2019.")
# sleep(10)
# this above code was implemented to test the opening code
sleep(5)
system("clear||cls")
welcome()
start()
r1 = input()
if r1.lower() in responses1:
    print("You open the curtains to find that you're in space, aboard your friend James' spaceship, \nthe Melchizedek. What do you do? valid answers:" , responses2 , )
    r2 = input()
    if r2.lower() in responses2:       
        print("You go up to the bridge to greet James and have a conversation. What do you talk about? valid answers:" , responses3 , )
        r3 = input()
        if r3.lower() in responses3:
            print("You and James discuss gopher, and somehow his radio show, 'Choose Your Own Adventure' comes up.\n(oh hey how ironic this is probably being read out on there right now! HEY INTERNET! -brendantcc)")
            print("press enter to continue..")
            input()
            system("clear||cls")
            print("Thanks for playing the demo for",game+"! This is yet to actually be named \nand i found it hard to come up with any more answers. \nAgain, thanks for playing! :)")
        else:
                    print("invalid answer. restart game and try again.")

else:
    print("Sorry, that isn't a valid answer.")
    print("Please restart the game and try again.")



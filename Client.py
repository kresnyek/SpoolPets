# SpoolPet Client
# This is the client side of the game, which allows the user to interact with the pet that
# is hosted on the server.
# v0.2
# Updated: 6/21/16
# By: kresnyek
# Created: 6/20/16
import socket
import os
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 8888)
print("trying to connect to port 8888")
s.connect(serverAddress)
print("connected")
       
try:
    print("received: " + s.recv(1024).decode("utf-8") )
            
except socket.error as msg:
    print("Oh noes. Failed: " + str(msg[0]) + '\n' + str(msg[1]))

#This functions cleans the input to be all caps,
# and returns a list of all the elements to look at.

def parseInput(uInput):
    playWith = uInput.upper()
    return playWith.split()

#intro dialogue piece
def introDialogue():
    os.system("cls")
    print("Oh, hi")
    time.sleep(1)
    print("I'm Molly... I run this shop.")
    time.sleep(1)
    print("umm... would you like to adopt a pet? They are quite lovely, and great listeners")
    time.sleep(2)
    print("I have a blue one that's a real sweetheart back there...")
    userInput = parseInput((input("[0] - I'd love to have them\n[1] - I'm good, thanks though\n")).strip())[0]

    if(userInput == "0"):
        print("Great! I'll pack them up for you now")
        print("*A strange creature was placed in your inventory*")
        
    elif(userInput == "1"):
        print("Are you sure? They'll have nowhere to go then... Just take them, free of charge!")
        print("*Molly swiftly placed a strange parcle in your bag*")
        print("I'm sure you'll love them")
    else:
        print("Well... I'm not really sure what you mean... but I'll go get them for you")
        print("*A strange creature was placed in your inventory*")

#This is the Play menu printer
def playMenu():
    os.system("cls")
    print("What would you like to do today?\n")
    print("[Pet] - Interact with Pet")
    print("[Shop] - Go to the Store")
    print("[Show] - Participate in show\n")
    print("[Quit] - Quit the game")

#Prints info about your pet   
def petAbout():
    msg = "ABOUT"
    s.send(msg.encode('UTF-8', 'strict'))
    print("About your Pet")
    

#use this function to send a request to feed your pet
def petFeed():
    print("Feed your Pet")

#use this function to send a play request
def petPlay():
    print("Play with Pet")

#use this function to send a walk request
def petWalk():
    print("Walk your pet")

#use this function to send a cuddle request
def petCuddle():
    print("Cuddle your odd pet")

#use this to access the shop
def shop():
    print("The Shop")

#use this to access the pet show
def show():
    print("The Show")
        

#This is the actual game interface. It runs much like run()
def play():
    introDialogue()
    time.sleep(4)
    running = True
    while running:
        playMenu()
        userInput = parseInput(input(">>"))
        if(userInput[0] == "PET"):
            if(len(userInput) < 2):
                #What actions the user can actually do in this area
                print("To Interact with your pet, please specify which actions. Example: \"Pet Feed\"")
                print("Possible Actions: About, Feed, Play, Walk, and Cuddle")
            elif(userInput[1] == "ABOUT"):
                petAbout()
            elif(userInput[1] == "FEED"):
                petFeed()
            elif(userInput[1] == "PLAY"):
                petPlay()
            elif(UuserInput[1] == "WALK"):
                petWalk()
            elif(UuserInput[1] == "CUDDLE"):
                petCuddle()
            else:
                print("I'm sorry, you can't do that with your pet.")
                
                
        elif(userInput[0] == "SHOP"):
            shop()
        elif(userInput[0] == "SHOW"):
            show()
        elif(userInput[0] == "QUIT"):
            msg = "QUIT"
            if(len(userInput)>1 and userInput[1] == "ALL"):
                msg = "QUIT ALL"
            #First, kill the connection
            s.send(msg.encode('UTF-8', 'strict'))
            #Then kill this loop
            running = False
        else:
            print("I'm Sorry, I don't know what you mean. Please try Again")
        
#This is a function about the game
def about():
    os.system("cls")
    print("About the Game")
    print("Blah blah stuff about the game")
    input("Press any key to continue")

def gameHelp():
    os.system("cls")
    print("Game Help")
    print("This sections hosts all the info you need to get throug this game")
    input("Press any key to continue")
    

#Prints main menu text
def mainMenu():
    
    print("SpoolPets: Threading Fluffy Friends")
    print("Main Menu")
    print("\nWhat would you like to do today?")
    print("[0] - Play Game")
    print("[1] - About Game")
    print("[2] - Help")
    print("[3] - Quit")

def run():
    running = True
    while running:
        mainMenu()
        userInput = parseInput(input(">> "))[0]
        if(userInput == "0"):
            play()
            
        elif(userInput == "1"):
            about()
            
        elif(userInput == "2"):
            gameHelp()
            
        elif(userInput == "3"):
            running = False
            
        else:
            print("I'm sorry, I don't know what you want me to do.")

        
    print("\nThank you for playing!")

run()
    

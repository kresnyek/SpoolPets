# SpoolPet Server
# This is the server side of the game, which threads the requests of the client.
# v0.1
# Updated: 6/20/16
# By: kresnyek
# Created: 6/20/16

import socket
import sys
import threading

running = True
hostPort = 8888
hostName = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Created Socket')
#try to get the socket up
try:
    s.bind((hostName, hostPort))
#Checks if there is any errors
except socket.error as msg:
    print("Oh noes. Failed: " + str(msg[0]) + '\n' + str(msg[1]))
    
print ('woooo! Socket Bound!')

#CLASSES---------------------------------------------------------------------------
class ThreadHandler(threading.Thread):
    
    #Initialize thread with pet
    def __init__(self, pet, connection):
        self.pet = pet
        self.conn = connection
        threading.Thread.__init__(self)

    #What the thread does    
    def run(self):
        print("Created Thread, and is running")
        msg = "100" #Welcome
        self.conn.send(msg.encode('UTF-8', 'strict'))
        running = True
        while running:
            try:
                userInput = self.conn.recv(1024).decode("utf-8")
                
            except socket.error as msg:
                print("Error: " + str(msg[0]) + '\n' + str(msg[1]) )

            userInput = (userInput.upper()).split()
            if(len(userInput) > 0):
                if(userInput[0] == "QUIT"):
                   
                    #Kills the server
                    if(len(userInput) > 1 and userInput[1] == "ALL"):
                        global running
                        running = False
                        print("Killing Server")
                    running = False   
                elif(userInput[0] == "ABOUT"):
                    print("About Pet Requested")
                else:
                    msg = "104" #Action not found
                    self.conn.send(msg.encode('UTF-8', 'strict'))
            else:
                msg = "105" #Message Empty
                self.conn.send(msg.encode('UTF-8', 'strict'))
                
#END CLASSES-----------------------------------------------------------------------
s.listen(10)
while running:
    connection, address = s.accept()
    pet = 2
    t = ThreadHandler(pet, connection)
    t.start()

s.close()

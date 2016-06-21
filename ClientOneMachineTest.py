# SpoolPet ClientOneMachineTest
# This is the client side of the game, and is used to test mutiple threads from one computer.
# v0.2
# Updated: 6/21/16
# By: kresnyek
# Created: 6/20/16

import socket
#import sys
import threading


#This is to test mutiple threads from one computer
class ThreadHandlerClient(threading.Thread):
    def __init__(self, count):
        self.count = count
        threading.Thread.__init__(self)
        
    def run(self):
        self.makeAConnection()
        print("Thread " + str(self.count) + " made a connection")
        
        while True:
            print("Thread Time: " + str(self.count))
        
        
    def makeAConnection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = ('localhost', 8888)
        print("trying to connect to port 8888")
        s.connect(serverAddress)
        print("connected")

        try:
            print("received: " + s.recv(1024).decode("utf-8") )
            msg = "Hello World"
            s.send(msg.encode('UTF-8', 'strict'))
            
        except socket.error as msg:
            print("Oh noes. Failed: " + str(msg[0]) + '\n' + str(msg[1]))

#This is just to test running mutiple threads at once
def doSomething():
    for x in range(5):
        t= ThreadHandlerClient(x)
        t.start()
    
    

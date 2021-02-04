import socket
import sys
from datetime import datetime

__author__      = "Erik Stroud"


#creates the socket and asks the user for input to set up the address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input ("Please enter an IP address or hostname: ")
port = int(input ("Please enter a port number: "))

#sets default variable
message = ''

#sets the server connection
server_address = ((server, port))

#Connects the to the server
print ("connecting")
sock.connect(server_address)
print("You have connected to your apartment's server \n type help for a list of commands \n")


#Will run until exit is typed
while message != "exit":

    #User can input commands
    message = input("Please enter your first name and departed/returned: ")
    if message == "help":
        print("exit - closes connection and shuts down client and server \n")
    else:

        #Message is encoded sent to the server
        message.encode()
        sock.sendto(message.encode('utf-8'), (server, port))

        #Data is received and decoded
        data = sock.recv(256)
        print (data.decode())
 

#if exit is sent, connection is closed 
print ('Connection Closed')
sock.sendto(message.encode('utf-8'), (server, port))
sock.close()
exit

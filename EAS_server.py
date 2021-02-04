import socket
import sys
import csv
import twitter
import HTML
from datetime import datetime

__author__      = "Erik Stroud"


#csvWriter will write the data to a CSV file for archiving
def csvWriter(name, status):
    with open('status.csv', 'a') as mainFile:
        print (name + " has " + status + " at " + str(datetime.now()))
        file = csv.writer(mainFile)
        file.writerow([name, status, str(datetime.now())])


#Uses the HTML library to write a list of
#status updates to a HTML file in a HTML Table
def htmlTableWriter(name, status, dataList):
    htmlFile = open('index.html', 'w')
    dataList.append([name, status, str(datetime.now())])
    htmlcode = HTML.table(dataList)
    print(htmlcode, file = htmlFile)
    htmlFile.close()

def sendMessage(connection, host, port, name, status, api):
    message = "Your status has been logged at " + str(datetime.now())
    time = str(datetime.now())
    connection.sendto(message.encode('utf-8'), (host, port))
    csvWriter(name, status)
    htmlTableWriter(name, status, dataList)
    api.PostUpdate(name + ' has ' + status + ' at ' + time)    

#Setting up the Twitter account
api = twitter.Api(consumer_key="wfaENNZRWTiv1qx6OsdlZBZhI",
                  consumer_secret="ktk04oZJqP80WpjGIqOCxoZesWZ1BOPtgqva80ofmz9c36WcFt",
                  access_token_key="16537303-mtjjvK9oGW2HHRcNsky3BwynASkiZ1B36dso0wnjD",
                  access_token_secret="RurbRPs8OvPgiKE3eSYZ20Af7hMnwJ4CpGDlrklznaAUi")


#creates the socket and asks the user for input to set up the address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Please enter the IP Address of this server: ")
port = int(input ("Please enter a port number: "))

#Default Messages
incorrect = "Please enter only FIRST NAME and returned/departed \n"

#Binds the socket and begins listening
sock.bind((host, port))
sock.listen(1)

#creates the basic variables and the data list while waiting for a connection
dataList = []
data = ""
data = data.encode('utf-8')
print ('waiting for a connection')


#accepts the connection and prints the name of the client that connected 
connection, client = sock.accept()
print (client, 'connected')


#Will run so long as the client doesn't send exit
while data != "exit":

    #receives and decodes the data
    data = connection.recv(256)
    data = data.decode()

    #closes the connection
    if data == "exit":
        print("Connection Closed, shutting down server")
        connection.close()
        break

    #splits the data into the separate variables and properly formats them
    name, status = data.split(' ',1)
    name = name.capitalize()
    status = status.lower()


    #Checks to see if the user departed or returned
    if status == "departed" or "returned":
        sendMessage(connection, host, port, name, status, api)

    #Checks if the message matches the 2 valid commands    
    if status != "returned" or "departed":
        connection.sendto(incorrect.encode('utf-8'), (host, port))
 
exit

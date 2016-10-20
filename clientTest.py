#!/usr/bin/python
# client.py  
import socket
import sys
'''{
  "animals": "all",
  "operation": "lookup",
  "field": "weight" 
}'''

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get host, port
host = '104.196.166.63'        
port = 12345

# connection to hostname on the port.
s.connect((host, port))                               

print "Server connected \nhost: " + host + "\nPort: " + str(port)
# Receive no more than 1024 bytes

#Get user input, and send message
userInput = input("Enter json object: ")

s.sendall(userInput.encode('utf-8'))

#Recieve response from server
data = s.recv(1024)
print('From server (', data.decode('utf-8'), ')')

s.close()




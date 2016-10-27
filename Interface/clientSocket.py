#!/usr/bin/python
import socket
import sys

host = '104.196.166.63'        # Server IP
port = 12345                   # Port accepting connection 



def sendSearchRequest(requests):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	print ("Server connected \nhost: " + host + "\nPort: " + str(port))

	searchFields = requests.split(" ")

	jsonMessage = '{"operation": "lookup", "animals": "all", "field": ['

	for field in searchFields:
	    jsonMessage += '"' + field + '", ' 

	jsonMessage = jsonMessage[:-2]
	jsonMessage += ']}'

	print("Created JSON search: " , jsonMessage)
	s.sendall(jsonMessage.encode('utf-8'))

	#Recieve response from server
	data = s.recv(1024)
	print('server returned: ' + data.decode('utf-8'))

	s.close()


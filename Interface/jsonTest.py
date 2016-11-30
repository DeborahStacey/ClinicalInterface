#!/usr/bin/python
import socket
import sys
import json

host = '104.196.166.63'        # Server IP
port = 12345                   # Port accepting connection 



def sendSearchRequest(requests,varNames):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	#print ("Server connected \nhost: " + host + "\nPort: " + str(port))

	searchFields = requests

	jsonMessage2 = '{"operation": "lookup", "animals": "cat",'
	counter = 0
	jsonMessage2 += '"field":' 
	print("number of varnames" + str(len(varNames)))
	if(len(varNames)>=2):
		jsonMessage2 += '[{"$and":['
	for field in searchFields: 
	    jsonMessage2 += '{' +'"' + varNames[counter] + '"' + ':' + '{' + '"' + "eq" + '"' + ':' + field + '}' + '}'
	    if(len(varNames)>=2 and counter<(len(varNames)-1) ):
	    	jsonMessage2 += ','
	    counter+= 1

	if(len(varNames)>=2):
		jsonMessage2+= ']}]'
	jsonMessage2 += '}'

	#print (jsonMessage2)
	#print "Created JSON search: " + jsonMessage2
	s.sendall(jsonMessage2.encode('utf-8'))
  
	#Recieve response from server
	target = open("test.txt", 'w')
	info = ''
	while True:
		data = s.recv(32767)
		if not data:break
		info += data.decode('utf-8') 
	#test = json.loads(data)
	#print (info)
	#print('server returned: ' + data.decode('utf-8'))

	s.close()
	#test = json.loads(data.decode('utf-8'))
	return info

varNames = []
"""breed = raw_input("Enter Cat Breed:")
if(breed != ""):
	varNames.append("Breed")
Colour = raw_input("what colour is your cat:")
if(Colour!= ""):
	varNames.append("Colour")"""
#length = raw_input("what is the length:")
#if(length!= ""):
#	varNames.append("length")
#weight = input("Enter weight:")
#if(weight!=""):
#	varNames.append("weight")
#temp = weight 
#print (temp)
#sendSearchRequest(temp, varNames)

#Flags
# Breed, Colour, Age, gender, deceased, wt, ht, length, pet id, owner id,name
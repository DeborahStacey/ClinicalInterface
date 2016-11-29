import json
import socket
import sys
import datetime
import requests
from tkinter import *

def convertJson(objName):
	objFile = open(objName, 'r')
	jsonString = objFile.read()
	return jsonString	

def sendJson(jsonString, action):		
	parsedObj = json.loads(jsonString)
	status = checkJson(parsedObj, action)
	return status

def checkDate(date):
	newDate = date.split('-', 2)
	if(len(newDate) == 3):
		try:
			newDate = datetime.datetime(int(newDate[0]), int(newDate[1]), int(newDate[2]))
			return(True)
		except ValueError:
			return(False)
	else:
		return(False)

def checkJson(parsedObj, action):
	canSend = False
	count = 0
	for obj in parsedObj:
		count += 1

	if(count > 15 or count == 0):
		printError(1, '')
		return canSend		
	else:		
		if (parsedObj.get("owner") == None or parsedObj.get("owner") == "" or type(parsedObj.get("owner")) != str):
			printError(2, parsedObj.get("owner"))
			return canSend

		if (parsedObj.get("animalTypeID") != None and type(parsedObj.get("animalTypeID")) != int):
			printError(2, parsedObj.get("animalTypeID"))
			return canSend

		if (parsedObj.get("petID") != None and type(parsedObj.get("petID")) != int):
			printError(2, parsedObj.get("petID"))
			return canSend

		if (parsedObj.get("name") != None and type(parsedObj.get("name")) != str or parsedObj.get("name") == ""):
			printError(2, parsedObj.get("name"))
			return canSend

		if (parsedObj.get("breed") != None and type(parsedObj.get("breed")) != int):
			printError(2, parsedObj.get("breed"))
			return canSend

		if (parsedObj.get("gender") != None and type(parsedObj.get("gender")) != int):
			printError(2, parsedObj.get("gender"))
			return canSend

		if (parsedObj.get("microchip") != None and type(parsedObj.get("microchip")) != bool):
			printError(2, parsedObj.get("microchip"))
			return canSend

		if (parsedObj.get("fitcat") != None and type(parsedObj.get("fitcat")) != bool):
			printError(2, parsedObj.get("fitcat"))	
			return canSend

		if (parsedObj.get("weight") != None and type(parsedObj.get("weight")) != float):
			printError(2, parsedObj.get("weight"))	
			return canSend

		if (parsedObj.get("height") != None and type(parsedObj.get("height")) != float):
			printError(2, parsedObj.get("height"))	
			return canSend

		if (parsedObj.get("length") != None and type(parsedObj.get("length")) != float):
			printError(2, parsedObj.get("length"))
			return canSend

		if (parsedObj.get("dateofdeath") != None and type(parsedObj.get("dateofdeath")) != str):
			printError(2, parsedObj.get("dateofdeath"))
			return canSend

		if (parsedObj.get("reasonfordeath") != None and type(parsedObj.get("reasonfordeath")) != str):
			printError(2, parsedObj.get("reasonfordeath"))
			return canSend

		if (parsedObj.get("lastupdate") != None and type(parsedObj.get("lastupdate")) != str):
			printError(2, parsedObj.get("lastupdate"))
			return canSend

		if (parsedObj.get("dateAdded") != None and type(parsedObj.get("dateAdded")) != str):
			print("Invalid date added format")
			printError(2, parsedObj.get("dateAdded"))
			return canSend

		if(parsedObj.get("dateOfBirth") != None and checkDate(parsedObj.get("dateOfBirth")) == False):
			print("Invalid date of birth format")
			printError(2, parsedObj.get("dateOfBirth"))			
			return canSend
		else:
			username = "taha@mymail.com"
			password = "soccer123"
			canSend = login(username, password, parsedObj, action)
			return canSend

def printError(flag, field):
	if(flag == 1):
		print("Invalid Json Format check # of fields")
	if(flag==2):
		if(field == ""):
			print ("Missing an important field")
		else:	
			print("Invalid field: " + str(field))

def login(userEmail, password, parseObj, action):
	loginString = {"email": userEmail,"password": password}
	loginObj = json.dumps(loginString)
	print(json.loads(loginObj))

	with requests.Session() as s: 
		p = s.post("https://cat.ddns.net/Backend/api.php/user/login", data=json.loads(loginObj))
		print(p.text)
		canSend = sendData(s, parseObj, action)		
	return canSend

def sendData(session, obj, action):

	url1 = "https://cat.ddns.net/Backend/api.php/PM/create"
	url2 = "https://cat.ddns.net/Backend/api.php/pet/update"
	url3 = "https://cat.ddns.net/Backend/api.php/pet/pets"
	
	postData = {}
	for line in obj:
		postData[line] = (obj.get(str(line))) 
			
	print("\n-----------connecting to backend--------------\n")
	
	postObj = json.dumps(postData)
	objString = json.dumps(obj)

	if(action == "add"):
		r=session.post(url1,data=json.loads(objString))
		print(r.url, "returned: ",r.text)

		if(r.text.find("true") > 0):
			return True
		else:
			return False
	elif(action == "update"):
		r=session.put(url2,data=json.loads(objString))
		print(r.url, "returned: ",r.text)

		if(r.text.find("true") > 0):
			return True
		else:
			r=session.get(url3)
			ownerCats = json.loads(r.text)
			print("Please ensure the petid is set for the update")
			print(ownerCats["personal"][0]["firstname"] + " has the following pets: ")

			for x in range(0,len(ownerCats)):
				print(str(ownerCats["personal"][x]["name"]) + " has id: " + str(ownerCats["personal"][x]["petid"]))			
	else:
		print("Incorrect action. Must be add or update. ")
		return False				
	
#API example
message = convertJson("tansari.json") 			
status = sendJson(message,"update")
if(status == True):
	print ("Json object successfully sent")
else:
	print ("Error sending json obj")
	
 # login example

#login("taha@mymail.com", "soccer123")




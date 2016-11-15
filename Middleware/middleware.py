import json
import socket
import sys
import datetime
import requests

def convertJson(objName):
    objFile = open(objName, 'r')
    jsonString = objFile.read()
    return jsonString	

def sendJson(jsonString):		
	parsedObj = json.loads(jsonString)
	status = checkJson(parsedObj)
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

def checkJson(parsedObj):
	canSend = False
	count = 0
	for obj in parsedObj:
		count += 1

	if(count > 15 or count == 0):
		printError(1, '')
		return canSend		
	else:		
		'''if (parsedObj.get("ownerid") == None or parsedObj.get("ownerid") == "" or type(parsedObj.get("ownerid")) != str):
			printError(2, parsedObj.get("ownerid"))
			return canSend'''

		if (parsedObj.get("petid") != None and type(parsedObj.get("petid")) != str):
			printError(2, parsedObj.get("petid"))
			return canSend

		if (parsedObj.get("name") != None and type(parsedObj.get("name")) != str or parsedObj.get("name") == ""):
			printError(2, parsedObj.get("name"))
			return canSend

		if (parsedObj.get("breedid") != None and type(parsedObj.get("breedid")) != int):
			printError(2, parsedObj.get("breedid"))
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

		if (parsedObj.get("dateOfBirth") != None and type(parsedObj.get("dateOfBirth")) != str):
			printError(2, parsedObj.get("dateOfBirth"))			
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

		if (parsedObj.get("dateadded") != None and type(parsedObj.get("dateadded")) != str):
			printError(2, parsedObj.get("dateadded"))
			return canSend
		else:			
			if(parsedObj.get("dateOfBirth") != None and checkDate(parsedObj.get("dateOfBirth")) == False):
				print("Invalid date of birth format")
				return canSend
			else:
				canSend = sendData(parsedObj)			
				return canSend

def printError(flag):
	if(flag == 1):
		print("Invalid Json Format not enough fields")
	if(flag==2):
		if(field == ""):
			print ("Missing an important field")
		else:	
			print("Invalid field: " + str(field))

def sendData(obj):
	#url = "http://localhost/post.php"
	url = "http://10.12.204.218/Backend/api.php/PM/create"
	print("Sending data: \n")
	for line in obj:
		print(line + ": " + str(obj.get(str(line))))
	print("\n-----------connecting to backend--------------\n")
	r=requests.post(url,data=obj)
	print(r.url, "returned: ",r.text)

	return True	
	
#API example
message = convertJson("tansari.json") 			
status = sendJson(message)
if(status == True):
	print ("Json object successfully sent")
else:
	print ("Error sending json obj")	





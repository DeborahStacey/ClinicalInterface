import json

def sendJson(objName):		
	objFile = open(objName, 'r')
	jsonString = objFile.read()	
	parsedObj = json.loads(jsonString)
	status = checkJson(parsedObj)

	return status

def checkJson(parsedObj):
	canSend = False
	count = 0
	for obj in parsedObj:
		count += 1

	if(count != 15):
		printError(1, '')
		return canSend		
	else:		
		if (type(parsedObj.get("ownerid")) != str):
			printError(2, parsedObj.get("ownerid"))
			return canSend
		if (type(parsedObj.get("petid")) != str):
			printError(2, parsedObj.get("petid"))
			return canSend

		if (type(parsedObj.get("name")) != str):
			printError(2, parsedObj.get("name"))
			return canSend

		if (type(parsedObj.get("breedid")) != int):
			printError(2, parsedObj.get("breedid"))
			return canSend

		if (type(parsedObj.get("gender")) != int):
			printError(2, parsedObj.get("gender"))
			return canSend

		if (type(parsedObj.get("microchip")) != bool):
			printError(2, parsedObj.get("microchip"))
			return canSend

		if (type(parsedObj.get("fitcat")) != bool):
			printError(2, parsedObj.get("fitcat"))	
			return canSend

		if (type(parsedObj.get("dateofbirth")) != str):
			printError(2, parsedObj.get("dateofbirth"))
			return canSend

		if (type(parsedObj.get("weight")) != float):
			printError(2, parsedObj.get("weight"))	
			return canSend

		if (type(parsedObj.get("height")) != float):
			printError(2, parsedObj.get("height"))	
			return canSend

		if (type(parsedObj.get("length")) != float):
			printError(2, parsedObj.get("length"))
			return canSend

		if (type(parsedObj.get("dateofdeath")) != str):
			printError(2, parsedObj.get("dateofdeath"))
			return canSend

		if (type(parsedObj.get("reasonfordeath")) != str):
			printError(2, parsedObj.get("reasonfordeath"))
			return canSend

		if (type(parsedObj.get("lastupdate")) != str):
			printError(2, parsedObj.get("lastupdate"))
			return canSend

		if (type(parsedObj.get("dateadded")) != str):
			printError(2, parsedObj.get("petid"))
			return canSend
		else:
			canSend = True
			sendData(parsedObj)			
			return canSend

def printError(flag, field):
	if(flag == 1):
		print("Invalid Json Format not enough fields")
	if(flag==2):
		print("Invalid field: " + str(field))

def sendData(obj):
	for line in obj:
		print(line + ": " + str(obj.get(str(line))))

			
status = sendJson("tansari.json")
if(status == True):
	print ("Json object successfully sent")
else:
	print ("Error sending json obj")	





import json


def readJson(objName):	
	objFile = open(objName, 'r')
	jsonString = objFile.read()	
	parsedObj = json.loads(jsonString)
	#print (parsedObj)
	recieveJson(parsedObj)

def recieveJson(parsedObj):

	print(parsedObj.get("ownerid"))

readJson("tansari.json")	
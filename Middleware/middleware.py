import json


def readJson(objName):	
	objFile = open(objName, 'r')
	jsonString = objFile.read()	
	parsedObj = json.loads(jsonString)
	#print (parsedObj)
	recieveJson(parsedObj)

def recieveJson(parsedObj):
	print (parsedObj[0]["ownerid"])



readJson("tansari.json")	
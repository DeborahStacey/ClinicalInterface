#!/usr/bin/python
import json

def main():
	'''print "Welcome to the Practice Management System Generator"
	print "Please choose an option:\n1) \n2) \n3)Quit\n"
	option = raw_input(">: ");'''

	# set JSON object as string path 
	objPath = "cat.JSON"
	objFile = open(objPath, 'r')
	jsonString = objFile.read()	
	# load data from json string into a parse object 
	parsedObj = json.loads(jsonString)

	#Example for loop accessing each data value 
	for i in range (0, len(parsedObj["Household"])):
		print "CAT_ID:" +  parsedObj["Household"][i]["CAT_ID"]
		print "Height:" + str(parsedObj["Household"][i]["Height"]) 
		print "Weight:" + str(parsedObj["Household"][i]["Weight"]) 
		print "Type:" + parsedObj["Household"][i]["Type"]
		print "\n"

main()
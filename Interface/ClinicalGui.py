#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from collections import *
import json
from jsonTest import *
from InputVariables import *

# Generates JSON-file from the list of enteries.
#	@param:  The name of the JSON-file to be generated.
#			 The list of data to be included in the JSON-file.
def write_JsonFile(fileName, fileData):
	with open(fileName + ".json", "w") as outFile:
		json.dump(fileData, outFile, indent=4, separators=(',', ':'))
	return None

# Reads the list of entries from the JSON-file.
#	@param:  The name of the JSON-file to be generated.
#	@return: The list of data to be included in the JSON-file.
def read_JsonFile(fileName):
	with open(fileName + ".json", "r") as inFile:
		fileData = json.load(inFile)
	return fileData

# The Application class that is used to encapsulate the GUI object.
class ClinicalGui:
	# Creates an Application instance.
	#	@param:  The name of the Application. 
	def __init__(self, title):
		self.windowTitle = title
		self.setOfWidgets = []
		self.clientWidgetCount = 0
		self.patientWidgetCount = 0


	def updateBreedWidget(self, widgetSpecies, widgetBreeds):
		if (widgetSpecies.get() == ""):
			widgetBreeds.config(values=[])
		else:
			widgetBreeds.config(values=constBreeds[widgetSpecies.get()])

	# This function takes all the values and constructs a JSON from all the fields 
	def Search(self):
		
		testVar = []
		requests = []
		if(widgetOwnerID.get()):
			print("value entered")
			testVar.append("ownerid")
			requests.append(widgetOwnerID.get())
		if(widgetPetName.get()):
			print("value entered")
			testVar.append("name")
			requests.append("\""+ widgetPetName.get() +"\"")
		if(widgetPetID.get()):
			testVar.append("petid")
			print("value entered")
			requests.append(widgetPetID.get())
		if(widgetWeight.get()):
			testVar.append("weight")
			requests.append(widgetWeight.get())
			print("value entered")
		if(widgetHeight.get()):
			testVar.append("height")
			print("value entered")
			requests.append(widgetHeight.get())
		if(widgetGender.get()):
			testVar.append("gender")
			requests.append(widgetGender.get())
		if(widgetReasonDeath.get()):
			testVar.append("reasonfordeath")
			requests.append(widgetReasonDeath.get())
		if(widgetDeathDate.get()):
			testVar.append("dateofdeath")
			requests.append(widgetDeathDate.get())
		if(checkFitCat.get() == 1):
			testVar.append("fitcat")
			print("YES WORKING")
			requests.append("\"" + "True" + "\"")
		if(checkMicrochip.get() == 1):
			testVar.append("microchip")
			requests.append("\"" + "True" + "\"")
		if(widgetBreed.get()):
			testVar.append("breed")
			requests.append(widgetBreed.get())
		if(widgetDateUpdate.get()):
			testVar.append("lastupdated")
			requests.append(widgetDateUpdate.get())
		if(widgetDateAdded.get()):
			testVar.append("dateadded")
			requests.append(widgetDateAdded.get())
		temp = sendSearchRequest(requests, testVar)
		test = json.loads(temp)
		T.configure(state='normal')
		for i in range(0,len(test["cats"])):
			T.insert(END,"Name:" + test["cats"][i]['name'] + "\n")
			T.insert(END,"Petid:" + test["cats"][i]['petid'] + "\n")
			T.insert(END,"Ownerid" + test["cats"][i]['ownerid'] + "\n")
			T.insert(END,"Gender" + test["cats"][i]['gender'] + "\n")
			T.insert(END,"ReasonforDeath:" + test["cats"][i]['reasonfordeath'] + "\n")
			T.insert(END,"Dateofdeath:"+test["cats"][i]['dateofdeath'] + "\n")
			T.insert(END,"fitcat:" + test["cats"][i]['fitcat'] + "\n")
			T.insert(END,"Microchip:" + test["cats"][i]['microchip'] + "\n")
			T.insert(END,"Breed:" + test["cats"][i]['breed'] + "\n")
			T.insert(END,"Lastupdated:" + test["cats"][i]['lastupdated'] + "\n")
			T.insert(END,"Weight:" + test["cats"][i]['weight'] + "\n")
			T.insert(END,"Height:" + test["cats"][i]['height'] + "\n")
			T.insert(END,"DateAdded:" + test["cats"][i]['dateadded'] + "\n")
			T.insert(END,"-------------------------" +"\n")

		T.configure(state='disabled')
		print ("Search")
		return
		

	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	 The list of prompts to be included in the App.
	def create_Window(self):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.windowTitle);
		self.root.resizable(width=True, height=True)



		# Widgets for the OwnerID and PetID fields (disabled state).
		Label(self.root, text="Owner ID:").grid(row=0, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetOwnerID
		widgetOwnerID = Entry(self.root)
		widgetOwnerID.grid(row=0, column=1, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetOwnerID)

		Label(self.root, text="Pet ID:").grid(row=0, column=6, padx=0, pady=(15,0), sticky='nsew')
		global widgetPetID
		widgetPetID = Entry(self.root)
		widgetPetID.grid(row=0, column=7, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetPetID)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=1, columnspan=12, padx=3, pady=(15,0), sticky='nsew')

		# Widgets for the fields regarding general information of the pet (enabled state).
		Label(self.root, text="Name:").grid(row=2, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetPetName
		widgetPetName = Entry(self.root)
		widgetPetName.grid(row=2, column=1, columnspan=11, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetPetName)
		
		#Label(self.root, text="Species:").grid(row=3, column=0, padx=0, pady=(15,0), sticky='nsew')
		#global widgetSpecies
		#widgetSpecies = ttk.Combobox(self.root, width=1, state="readonly", values=constSpecies)
		#widgetSpecies.grid(row=3, column=1, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		#widgetSpecies.bind("<<ComboboxSelected>>", lambda e:self.updateBreedWidget(widgetSpecies, widgetBreed))
		#self.setOfWidgets.append(widgetSpecies)


		Label(self.root, text="Breed:").grid(row=3, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetBreed
		widgetBreed = ttk.Combobox(self.root, width=1, state="readonly")
		widgetBreed.grid(row=3, column=1, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetBreed)
		
		Label(self.root, text="Gender:").grid(row=3, column=6, padx=0, pady=(15,0), sticky='nsew')
		global widgetGender
		widgetGender = ttk.Combobox(self.root, width=1, state="readonly", values=constGenders)
		widgetGender.grid(row=3, column=7, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetGender)

		Label(self.root, text="Microchip:").grid(row=4, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetMicrochip
		global checkMicrochip
	#	checkMicrochip = bool()
		checkMicrochip = IntVar()
		widgetMicrochip = Checkbutton(self.root,variable = checkMicrochip)
		widgetMicrochip.grid(row=4, column=1, columnspan=3, sticky='ws')
		self.setOfWidgets.append(widgetMicrochip)
		
		Label(self.root, text="FitCat:").grid(row=4, column=4, padx=0, pady=(15,0), sticky='nsew')
		global widgetFitCat
		global checkFitCat
		checkFitCat = IntVar()
	#	checkFitCat = bool()
		widgetFitCat = Checkbutton(self.root, variable = checkFitCat)
		widgetFitCat.grid(row=4, column=5, columnspan=3, sticky='ws')
		self.setOfWidgets.append(widgetFitCat)
		
		Label(self.root, text="Date of Birth:").grid(row=6, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetDateBirth
		widgetDateBirth = Entry(self.root)
		widgetDateBirth.grid(row=6, column=1, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateBirth)

		Label(self.root, text="Date of Death:").grid(row=6, column=6, padx=0, pady=(15,0), sticky='nsew')
		global widgetDeathDate
		widgetDeathDate = Entry(self.root)
		widgetDeathDate.grid(row=6, column=7, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetDeathDate)

		Label(self.root, text="Reason for Death:").grid(row=7, column=6, padx=0, pady=(15,0), sticky='nsew')
		global widgetReasonDeath
		widgetReasonDeath = Entry(self.root)
		widgetReasonDeath.grid(row=7, column=8, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetReasonDeath)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=8, columnspan=12, padx=3, pady=(15,0), sticky='nsew')

		# Widgets for the fields regarding specific information of the pet (enabled state).
		Label(self.root, text="Wt. (lbs):").grid(row=9, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetWeight
		widgetWeight = Entry(self.root, width=12)
		widgetWeight.grid(row=9, column=1, columnspan=2, padx=(0,6), pady=(15,0), sticky='w')
		self.setOfWidgets.append(widgetWeight)

		Label(self.root, text="Ht. (cm):").grid(row=9, column=4, padx=0, pady=(15,0), sticky='nsew')
		global widgetHeight
		widgetHeight = Entry(self.root, width=12)
		widgetHeight.grid(row=9, column=5, columnspan=2, padx=(0,6), pady=(15,0), sticky='w')
		self.setOfWidgets.append(widgetHeight)

		Label(self.root, text="Len. (cm):").grid(row=9, column=9, padx=0, pady=(15,0), sticky='nsew')
		global widgetLength
		widgetLength = Entry(self.root, width=12)
		widgetLength.grid(row=9, column=10, columnspan=2, padx=(0,6), pady=(15,0), sticky='w')
		self.setOfWidgets.append(widgetLength)
		
		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=10, columnspan=12, padx=3, pady=(15,0), sticky='nsew')

		# Widgets for the DateUpdated and DateAdded fields.
		Label(self.root, text="Date Updated:").grid(row=11, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetDateUpdate
		widgetDateUpdate = Entry(self.root)
		widgetDateUpdate.grid(row=11, column=1, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateUpdate)

		Label(self.root, text="Date Registered:").grid(row=11, column=6, padx=0, pady=(15,0), sticky='nsew')
		global widgetDateAdded
		widgetDateAdded = Entry(self.root)
		widgetDateAdded.grid(row=11, column=7, columnspan=5, padx=(0,6), pady=(15,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateAdded)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=12, columnspan=12, pady=(15,0))

		# Search button that takes all input and constructs a JSON object to query to the database
		searchButton = Button(self.root, text="Search", command=self.Search)
		searchButton.grid(row=13, column=0, columnspan=12, padx=12, pady=(15,0), sticky='nsew')


		#global results
		#results = Text(self.root, height=20, width=20, state = NORMAL)
		#results.grid( column = 50, columnspan=12, padx=12,pady=(15,6))
		#results.configure(state='disabled')
		Label(self.root, text="Search Results:").grid(row=0, column=20, padx=(30,0), pady=(15,0), sticky='nsew')
		global T
		T = Text(self.root, height=25, width=70, state = NORMAL)
		T.grid(row=1, column=15, rowspan = 14, columnspan=14, padx=5,pady=5)
		T.configure(state='disabled')

	# Presents the window instance to the user.
	def show_Window(self):
		self.root.mainloop();
		

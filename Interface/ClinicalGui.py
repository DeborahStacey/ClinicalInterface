#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from collections import *
import json

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

	

	# Randomly enters information into the prompts for all sections. (here just incase)
	def autofill(self):
		print ("Auto-fill")
		return

	# This function takes all the values and constructs a JSON from all the fields 
	def Search(self):
		# this function does nothing as of yet
		print ("Search")
		return
		

	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	 The list of prompts to be included in the App.
	def create_Window(self):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.windowTitle);
		self.root.resizable(width=False, height=False)


		# Widgets for the OwnerID and PetID fields (disabled state).
		Label(self.root, text="Owner ID:").grid(row=0, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetOwnerID = Entry(self.root)
		widgetOwnerID.grid(row=0, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetOwnerID)

		Label(self.root, text="Pet ID:").grid(row=0, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetPetID = Entry(self.root)
		widgetPetID.grid(row=0, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetPetID)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=1, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# Widgets for the fields regarding general information of the pet (enabled state).
		Label(self.root, text="Name:").grid(row=2, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetPetName = Entry(self.root)
		widgetPetName.grid(row=2, column=1, columnspan=11, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetPetName)
		
		Label(self.root, text="Breed:").grid(row=3, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetBreed = ttk.Combobox(self.root, width=1, state="readonly", values=["Feline", "Improvius", "Coder", "Persian"])
		widgetBreed.grid(row=3, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetBreed)
		
		Label(self.root, text="Gender:").grid(row=3, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetGender = ttk.Combobox(self.root, width=1, state="readonly", values=["male","female","whatever is left","test"])
		widgetGender.grid(row=3, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetGender)

		Label(self.root, text="Microchip:").grid(row=4, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetMicrochip = Checkbutton(self.root)
		widgetMicrochip.grid(row=4, column=1, columnspan=3, sticky='ws')
		self.setOfWidgets.append(widgetMicrochip)
		
		Label(self.root, text="FitCat:").grid(row=4, column=4, padx=0, pady=(6,0), sticky='nsew')
		widgetMicrochip = Checkbutton(self.root)
		widgetMicrochip.grid(row=4, column=5, columnspan=3, sticky='ws')
		self.setOfWidgets.append(widgetMicrochip)
		
		Label(self.root, text="Date of Birth:").grid(row=6, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateBirth = Entry(self.root)
		widgetDateBirth.grid(row=6, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateBirth)

		Label(self.root, text="Date of Death:").grid(row=6, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetDeathDate = Entry(self.root)
		widgetDeathDate.grid(row=6, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDeathDate)

		Label(self.root, text="Reason for Death:").grid(row=7, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetReasonDeath = Entry(self.root)
		widgetReasonDeath.grid(row=7, column=8, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetReasonDeath)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=8, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# Widgets for the fields regarding specific information of the pet (enabled state).
		Label(self.root, text="Wt. (lbs):").grid(row=9, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetWeight = Entry(self.root, width=12)
		widgetWeight.grid(row=9, column=1, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetWeight)

		Label(self.root, text="Ht. (cm):").grid(row=9, column=4, padx=0, pady=(6,0), sticky='nsew')
		widgetHeight = Entry(self.root, width=12)
		widgetHeight.grid(row=9, column=5, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetHeight)

		Label(self.root, text="Len. (cm):").grid(row=9, column=9, padx=0, pady=(6,0), sticky='nsew')
		widgetLength = Entry(self.root, width=12)
		widgetLength.grid(row=9, column=10, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetLength)
		
		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=10, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# Widgets for the DateUpdated and DateAdded fields.
		Label(self.root, text="Date Updated:").grid(row=11, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateUpdate = Entry(self.root)
		widgetDateUpdate.grid(row=11, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateUpdate)

		Label(self.root, text="Date Registered:").grid(row=11, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetDateAdded = Entry(self.root)
		widgetDateAdded.grid(row=11, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateAdded)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=12, columnspan=12)

		
		
		# Search button that takes all input and constructs a JSON object to query to the database
		searchButton = Button(self.root, text="Search", command=self.Search)
		searchButton.grid(row=13, column=0, columnspan=12, padx=12, pady=(0,6), sticky='nsew')

		#labelframe = ttk.LabelFrame(self.root, text="Search Results").grid(row=14,columnspan = 12)
		textField = Text(self.root, height=20, width=70, state = DISABLED).grid(row=15, columnspan=12)


	# Presents the window instance to the user.
	def show_Window(self):
		self.root.mainloop();

#!c:/Python34/python

from tkinter import *
import random
import json
import hello

# The list of all JSON-related information (household is already set).
	# THIS IS THE BASE STRUCTURE OF OUR JSON FILE...
listOfEntries = {"household" : [{}]}
# The list of all specified entries to be prompted by the Application.
	# MORE TEXTFIELDS CAN BE ADDED HERE...
listOfPrompts = [ "Name", "Breed", "Gender" ]
# The list of all dummy entries to be auto-filled into the Application.
	# THE DUMMY CONTENTS CAN BE CHANGED HERE...
listOfDummies = [ 
	["Manga", "Luna", "Oliver", "Chloe", "Smokey", "Gigi"], 
	["Siamese", "Persian", "Ocicat", "Siberian", "Pizza"],
	["Male", "Female", "Other"] 
]

# The Application class that is used to encapsulate the GUI object.
class App:
	# Creates an Application instance.
	#	@param: The name of the Application. 
	def __init__(self, title):
		self.wm_title = title
		self.wm_width = 300
		self.wm_height = 500
		self.wm_num = 1

	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	The maximum width of the window.
	#			The maximum height of the window.
	def create_Window(self):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.wm_title);
		self.root.resizable(width=False, height=False)
		# Organize the window into sections for the individual widgets.
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_columnconfigure(1, weight=8)

	# Presents the window instance to the user.
	def show_Window(self):
		# Positioning the window onto the center of the screen.
		px = (self.root.winfo_screenwidth() - self.wm_width) / 2
		py = (self.root.winfo_screenheight() - self.wm_height) / 2
		self.root.geometry('%dx%d+%d+%d' % (self.wm_width, self.wm_height, px, py))
		#
		hello.hello();
		# Main event-based loop for the window.
		self.root.mainloop();

	# Adds a custom text-field to the Application GUI.
	def add_Widgets(self, inputs):
		# The list of all current widgets/fields in the Application.
		listOfWidgets = {}
		# The textfield that conatins the HouseHold name.
		houseWidget = None

		def submit_Fields():
			# Name if the JSON file.
			fName = houseWidget.get()
			# Recplace the file name if household is not present. 
			if (fName == ""):
				fName = "temp"
			# Retrieve all entries and contain them to the lists.
			for i in listOfWidgets:
				listOfEntries["household"][0][i] = listOfWidgets[i].get()
			# Generate JSON file from entries.
			with open(fName + ".json", "w") as outFile:
				json.dump(listOfEntries, outFile)
			# Destroy window after successful JSON file creation.
			self.root.destroy()

		def auto_Fill():
			for i in range(0, len(listOfPrompts)):
				listOfWidgets[listOfPrompts[i]].delete(0, "end")
				listOfWidgets[listOfPrompts[i]].insert(0, random.choice(listOfDummies[i])) 

		# Adding Household-Label to the left-side of the grid.
		houseLabel = Label(self.root, text="HouseHold")
		houseLabel.grid(row=0, column=0, padx=12, pady=0, sticky='nsew')
		# Adding Household-Prompt to the right-side of the grid.
		houseEntry = Entry(self.root)
		houseEntry.grid(row=0, column=1, padx=12, pady=1, sticky='nsew')
		# Adding Household widget (label & prompt) to the list.
		houseWidget = houseEntry

		for i in inputs:
			# Adding Label to the left-side of the grid.
			newLabel = Label(self.root, text=i)
			newLabel.grid(row=self.wm_num, column=0, padx=12, pady=0, sticky='nsew')
			# Adding Prompt to the right-side of the grid.
			newPrompt = Entry(self.root)
			newPrompt.grid(row=self.wm_num, column=1, padx=12, pady=1, sticky='nsew')
			# Adding widget (label & prompt) to the list.
			listOfWidgets[i] = newPrompt
			# Increment the number of widgets on the window.
			self.wm_num += 1

		# Submit Button
		btnSubmit = Button(self.root, text="Submit", command=submit_Fields)
		btnSubmit.grid(row=self.wm_num, column=1, padx=12, pady=0, sticky='nsew')

		# Autofill Button (using Dummy-Text)
		btnAutoFill = Button(self.root, text="Autofill", command=auto_Fill)
		btnAutoFill.grid(row=self.wm_num, column=0, padx=12, pady=0, sticky='nsew')

###### The main execution of this script.

# Declaring an Application instance.
jsonGene = App("JSON Generator")
# Assembling the Application interface.
jsonGene.create_Window()
jsonGene.add_Widgets(listOfPrompts)
# Presenting the Application interface.
jsonGene.show_Window()
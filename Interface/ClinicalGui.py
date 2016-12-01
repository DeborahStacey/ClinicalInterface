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
		#self.setOfWidgets = []
		self.clientWidgetCount = 0
		self.patientWidgetCount = 0


	def updateBreedWidget(self, widgetSpecies, widgetBreeds):
		if (widgetSpecies.get() == ""):
			widgetBreeds.config(values=[])
		else:
			widgetBreeds.config(values=constBreeds[widgetSpecies.get()])

	#resets the fields in the search boxes
	def resetFields(self):
		self.setOfWidgets[0].delete(0, "end")
		self.setOfWidgets[1].delete(0, "end")
		self.setOfWidgets[2].delete(0, "end")
		self.setOfWidgets[3].set("")
		self.setOfWidgets[4].set("")
		self.setOfWidgets[5].deselect()
		self.setOfWidgets[6].deselect()
		self.setOfWidgets[7].delete(0, "end")
		self.setOfWidgets[8].delete(0, "end")
		self.setOfWidgets[9].delete(0, "end")
		self.setOfWidgets[10].delete(0, "end")
		self.setOfWidgets[11].delete(0, "end")
		self.setOfWidgets[12].delete(0, "end")
		self.setOfWidgets[13].delete(0, "end")
		self.setOfWidgets[14].delete(0, "end")

	def OnDoubleClick(self, event):

		top = Toplevel()
		top.geometry("380x550")
		top.title("Cat Details")

		#store all details in a list for the selected cat
		item = self.tree.selection()[0]
		detailList = self.tree.item(item, "values")

		msg = Label(top, text="Owner ID: ").grid(row=0, column=0, padx=0, pady=(6,0), sticky='nsew')
		msg = Label(top, text=(self.tree.item(item, "text"))).grid(row=0, column=3, padx=0, pady=(6,0), sticky='nsew')
	
		for i in range (19):
			item = self.tree.selection()[0]
			#msg = Message(top, text=constColumns[i] + ": " + (self.tree.item(item,"text")))
			#msg.grid(row = i, column = 0)
			#Label(self.root, text="Wt. (lbs):").grid(row=9, column=0, padx=0, pady=(15,0), sticky='nsew')
			msg = Label(top, text=constColumns[i] + ": ").grid(row=i+1, column=0, padx=0, pady=(6,0), sticky='nsew')
			msg = Label(top, text=(detailList[i])).grid(row=i+1, column=3, padx=0, pady=(6,0), sticky='nsew')
	
		msg = Label(top, text=constColumns[i] + ": ").grid(row=i+1, column=0, padx=0, pady=(6,0), sticky='nsew')
		msg = Label(top, text=(detailList[i])).grid(row=i+1, column=3, padx=0, pady=(6,0), sticky='nsew')
		
		button = Button(top, text="Dismiss", command=top.destroy).grid(row=i+2, column=2, pady = 6)

	# This function takes all the values and constructs a JSON from all the fields 
	def Search(self):
		
		testVar = []
		requests = []
		

		#setting temporary numerical values for breeds and genders for database
		if(widgetBreed.get() == "Feline"):
			breedNum = 1
		if(widgetBreed.get() == "American Bobtail"):
			breedNum = 2
		if(widgetBreed.get() == "Bengal"):
			breedNum = 3
		if(widgetBreed.get() == "Persian"):
			breedNum = 4
		if (widgetGender.get() == "Male"):
			genderNum = 1
		if (widgetGender.get() == "Male (Neutered)"):
			genderNum = 2
		if (widgetGender.get() == "Female"):
			genderNum = 3
		if (widgetGender.get() == "Female (Spayed)"):
			genderNum = 4

		if(widgetOwnerID.get()):
			testVar.append("ownerid")
			requests.append(widgetOwnerID.get())
		if(widgetPetName.get()):
			testVar.append("name")
			requests.append("\""+ widgetPetName.get() +"\"")
		if(widgetPetID.get()):
			testVar.append("petid")
			requests.append(widgetPetID.get())
		if(widgetWeight.get()):
			testVar.append("weight")
			requests.append(widgetWeight.get())
		if(widgetHeight.get()):
			testVar.append("height")
			requests.append(widgetHeight.get())
		if(widgetGender.get()):
			testVar.append("gender")
			requests.append(str(genderNum))
		if(widgetReasonDeath.get()):
			testVar.append("reasonfordeath")
			requests.append(widgetReasonDeath.get())
		if(widgetDeathDate.get()):
			testVar.append("dateofdeath")
			requests.append(widgetDeathDate.get())
		if(checkFitCat.get() == 1):
			testVar.append("fitcat")
			requests.append("\"" + "True" + "\"")
		if(checkMicrochip.get() == 1):
			testVar.append("microchip")
			requests.append("\"" + "True" + "\"")
		if(widgetBreed.get()):
			testVar.append("breed")
			requests.append(str(breedNum))
		if(widgetDateUpdate.get()):
			testVar.append("lastupdated")
			requests.append(widgetDateUpdate.get())
		if(widgetDateAdded.get()):
			testVar.append("dateadded")
			requests.append(widgetDateAdded.get())
		temp = sendSearchRequest(requests, testVar)
		test = json.loads(temp)

		#clears field only if there are previous entries
		for row in self.tree.get_children():
			self.tree.delete(row)

		#add search results to the treeview
		for i in range(0,len(test["cats"])):
			self.tree.insert('', 'end', text = test["cats"][i]['ownerid'], values = (test["cats"][i]['petid'], test["cats"][i]['name'], test["cats"][i]['breed'], test["cats"][i]['gender'], test["cats"][i]['weight'],
			test["cats"][i]['height'], test["cats"][i]['length'], test["cats"][i]['microchip'], test["cats"][i]['fitcat'], test["cats"][i]['dateofbirth'], test["cats"][i]['dateofdeath'], test["cats"][i]['reasonfordeath'], test["cats"][i]['lastupdated'],
			test["cats"][i]['dateadded'], test["cats"][i]['ribcage'], test["cats"][i]['leglength'], test["cats"][i]['lastvisit'], test["cats"][i]['disease'], test["cats"][i]['visible'] ))

		self.tree.bind("<Double-1>", self.OnDoubleClick)
		
		return
		
	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	 The list of prompts to be included in the App.
	def create_Window(self):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.windowTitle);
		self.root.resizable(width=False, height=False)
		self.setOfWidgets = []

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

		Label(self.root, text="Breed:").grid(row=3, column=0, padx=0, pady=(15,0), sticky='nsew')
		global widgetBreed
		widgetBreed = ttk.Combobox(self.root, width=1, state="readonly", values = ["Feline", "American Bobtail", "Bengal", "Persian"])
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

		buttonFrame = Frame(self.root)
		buttonFrame.grid(row=13, column=0, columnspan=12, sticky='nsew')
		for i in range(0, 3):
			buttonFrame.grid_columnconfigure(i, weight=1)

		# AutoFill Button: generates sample inputs.
		searchButton = Button(buttonFrame, text="Search", command=self.Search, bg = "grey")
		searchButton.grid(row=0, column=0, padx=70, pady=(4,6), sticky='nsew')
		# Reset Button: resets all inputs.
		clearButton = Button(buttonFrame, text=" Reset  ", command=self.resetFields, bg = "grey")
		clearButton.grid(row=0, column=2, padx=70, pady=(4,6), sticky='nsew')

		#Label(self.root, text="Search Results:").grid(row=15, column=5, padx = 10 ,pady=(15,0), sticky='nsew')
		
		self.tree = ttk.Treeview(self.root, columns = (constColumns))
		self.tree.heading('#0', text='Owner ID')
		self.tree.heading('#1', text='Pet ID')
		self.tree.heading('#2', text='Name')
		self.tree.heading('#3', text='Breed')
		self.tree.heading('#4', text='Gender')
		self.tree.heading('#5', text='Weight')
		self.tree.heading('#6', text='Height')
		self.tree.heading('#7', text='Length')
		self.tree.heading('#8', text='Microchip')
		self.tree.heading('#9', text='Fitcat')
		self.tree.heading('#10', text='Date of Birth')
		self.tree.heading('#11', text='Date of Death')
		self.tree.heading('#12', text='Reason for Death')
		self.tree.heading('#13', text='Last Updated')
		self.tree.heading('#14', text='Date Added')
		self.tree.heading('#15', text='Ribcage')
		self.tree.heading('#16', text='Leg Length')
		self.tree.heading('#17', text='Last Visit')
		self.tree.heading('#18', text='Disease')
		self.tree.heading('#19', text='Visible')

		#adjustments for each of the displayed columns
		self.tree.column('#0', width = 65, minwidth = 40)
		self.tree.column('#1', width = 65, minwidth = 40)
		self.tree.column('#2', width = 80, minwidth = 40)
		self.tree.column('#3', width = 65, minwidth = 40)
		self.tree.column('#4', width = 65, minwidth = 40)
		self.tree.column('#5', width = 65, minwidth = 40)

		self.tree["displaycolumns"]=(constReducedColumns)

		self.treeScroll = ttk.Scrollbar(self.root, orient = 'vertical', command=self.tree.yview)
		self.tree.configure(yscroll=self.treeScroll.set)
		self.treeScroll.grid(row=16, column = 13, sticky='nsew', pady = 10)
		self.tree.grid(row=16, columnspan=12, sticky='nsew', pady = 10)
		self.treeview = self.tree

	# Presents the window instance to the user.
	def show_Window(self):
		self.root.mainloop();
		

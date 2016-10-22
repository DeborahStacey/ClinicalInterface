#!c:/Python34/python
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
class JsonApp:
	# Creates an Application instance.
	#	@param:  The name of the Application. 
	def __init__(self, title):
		self.windowTitle = title
		self.setOfWidgets = []
		self.clientWidgetCount = 0
		self.patientWidgetCount = 0

	# Creates prompts for the Application that the user can use to enter information.
	#	@param:  The frame object that the prompts will be placed into. 
	#			 The list of prompts with their repsecitve configurations.
	def newPrompts(self, frame, prompts):
		# Divide the frame into twelve equally-spaced columns.
		for x in range(0, 12):
			frame.grid_columnconfigure(x, weight=1)
		# Constructing each prompt with its own configuration and adding it to the frame.
		for i in prompts:
			# The number of widgets in the list within the current iteration.
			numOfWidgets = len(self.setOfWidgets)
			# Indices to each prompt's settings (configuration and extensions).
			inConfig = 2
			inExt = 8
			# Creates a horizontal line-break when the prompt is actally a "divider".
			if (i[0] == "--divider--"):
				tempLine = ttk.Separator(frame, orient="horizontal")
				tempLine.grid(row=i[1], column=i[2], columnspan=12, padx=3, pady=(6,0), sticky='nsew')
				continue
			if (i[0] != "--none--"):
				if (i[7]):
					newLabel = Label(frame, text=str(i[0]+"*:"))
				else:
					newLabel = Label(frame, text=str(i[0]+":"))
				newLabel.grid(row=i[2], column=i[3], padx=0, pady=(6,0), sticky='nsew')
			# If the prompt has no name, it's assumed as another widget for the previous one.
			else:
				inConfig = 1
				inExt = 6
			# Construction of the specified prompt (labelled and no-name)
			if (i[inConfig+4] == "text"):
				newWidget = Entry(frame)
				newWidget.grid(row=i[inConfig], column=i[inConfig+1]+1, rowspan=i[inConfig+2], 
									columnspan=i[inConfig+3], padx=(0,6), pady=(6,0), sticky='nsew')
			elif (i[inConfig+4] == "menu"):
				newWidget = ttk.Combobox(frame, width=10, state="readonly", values=i[inExt])
				newWidget.grid(row=i[inConfig], column=i[inConfig+1]+1, rowspan=i[inConfig+2], 
									columnspan=i[inConfig+3], padx=(0,6), pady=(6,0), sticky='nsew')
			elif (i[inConfig+4] == "spinbox-i"):
				newWidget = Spinbox(frame, from_=i[inExt][0], to=i[inExt][1], increment=i[inExt][2])
				newWidget.grid(row=i[inConfig], column=i[inConfig+1]+1, rowspan=i[inConfig+2], 
									columnspan=i[inConfig+3], padx=(0,6), pady=(6,0), sticky='nsew')	
				newWidget.delete(0, "end")
				newWidget.insert(0, 0)
			elif (i[inConfig+4] == "spinbox-f"):
				newWidget = Spinbox(frame, format="%.1f", from_=i[inExt][0], to=i[inExt][1], 
										increment=i[inExt][2])
				newWidget.grid(row=i[inConfig], column=i[inConfig+1]+1, rowspan=i[inConfig+2], 
									columnspan=i[inConfig+3], padx=(0,6), pady=(6,0), sticky='nsew')
				newWidget.delete(0, "end")
				newWidget.insert(0, 0)
			# The widgets associated with the prompts are stored for future JSON-assembly.
			#	- Prompts with no name, have their widgets included in the previous prompt.
			if (i[0] != "--none--"):
				self.setOfWidgets.append({"tag-name": i[1],"widget": [newWidget], "is-required": i[7]})
			else:
				self.setOfWidgets[numOfWidgets-1]["widget"].append(newWidget)

	# Creates prompts for the account-section of the Application.
	#	@param:  The list of account-related prompts with their repsecitve configurations.
	def newAccount(self, accountPrompts):
		tempFrame = Frame(self.root)
		self.newPrompts(tempFrame, accountPrompts)
		tempFrame.grid(row=0, column=0, columnspan=4, sticky='nsew')

	# Creates prompts for each patient-tab in the Notebook.
	#	@param:  The list of patient-related prompts with their repsecitve configurations.
	def newPatient(self, patientPrompts):
		tempFrame = Frame(self.root)
		self.newPrompts(tempFrame, patientPrompts)
		self.notebook.add(tempFrame, text=("Pet-"+str(len(self.notebook.tabs()))+""))

	# Removes the selected patient-tab from the Notebook (unless it's the only one).
	def removePatient(self):
		if (len(self.notebook.tabs()) > 1):
			self.notebook.forget(self.notebook.select())

	# Randomly enters information into the prompts for all sections.
	def autofill(self):
		print ("Auto-fill")
		return

	# Compiles an ordered-set of values from the set of widgets into a JSON-object.
	def submitProfile(self):
		# The master-list of values that is used to construct the JSON-object.
		setOfValues = OrderedDict()
		# Traversing the master-list of widgets and sending inputs to an ordered-set.
		for i in range(0, len(self.setOfWidgets)):
			# The index of the patient that is currently being added to the set.
			inPatient = int((i-self.clientWidgetCount) / self.patientWidgetCount)
			print (inPatient)
			# The parameters of the widget sets that are used to rettrieve information.
			paramName = self.setOfWidgets[i]["tag-name"]
			paramWidget = self.setOfWidgets[i]["widget"]
			paramState = self.setOfWidgets[i]["is-required"]
			# The account widgets are always handled before all other sections.
			if (i < self.clientWidgetCount):
				setOfValues.update({paramName: paramWidget[0].get()})
				for n in range(1, len(paramWidget)):
					setOfValues.update({paramName: " "+paramWidget[n].get()})
			# Separate sets are created for each tab (represents each patient).
			elif ((i-self.clientWidgetCount) % self.patientWidgetCount == 0):
				# Creates a new set for the next patient and their respective values.
				#	- If the account widgets were recently completed, create "Household" group.
				if (i == self.clientWidgetCount):
					setOfValues.update({"houseHold": [OrderedDict()]})
				else:
					setOfValues["houseHold"].append(OrderedDict())
				setOfValues["houseHold"][inPatient].update({paramName: paramWidget[0].get()})
				for n in range(1, len(paramWidget)):
					setOfValues["houseHold"][inPatient].update({paramName: " "+paramWidget[n].get()})
			# The patient widgets are grouped for each tab in the Notebook. 
			else:
				setOfValues["houseHold"][inPatient].update({paramName: str(paramWidget[0].get())})
				for n in range(1, len(paramWidget)):
					setOfValues["houseHold"][inPatient].update({paramName: " "+str(paramWidget[n].get())})
		# Create the JSON-File and exit the program.
		write_JsonFile("temp", setOfValues)
		self.root.destroy()

	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	 The list of prompts to be included in the App.
	def create_Window(self, accountPrompts, patientPrompts):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.windowTitle);
		self.root.resizable(width=False, height=False)
		# Organize the window into sections for easier layout management.
		for x in range(0, 4):
			self.root.grid_columnconfigure(x, weight=1)
		# Determines the number of valid prompts in each list.
		for i in accountPrompts:
			if (i[0] == "--divider--" or i[0] == "--none--"):
				continue
			self.clientWidgetCount += 1
		for i in patientPrompts:
			if (i[0] == "--divider--" or i[0] == "--none--"):
				continue
			self.patientWidgetCount += 1
		
		# Adding a starting patient-tab for the Application.
		self.newAccount(accountPrompts)
		# Horizontal line that separates this section and the next.
		tempLine1 = ttk.Separator(self.root, orient="horizontal")
		tempLine1.grid(row=1, columnspan=4, padx=0, pady=(6,0), sticky="nsew")
		# Creating a Notebook(Tabs) for the patients.
		self.notebook = ttk.Notebook(self.root)
		self.notebook.grid(row=2, column=0, columnspan=4, padx=(5,2), pady=6, sticky='nsew')
		# Adding a starting patient-tab for the Notebook.
		self.newPatient(patientPrompts)
		# Horizontal line that separates this section and the next.
		tempLine2 = ttk.Separator(self.root, orient="horizontal")
		tempLine2.grid(row=3, columnspan=4, padx=0, pady=(0,12), sticky="nsew")

		# Creates the "New Patient" button that inserts a new tab into the Notebook.
		addButton = Button(self.root, text="New Patient", command=lambda: self.newPatient(patientPrompts))
		addButton.grid(row=4, column=0, padx=12, pady=(0,6), sticky='nsew')
		# Creates the "Remove" button that removes the selected tab from the Notebook.
		removeButton = Button(self.root, text="Remove", command=self.removePatient)
		removeButton.grid(row=4, column=1, padx=12, pady=(0,6), sticky='nsew')
		# Creates the "Auto-Fill" button that generates values for all the prompts.
		autoFillButton = Button(self.root, text="Auto-Fill", command=self.autofill)
		autoFillButton.grid(row=4, column=2, padx=12, pady=(0,6), sticky='nsew')
		# Creates the "Register" button that generates the JSON-object and exits the program.
		registerButton = Button(self.root, text="Register", command=self.submitProfile)
		registerButton.grid(row=4, column=3, padx=12, pady=(0,6), sticky='nsew')

	# Presents the window instance to the user.
	def show_Window(self):
		self.root.mainloop();
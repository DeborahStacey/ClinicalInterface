#!c:/Python34/python
from tkinter import *
from tkinter import ttk
import json

# Generates JSON-file from the list of enteries.
#	@param:  The name of the JSON-file to be generated.
#			 The list of data to be included in the JSON-file.
def write_JsonFile(fileName, fileData):
	with open(fileName + ".json", "w") as outFile:
		json.dump(fileData, outFile)
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
	# The template of entries for the JSON-file.
	#		<household>: {
	#			<entry_01>: { <data> },
	#			<entry_02>: { <data> },
	#			<entry_03>: { <data> },
	#				and so on...
	tempJSON = {}

	# Creates an Application instance.
	#	@param:  The name of the Application. 
	def __init__(self, title):
		self.wm_title = title
		self.wm_height = 400
		self.wm_width = 500
		self.client_widgets = []
		self.patient_widgets = []
		self.patient_count = 1

# The Command Section of the JsonApp.
	def newSinglePrompt(self, prompt):
		return

	def newAccountPrompts(self, accountPrompts):
		accountFrame = Frame(self.root)
		for x in range(0, 6):
			accountFrame.grid_columnconfigure(x, weight=1)
		for i in accountPrompts:
			# newSinglePrompt(self, i)
			newLabel = Label(accountFrame, text=i[0])
			newLabel.grid(row=i[2], column=i[3], padx=0, pady=(6,0), sticky='nsew')
			newEntry = Entry(accountFrame)
			newEntry.grid(row=i[2], column=i[3]+1, columnspan=i[5]-1, padx=(0,6), pady=(6,0), sticky='nsew')
			self.client_widgets.append({"widget": [newEntry], "is-required": i[6]})
		accountFrame.grid(row=0, column=0, columnspan=4, sticky='nsew')

	def newPatientPrompts(self, patientPrompts):
		# Temproary set of widgets to be added to the list.
		tempWidgets = []
		# Create temporary Frame for the new Patient-tabe
		tempFrame = Frame(self.notebook)
		for x in range(0, 6):
			tempFrame.grid_columnconfigure(x, weight=1)
		for i in patientPrompts:
			if (i[0] == "--divider--"):
				tempLine = ttk.Separator(tempFrame, orient="horizontal")
				tempLine.grid(row=i[1], column=i[2], columnspan=6, padx=3, pady=(6,0), sticky='nsew')
				continue
			if (i[0] == "--none--"):
				continue
			newLabel = Label(tempFrame, text=i[0])
			newLabel.grid(row=i[2], column=i[3], padx=0, pady=(6,0), sticky='nsew')
			newEntry = Entry(tempFrame)
			newEntry.grid(row=i[2], column=i[3]+1, columnspan=i[5]-1, padx=(0,6), pady=(6,0), sticky='nsew')
			self.patient_widgets.append({"widget": [newEntry], "is-required": i[6]})
		tempFrame.grid(row=0, column=0, columnspan=4, sticky='nsew')

		# Add the temporary Frame to the Notebook
		self.notebook.add(tempFrame, text=("Pet-"+str(self.patient_count)))
		self.patient_count += 1

		print ("We are adding a tab")

	def remove_Patient(self):
		print ("We are removing a tab")
		return

	def submit_JsonApp(self):
		print ("We are submitting it all")
		for i in self.client_widgets:
			for j in i["widget"]:
				print (j.get())
		for i in self.patient_widgets:
			for j in i["widget"]:
				print (j.get())
		return

	def cancel_JsonApp(self):
		print ("We are cancelling it all")
		return

# The Interface Section of the JsonApp.
	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	 The list of prompts to be included in the App.
	def create_Window(self, accountPrompts, patientPrompts):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.wm_title);
		self.root.resizable(width=False, height=False)
		# Organize the window into sections for easier layout management.
		for x in range(0, 4):
			self.root.grid_columnconfigure(x, weight=1)
		
		# The HouseHold Prompt that is used to name the Json-file.
		self.newAccountPrompts(accountPrompts)

		# Horizontal line that separates this section and the next.
		tempLine1 = ttk.Separator(self.root, orient="horizontal")
		tempLine1.grid(row=1, columnspan=4, padx=0, pady=(6,0), sticky="nsew")

		# Creating a Notebook(Tabs) for the patients.
		self.notebook = ttk.Notebook(self.root)
		self.notebook.grid(row=2, column=0, columnspan=4, padx=(5,2), pady=6, sticky='nsew')
		# Adding a starting client-tab for the Notebook.
		self.newPatientPrompts(patientPrompts)

		# Horizontal line that separates this section and the next.
		tempLine2 = ttk.Separator(self.root, orient="horizontal")
		tempLine2.grid(row=3, columnspan=4, padx=0, pady=(0,12), sticky="nsew")

		# Add Button
		btnInsert = Button(self.root, text="Add", command=lambda: self.newPatientPrompts(patientPrompts))
		btnInsert.grid(row=4, column=0, padx=12, pady=(0,6), sticky='nsew')
		# Remove Button
		btnRemove = Button(self.root, text="Remove", command=self.remove_Patient)
		btnRemove.grid(row=4, column=1, padx=12, pady=(0,6), sticky='nsew')
		# Submit Button
		btnSubmit = Button(self.root, text="Submit", command=self.submit_JsonApp)
		btnSubmit.grid(row=4, column=2, padx=12, pady=(0,6), sticky='nsew')
		# Cancel Button
		btnCancel = Button(self.root, text="Cancel", command=self.cancel_JsonApp)
		btnCancel.grid(row=4, column=3, padx=12, pady=(0,6), sticky='nsew')

	# Presents the window instance to the user.
	def show_Window(self):
		# Positioning the window onto the center of the screen.
		p_x = (self.root.winfo_screenwidth() - self.wm_width) / 2
		p_y = (self.root.winfo_screenheight() - self.wm_height) / 2
		self.root.geometry('%dx%d+%d+%d' % (self.wm_width, self.wm_height, p_x, p_y))
		# Main event-based loop for the window.
		self.root.mainloop();
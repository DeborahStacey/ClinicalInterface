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
		self.client_widgets = []
		self.patient_widgets = []
		self.patient_count = 1

# The Command Section of the JsonApp.
	def newPrompts(self, frame, prompts):
		# Divide the frame into six equally-spaced columns for prompts.
		for x in range(0, 12):
			frame.grid_columnconfigure(x, weight=1)
		# Adding each prompt to their specified parameters.
		for i in prompts:
			#
			configIndex = 2
			extIndex = 8
			#
			numOfWidgets = len(self.patient_widgets)
			# If prompt is actually a divider, create a horizontal line.
			if (i[0] == "--divider--"):
				tempLine = ttk.Separator(frame, orient="horizontal")
				tempLine.grid(row=i[1], column=i[2], columnspan=12, padx=3, pady=(6,0), sticky='nsew')
				continue
			# Otherwise, add the specified prompt to the frame.
			if (i[0] != "--none--"):
				if (i[7]):
					tempLabel = Label(frame, text=str(i[0]+"*:"))
				else:
					tempLabel = Label(frame, text=str(i[0]+":"))
				tempLabel.grid(row=i[2], column=i[3], padx=0, pady=(6,0), sticky='nsew')
			else:
				configIndex = 1
				extIndex = 6
			#	
			if (i[configIndex+4] == "text"):
				tempWidget = Entry(frame)
				tempWidget.grid(row=i[configIndex], column=i[configIndex+1]+1, rowspan=i[configIndex+2], 
									columnspan=i[configIndex+3], padx=(0,6), pady=(6,0), sticky='nsew')
			elif (i[configIndex+4] == "menu"):
				tempWidget = ttk.Combobox(frame, width=10, state="readonly", values=i[extIndex])
				tempWidget.grid(row=i[configIndex], column=i[configIndex+1]+1, rowspan=i[configIndex+2], 
									columnspan=i[configIndex+3], padx=(0,6), pady=(6,0), sticky='nsew')
			elif (i[configIndex+4] == "spinbox-i"):
				tempWidget = Spinbox(frame, from_=i[extIndex][0], to=i[extIndex][1], increment=i[extIndex][2])
				tempWidget.grid(row=i[configIndex], column=i[configIndex+1]+1, rowspan=i[configIndex+2], 
									columnspan=i[configIndex+3], padx=(0,6), pady=(6,0), sticky='nsew')	
				tempWidget.delete(0, "end")
				tempWidget.insert(0, 0)
			elif (i[configIndex+4] == "spinbox-f"):
				tempWidget = Spinbox(frame, format="%.1f", from_=i[extIndex][0], to=i[extIndex][1], 
										increment=i[extIndex][2])
				tempWidget.grid(row=i[configIndex], column=i[configIndex+1]+1, rowspan=i[configIndex+2], 
									columnspan=i[configIndex+3], padx=(0,6), pady=(6,0), sticky='nsew')
				tempWidget.delete(0, "end")
				tempWidget.insert(0, 0)
			#
			if (i[0] != "--none--"):
				self.patient_widgets.append({"tag-name": i[1],"widget": [tempWidget], "is-required": i[7]})
			else:
				self.patient_widgets[numOfWidgets-1]["widget"].append(tempWidget)

	def newAccountPrompts(self, accountPrompts):
		# Temp-frame to be added to the GUI.
		tempFrame = Frame(self.root)
		self.newPrompts(tempFrame, accountPrompts)
		# Place the Account prompts on the top-section of the Application.
		tempFrame.grid(row=0, column=0, columnspan=4, sticky='nsew')

	def newPatientPrompts(self, patientPrompts):
		# Temp-frame to be added to the GUI.
		tempFrame = Frame(self.root)
		self.newPrompts(tempFrame, patientPrompts)
		# Place the Patient prompts in a new tab of the Notebook.
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
		self.root.mainloop();
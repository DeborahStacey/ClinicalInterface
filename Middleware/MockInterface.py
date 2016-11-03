#!c:/Python34/python
from collections import *
from tkinter import *
from tkinter import ttk
from random import *

from InputGenerator import *
from InputVariables import *
#from middleware import *

class MockInterface:
	# Creates a MockInterface Instance.
	# 	@param:		The Name of the Interface.
	#	@return:	None.
	def __init__(self, title):
		self.title = title
		self.setOfWidgets = None
		self.isDead = False
		self.hasKnownDeath = False

	# Toggles the TextArea widget depending on the "Reason Of Death?" checkbox.
	#	@param:		The TextArea widget that will be placed/removed.
	def toggleDeathWidget(self, widgetTextArea):
		if (not self.hasKnownDeath):
			widgetTextArea.grid(row=6, column=1, columnspan=11, padx=(0,6), pady=(6,0), sticky='nsew')
			self.hasKnownDeath = True
		else:
			widgetTextArea.delete(1.0, "end")
			widgetTextArea.grid_forget()
			self.hasKnownDeath = False
	
	# Toggles the entire Prompt for "Date of Date" depending on the "Deceased?" checkbox.
	#	@param:		The TextBar widget that will be enabled/disabled.
	#				The CheckBox widget that will be enabled/disabled.
	#				The TextArea widget that might be placed/removed.
	def toggleDeathState(self, widgetTextBar, widgetCheckBox, widgetTextArea):
		if (not self.isDead):
			widgetTextBar.config(state="normal")
			widgetCheckBox.config(state="normal")
			self.isDead = True
		else:
			widgetTextBar.delete(0, "end")
			widgetTextBar.config(state="disabled")
			widgetCheckBox.config(state="disabled")
			self.isDead = False
			# Remove the TextArea when the prompt becomes disabled.
			widgetTextArea.delete(1.0, "end")
			widgetTextArea.grid_forget()
			if (self.hasKnownDeath):
				widgetCheckBox.toggle()
				self.hasKnownDeath = False

	# Generates random input-values for all of the fields in the interface.
	def generateRecord(self):
		# OwnerID and PetID
		self.setOfWidgets[0].config(state="normal")
		self.setOfWidgets[0].delete(0, "end")
		self.setOfWidgets[0].insert(0, str(randCode()))
		self.setOfWidgets[0].config(state="disabled")

		self.setOfWidgets[1].config(state="normal")
		self.setOfWidgets[1].delete(0, "end")
		self.setOfWidgets[1].insert(0, str(randCode()))
		self.setOfWidgets[1].config(state="disabled")
		# General Pet-Information
		self.setOfWidgets[2].delete(0, "end")
		self.setOfWidgets[2].insert(0, str(randString(constName)))

		self.setOfWidgets[3].delete(0, "end")
		self.setOfWidgets[3].current(randint(0, len(self.setOfWidgets[3]["values"])-1))

		self.setOfWidgets[4].delete(0, "end")
		self.setOfWidgets[4].current(randint(0, len(self.setOfWidgets[4]["values"])-1))

		#
		dateBirth = str(randDateTime("1/1/2010", "12/31/2015", "%m/%d/%Y"))

		self.setOfWidgets[5].delete(0, "end")
		self.setOfWidgets[5].insert(0, dateBirth)

		if (self.isDead):
			self.setOfWidgets[6].delete(0, "end")
			self.setOfWidgets[6].insert(0, 
				str(randDateTime(dateBirth, "3/11/2016", "%m/%d/%Y")))

		if (self.hasKnownDeath):
			self.setOfWidgets[7].delete(1.0, "end")
			self.setOfWidgets[7].insert(1.0, str(randString(constDeaths)))
		# Specific Pet-Information
		self.setOfWidgets[8].delete(0, "end")
		self.setOfWidgets[8].insert(0, str(randint(1, 99)))

		self.setOfWidgets[9].delete(0, "end")
		self.setOfWidgets[9].insert(0, str(randint(1, 99)))

		self.setOfWidgets[10].delete(0, "end")
		self.setOfWidgets[10].insert(0, str(randint(1, 99)))
		# Date-Time Information
		dateAdded = str(randDateTime("2010-01-01 12:00:00", "2015-12-31 11:59:00", 
						"%Y-%m-%d %H:%M:%S"))

		self.setOfWidgets[11].config(state="normal")
		self.setOfWidgets[11].delete(0, "end")
		self.setOfWidgets[11].insert(0, 
			str(randDateTime(dateAdded, "2016-12-31 11:59:00", "%Y-%m-%d %H:%M:%S")))
		self.setOfWidgets[11].config(state="disabled")

		self.setOfWidgets[12].config(state="normal")
		self.setOfWidgets[12].delete(0, "end")
		self.setOfWidgets[12].insert(0, dateAdded)
		self.setOfWidgets[12].config(state="disabled")

	# Organizes all the input-values and sends them to the database.
	def submitRecord(self):
		#
		setOfValues = OrderedDict()
		#
		setOfValues.update({"ownerid": self.setOfWidgets[0].get()})
		setOfValues.update({"petid": self.setOfWidgets[1].get()})
		setOfValues.update({"name": self.setOfWidgets[2].get()})
		setOfValues.update({"breed": int(self.setOfWidgets[3].current())})
		setOfValues.update({"gender": int(self.setOfWidgets[4].current())})
		setOfValues.update({"microchip": True})
		setOfValues.update({"fitcat": False})
		setOfValues.update({"dateOfBirth": self.setOfWidgets[5].get()})
		setOfValues.update({"dateOfDeath": self.setOfWidgets[6].get()})
		setOfValues.update({"reasonOfDeath": self.setOfWidgets[7].get(1.0, "end")})
		setOfValues.update({"weight": float(self.setOfWidgets[8].get())})
		setOfValues.update({"height": float(self.setOfWidgets[9].get())})
		setOfValues.update({"length": float(self.setOfWidgets[10].get())})
		setOfValues.update({"dateUpdate": self.setOfWidgets[11].get()})
		setOfValues.update({"dateAdded": self.setOfWidgets[12].get()})
		#
		print (setOfValues)

	# Creates the Interface, along with all its required content.
	#	@param:		None.
	#	@return:	None.
	def createWindow(self):
		# Creating the root-frame of the interface.
		self.root = Tk()
		self.root.wm_title(self.title);
		# Restricting the user from resizing the interface.
		self.root.resizable(width=False, height=False)
		# Initializing our Set of Widgets to an empty list.
		self.setOfWidgets = []

		# Widgets for the OwnerID and PetID fields (disabled state).
		Label(self.root, text="Owner ID:").grid(row=0, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetOwnerID = Entry(self.root, state="readonly")
		widgetOwnerID.grid(row=0, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetOwnerID)

		Label(self.root, text="Pet ID:").grid(row=0, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetPetID = Entry(self.root, state="readonly")
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
		widgetBreed = ttk.Combobox(self.root, width=1, state="readonly", values=constBreed)
		widgetBreed.grid(row=3, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetBreed)
		
		Label(self.root, text="Gender:").grid(row=3, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetGender = ttk.Combobox(self.root, width=1, state="readonly", values=constGender)
		widgetGender.grid(row=3, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetGender)
		
		Label(self.root, text="Date of Birth:").grid(row=4, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateBirth = Entry(self.root)
		widgetDateBirth.grid(row=4, column=1, columnspan=8, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateBirth)
		#
		Label(self.root, text="Date of Death:").grid(row=5, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateDeath = Entry(self.root, state="disabled", textvariable="")
		widgetDateDeath.grid(row=5, column=1, columnspan=8, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateDeath)

		widgetKnownDeath = Text(self.root, width=10, height=3)
		self.setOfWidgets.append(widgetKnownDeath)
		#
		widgetHasKnownDeath = Checkbutton(self.root, state="disabled", text="Reason of Death?")
		widgetHasKnownDeath.grid(row=5, column=9, columnspan=3, sticky='ws')
		widgetHasKnownDeath.config(command=lambda:self.toggleDeathWidget(widgetKnownDeath))

		widgetIsDead = Checkbutton(self.root, text="Deceased?")
		widgetIsDead.grid(row=4, column=9, columnspan=3, sticky='ws')
		widgetIsDead.config(command=lambda:self.toggleDeathState(widgetDateDeath, widgetHasKnownDeath, widgetKnownDeath))

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=7, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# Widgets for the fields regarding specific information of the pet (enabled state).
		Label(self.root, text="Wt. (lbs):").grid(row=8, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetWeight = Entry(self.root, width=12)
		widgetWeight.grid(row=8, column=1, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetWeight)

		Label(self.root, text="Ht. (cm):").grid(row=8, column=5, padx=0, pady=(6,0), sticky='nsew')
		widgetHeight = Entry(self.root, width=12)
		widgetHeight.grid(row=8, column=6, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetHeight)

		Label(self.root, text="Len. (cm):").grid(row=8, column=9, padx=0, pady=(6,0), sticky='nsew')
		widgetLength = Entry(self.root, width=12)
		widgetLength.grid(row=8, column=10, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetLength)
		
		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=9, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# Widgets for the DateUpdated and DateAdded fields (disabled state).
		Label(self.root, text="Date Updated:").grid(row=10, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateUpdate = Entry(self.root, state="readonly")
		widgetDateUpdate.grid(row=10, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateUpdate)

		Label(self.root, text="Date Registered:").grid(row=10, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetDateAdded = Entry(self.root, state="readonly")
		widgetDateAdded.grid(row=10, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateAdded)

		# Horizontal line that separates the widgets as groups.
		ttk.Separator(self.root, orient="horizontal").grid(row=11, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# AutoFill Button: generates sample inputs.
		autofillButton = Button(self.root, text="AutoFill", command=self.generateRecord)
		autofillButton.grid(row=12, column=0, columnspan=6, padx=(12,6), pady=(4,6), sticky='nsew')
		# Submit Button: generates JSON files.
		submitButton = Button(self.root, text="Register", command=self.submitRecord)
		submitButton.grid(row=12, column=6, columnspan=6, padx=(6,12), pady=(4,6), sticky='nsew')

	# Destroys the Interface and all of its contents.
	# 	@param:		None.
	#	@return:	None.
	def destroyWindow(self):
		self.root.destroy();

	# Updates the Interface of all occurring events.
	# 	@param:		None.
	#	@return:	None.
	def update(self):
		#
		self.setOfWidgets[0].config(state="normal")
		self.setOfWidgets[0].delete(0, "end")
		self.setOfWidgets[0].insert(0, str(randCode()))
		self.setOfWidgets[0].config(state="disabled")

		self.setOfWidgets[1].config(state="normal")
		self.setOfWidgets[1].delete(0, "end")
		self.setOfWidgets[1].insert(0, str(randCode()))
		self.setOfWidgets[1].config(state="disabled")
		#
		dateAdded = str(randDateTime("2010-01-01 12:00:00", "2015-12-31 11:59:00", 
						"%Y-%m-%d %H:%M:%S"))

		self.setOfWidgets[11].config(state="normal")
		self.setOfWidgets[11].delete(0, "end")
		self.setOfWidgets[11].insert(0, 
			str(randDateTime(dateAdded, "2016-12-31 11:59:00", "%Y-%m-%d %H:%M:%S")))
		self.setOfWidgets[11].config(state="disabled")

		self.setOfWidgets[12].config(state="normal")
		self.setOfWidgets[12].delete(0, "end")
		self.setOfWidgets[12].insert(0, dateAdded)
		self.setOfWidgets[12].config(state="disabled")
		#
		self.root.mainloop();
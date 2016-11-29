#!c:/Python34/python
from collections import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import *

from InputGenerator import *
from InputVariables import *
from LoginInterface import *
from middleware import *

class MockInterface:
	# Creates a MockInterface Instance.
	# 	@param:		The Name of the Interface.
	#	@return:	None.
	def __init__(self, title):
		self.title = title
		self.setOfWidgets = None
		self.isDead = False
		self.hasKnownDeath = False

	# Updates the Breed Selection based on the selected Species.
	#	@param:		The Combobox widget that will be verified.
	#				The Combobox widget that will be updated.
	#	@return:	None.
	def updateBreedWidget(self, widgetSpecies, widgetBreeds):
		if (widgetSpecies.get() == ""):
			widgetBreeds.config(values=None)
		else:
			widgetBreeds.config(values=constBreeds[widgetSpecies.get()])

	# Toggles the TextArea widget depending on the "Reason Of Death?" checkbox.
	#	@param:		The TextArea widget that will be placed/removed.
	#	@return:	None.
	def toggleDeathWidget(self, widgetTextArea):
		if (not self.hasKnownDeath):
			widgetTextArea.grid(row=7, column=1, columnspan=11, padx=(0,6), pady=(6,0), sticky='nsew')
			self.hasKnownDeath = True
		else:
			widgetTextArea.delete(1.0, "end")
			widgetTextArea.grid_forget()
			self.hasKnownDeath = False
	
	# Toggles the entire Prompt for "Date of Date" depending on the "Deceased?" checkbox.
	#	@param:		The TextBar widget that will be enabled/disabled.
	#				The CheckBox widget that will be enabled/disabled.
	#				The TextArea widget that might be placed/removed.
	#	@return:	None.
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
	#	@param:		None.
	#	@return:	None.
	def autoPetInputs(self):
		# Generating information from the General-Information Section.
		self.setOfWidgets[0].delete(0, "end")
		self.setOfWidgets[0].insert(0, str(randString(constNames)))

		# Generate the species before the breed (since it's important).
		self.setOfWidgets[3].delete(0, "end")
		self.setOfWidgets[3].current(randint(0, len(self.setOfWidgets[3]["values"])-1))
		# Update the breed selection acordingly.
		self.updateBreedWidget(self.setOfWidgets[3], self.setOfWidgets[2])
		# Generate the breed after.
		self.setOfWidgets[2].delete(0, "end")
		self.setOfWidgets[2].current(randint(0, len(self.setOfWidgets[2]["values"])-1))

		self.setOfWidgets[4].delete(0, "end")
		self.setOfWidgets[4].current(randint(0, len(self.setOfWidgets[4]["values"])-1))
		self.setOfWidgets[5].delete(0, "end")
		self.setOfWidgets[5].current(randint(0, len(self.setOfWidgets[5]["values"])-1))

		# Generating information from the Date/Time Section.
		dateBirth = str(randDateTime("2008-1-1", "2015-12-31", "%Y-%m-%d"))

		self.setOfWidgets[6].delete(0, "end")
		self.setOfWidgets[6].insert(0, dateBirth)
		if (self.isDead):
			self.setOfWidgets[7].delete(0, "end")
			self.setOfWidgets[7].insert(0, str(randDateTime(dateBirth, "2016-12-1", "%Y-%m-%d")))
		if (self.hasKnownDeath):
			self.setOfWidgets[8].delete(1.0, "end")
			self.setOfWidgets[8].insert(1.0, str(randString(constDeathReasons)))

		# Generating information from the Statistics Section.
		self.setOfWidgets[9].delete(0, "end")
		self.setOfWidgets[9].insert(0, str("{0:.2f}".format(uniform(1.0, 99.0))))
		self.setOfWidgets[10].delete(0, "end")
		self.setOfWidgets[10].insert(0, str("{0:.2f}".format(uniform(1.0, 99.0))))
		self.setOfWidgets[11].delete(0, "end")
		self.setOfWidgets[11].insert(0, str("{0:.2f}".format(uniform(1.0, 99.0))))

	# Clears all normal input-fields.
	#	@param:		None.
	#	@return:	None.
	def clearPetInputs(self):
		# Compiling information from the General-Information Section.
		self.setOfWidgets[0].delete(0, "end")
		self.setOfWidgets[1].delete(0, "end")

		self.setOfWidgets[3].set("")
		self.setOfWidgets[2].set("")
		self.updateBreedWidget(self.setOfWidgets[2], self.setOfWidgets[1])

		self.setOfWidgets[4].set("")
		self.setOfWidgets[5].set("")

		# Compiling information from the Date/Time Section.
		self.setOfWidgets[6].delete(0, "end")
		self.setOfWidgets[7].delete(0, "end")
		self.setOfWidgets[8].delete(1.0, "end")

		# Compiling information from the Statistics Section.
		self.setOfWidgets[9].delete(0, "end")
		self.setOfWidgets[10].delete(0, "end")
		self.setOfWidgets[11].delete(0, "end")

		# Compiling information from the Extras Section.
		self.setOfWidgets[12].delete(1.0, "end")

	# Organizes all the input-values and sends them to the database.
	#	@param:		The option that determines the operation of the function.
	#	@return:	None.
	def sendPetInputs(self, userID, option):
		setOfValues = "{"
		# Compiling information from the login credentials.
		if (self.setOfWidgets[1].get() != ""):
			setOfValues += "\"petID\": " + str(self.setOfWidgets[1].get()) + ", "
		setOfValues += "\"owner\": \"" + str(userID) + "\", "

		# Compiling information from the General-Information Section.
		setOfValues += "\"name\": \"" + str(self.setOfWidgets[0].get()) + "\", "
		setOfValues += "\"animalTypeID\": " + str(self.setOfWidgets[3].current() + 1) + ", "
		setOfValues += "\"breed\": " + str(self.setOfWidgets[2].current() + 1) + ", "
		setOfValues += "\"gender\": " + str(int(self.setOfWidgets[4].current() / 2) + 1) + ", "

		if (self.setOfWidgets[4].current() % 2 == 1):
			setOfValues += "\"fixed\": \"true\", " 
		else:
			setOfValues += "\"fixed\": \"false\", "

		if (self.setOfWidgets[5].current() == 1):
			setOfValues += "\"outdoor\": \"true\", " 
		else:
			setOfValues += "\"outdoor\": \"false\", "

		if (self.setOfWidgets[5].current() == 0):
			setOfValues += "\"declawed\": \"true\", " 
		else:
			setOfValues += "\"declawed\": \"false\", "

		# Compiling information from the Date/Time Section.
		setOfValues += "\"dateOfBirth\": \"" + str(self.setOfWidgets[6].get()) + "\", "
		if (self.setOfWidgets[7].get() != ""):
			setOfValues += "\"dateOfDeath\": \"" + str(self.setOfWidgets[7].get()) + "\", "
		if (self.setOfWidgets[8].get(1.0, "end").strip() != ""):
			setOfValues += "\"reasonForDeath\": \"" + str(self.setOfWidgets[8].get(1.0, "end").strip()) + "\", "

		# Compiling information from the Statistics Section.
		setOfValues += "\"weight\": " + str(self.setOfWidgets[9].get()) + ", "
		setOfValues += "\"height\": " + str(self.setOfWidgets[10].get()) + ", "
		setOfValues += "\"length\": " + str(self.setOfWidgets[11].get()) 

		# Compiling information from the Extras Section.
		if (self.setOfWidgets[12].get(1.0, "end").strip() != ""):
			setOfValues += ", \"other\": \"" + str(self.setOfWidgets[12].get(1.0, "end").strip()) + "\"}"
		setOfValues +="}"
		# Send the JSON-string to the middleware for processing.
		if (option == "add" and not sendJson(str(setOfValues), option)):
			messagebox.showerror("Invalid Registration", "Registration Request could not be sent.")
		elif (option == "add"):
			messagebox.showinfo("Successful Registration", "Registration Request was successful.")
		if (option == "update" and not sendJson(str(setOfValues), option)):
			messagebox.showerror("Invalid Upadte", "Update Request could not be sent.")
		elif (option == "update"):
			messagebox.showinfo("Successful Update", "Update Request was successful.")

	# Creates the Login Interface and re-opens the PMS upon successful login.
	#	@param:		None.
	#	@return:	None.
	def createLoginPrompt(self):
		# Clear the current profile and open the login prompt.
		self.clearPetInputs()
		self.root.destroy()
		self.createWindow()

	# Creates the Interface, along with all its required content.
	#	@param:		None.
	#	@return:	None.
	def createWindow(self):
		# Attempt to login into the backend.
		loginApp = LoginInterface()
		loginApp.promptLogin()
		# Exit the program if the login prompt ends abruptly.
		if (not loginApp.getLoginStatus()):
			return 

		# Creating the root-frame of the interface.
		self.root = Tk()
		self.root.wm_title(self.title);
		# Restricting the user from resizing the interface.
		self.root.resizable(width=False, height=False)
		# Initializing our Set of Widgets to an empty list.
		self.setOfWidgets = []

		### GENERAL-INFORMATION SECTION
		# Standard TextField widget for the Pet's Name.
		Label(self.root, text="Name:").grid(row=0, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetPetName = Entry(self.root)
		widgetPetName.grid(row=0, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetPetName)
		# Standard TextField widget for the Pet's ID.
		Label(self.root, text="PetID:").grid(row=0, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetPetName = Entry(self.root)
		widgetPetName.grid(row=0, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetPetName)

		### GENERAL-INFORMATION (PET-SPECIFIC) SECTION
		ttk.Separator(self.root, orient="horizontal").grid(row=1, columnspan=12, padx=3, pady=(6,0), sticky='nsew')
		# Standard DropDown-List widget for the Pet's Breed (respective to Species).
		Label(self.root, text="Breed:").grid(row=2, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetBreed = ttk.Combobox(self.root, width=1, state="readonly")
		widgetBreed.grid(row=2, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetBreed)
		# Standard DropDown-List widget for the Pet's Species.
		Label(self.root, text="Species:").grid(row=2, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetSpecies = ttk.Combobox(self.root, width=1, state="readonly", values=constSpecies)
		widgetSpecies.grid(row=2, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		widgetSpecies.bind("<<ComboboxSelected>>", lambda e:self.updateBreedWidget(widgetSpecies, widgetBreed))
		self.setOfWidgets.append(widgetSpecies)
		# Standard DropDown-List widget for the Pet's Gender.
		Label(self.root, text="Gender:").grid(row=3, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetGender = ttk.Combobox(self.root, width=1, state="readonly", values=constGenders)
		widgetGender.grid(row=3, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetGender)
		# Standard DropDown-List widget for the Pet's LifeStyle.
		Label(self.root, text="LifeStyle:").grid(row=3, column=6, padx=0, pady=(6,0), sticky='nsew')
		widgetLifestyle = ttk.Combobox(self.root, width=1, state="readonly", values=constLifeStyles)
		widgetLifestyle.grid(row=3, column=7, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetLifestyle)

		### DATE/TIME SECTION
		ttk.Separator(self.root, orient="horizontal").grid(row=4, columnspan=12, padx=3, pady=(6,0), sticky='nsew')
		# Standard TextField widget for the Pet's Date of Birth.
		Label(self.root, text="Date of Birth:").grid(row=5, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateBirth = Entry(self.root)
		widgetDateBirth.grid(row=5, column=1, columnspan=8, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateBirth)
		# Standard TextField widget for the Pet's Date of Death.
		Label(self.root, text="Date of Death:").grid(row=6, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetDateDeath = Entry(self.root, state="disabled", textvariable="")
		widgetDateDeath.grid(row=6, column=1, columnspan=8, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetDateDeath)
		# Standard TextField widget for the Pet's Reason of Death.
		widgetKnownDeath = Text(self.root, width=10, height=3)
		self.setOfWidgets.append(widgetKnownDeath)

		# Toggle the TextField widget for the Pet's Reason of Death.
		widgetHasKnownDeath = Checkbutton(self.root, state="disabled", text="Reason of Death?")
		widgetHasKnownDeath.grid(row=6, column=9, columnspan=3, sticky='ws')
		widgetHasKnownDeath.config(command=lambda:self.toggleDeathWidget(widgetKnownDeath))
		# Toggle the TextField widget for the Pet's Date of Death.
		widgetIsDead = Checkbutton(self.root, text="Deceased?")
		widgetIsDead.grid(row=5, column=9, columnspan=3, sticky='ws')
		widgetIsDead.config(command=lambda:self.toggleDeathState(widgetDateDeath, widgetHasKnownDeath, widgetKnownDeath))

		### STATISTICS SECTION
		ttk.Separator(self.root, orient="horizontal").grid(row=8, columnspan=12, padx=3, pady=(6,0), sticky='nsew')
		# Standard TextField widget for the Pet's Weight.
		Label(self.root, text="Wt. (lbs):").grid(row=9, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetWeight = Entry(self.root, width=12)
		widgetWeight.grid(row=9, column=1, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetWeight)
		# Standard TextField widget for the Pet's Height.
		Label(self.root, text="Ht. (cm):").grid(row=9, column=5, padx=0, pady=(6,0), sticky='nsew')
		widgetHeight = Entry(self.root, width=12)
		widgetHeight.grid(row=9, column=6, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetHeight)
		# Standard TextField widget for the Pet's Length.
		Label(self.root, text="Len. (cm):").grid(row=9, column=9, padx=0, pady=(6,0), sticky='nsew')
		widgetLength = Entry(self.root, width=12)
		widgetLength.grid(row=9, column=10, columnspan=2, padx=(0,6), pady=(6,0), sticky='w')
		self.setOfWidgets.append(widgetLength)

		### EXTRAS SECTION
		ttk.Separator(self.root, orient="horizontal").grid(row=10, columnspan=12, padx=3, pady=(6,0), sticky='nsew')
		# Standard TextField widget for Other Information about the Pet.
		Label(self.root, text="Other:").grid(row=11, column=0, padx=0, pady=(6,0), sticky='new')
		widgetOther = Text(self.root, width=10, height=3)
		widgetOther.grid(row=11, column=1, columnspan=11, padx=(0,6), pady=(6,0), sticky='nsew')
		self.setOfWidgets.append(widgetOther)

		### BUTTON-PANEL SECTION
		ttk.Separator(self.root, orient="horizontal").grid(row=12, columnspan=12, padx=3, pady=(6,0), sticky='nsew')

		# Creating a separate frame for the buttons (for independant alignment).

		buttonTopFrame = Frame(self.root)
		buttonTopFrame.grid(row=13, column=0, columnspan=12, sticky='nsew')
		for i in range(0, 3):
			buttonTopFrame.grid_columnconfigure(i, weight=1)

		# AutoFill Button: generates sample inputs.
		autofillButton = Button(buttonTopFrame, text="AutoFill", command=self.autoPetInputs)
		autofillButton.grid(row=0, column=0, padx=(12,6), pady=(4,6), sticky='nsew')
		# Reset Button: resets all inputs.
		resetButton = Button(buttonTopFrame, text=" Reset  ", command=self.clearPetInputs)
		resetButton.grid(row=0, column=1, padx=(6,6), pady=(4,6), sticky='nsew')
		# Change-User Button: prompts the login interface.
		userButton = Button(buttonTopFrame, text=" Logout ", command=self.createLoginPrompt)
		userButton.grid(row=0, column=2, padx=(6,12), pady=(4,6), sticky='nsew')

		buttonBotFrame = Frame(self.root)
		buttonBotFrame.grid(row=14, column=0, columnspan=12, sticky='nsew')
		for i in range(0, 2):
			buttonBotFrame.grid_columnconfigure(i, weight=1)

		# Add Button: sends register requests.
		addButton = Button(buttonBotFrame, text="  Add ", command=lambda:self.sendPetInputs(loginApp.getUserName(), "add"))
		addButton.grid(row=0, column=0, padx=(12,6), pady=(4,6), sticky='nsew')
		# Update Button: sends updates.
		updateButton = Button(buttonBotFrame, text="Update", command=lambda:self.sendPetInputs(loginApp.getUserName(), "update"))
		updateButton.grid(row=0, column=1, padx=(6,12), pady=(4,6), sticky='nsew')

		# Updates the Interface of all occurring events.
		self.root.mainloop();
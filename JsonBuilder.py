#!/usr/bin/python
import Tkinter
from Tkinter import *
import json

##### The class definitions that support this script.

listOfButtons = []

# The Application class that is used to encapsulate the GUI object.
class App:
	# Creates an Application instance.
	#	@param: The name of the Application. 
	def __init__(self, title):
		self.wm_title = title
		self.wm_width = 300
		self.wm_height = 500
		self.wm_num = 0

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
		# Adding a divider and button for the main functionality.
		PanedWindow(self.root, orient=HORIZONTAL).grid(row=self.wm_num, column=0, sticky='ew')
		Button(self.root, text="Create JSON-Object")
		# Positioning the window onto the center of the screen.
		px = (self.root.winfo_screenwidth() - self.wm_width) / 2
		py = (self.root.winfo_screenheight() - self.wm_height) / 2
		self.root.geometry('%dx%d+%d+%d' % (self.wm_width, self.wm_height, px, py))
		# Main event-based loop for the window.
		self.root.mainloop();

	# Destroys the window instance.
	def destroy_Window(self):
		self.root.destroy()

	# Adds a custom text-field to the Application GUI.
	def add_Fields(self):
		#Variables
		listOfFields = ["Name", "Breed", "Gender", "Hi"]
		listOfDummy = ["Manga", "Norwegian Forest Cat", "Male"]
		count = 1

		def submit_Fields():
			for x in listOfButtons:
				inputText = x.get()
				print inputText

		def auto_Fill():
			for x in listOfButtons:
				inputText = x.insert(0, "dummy")
				#print listOfDummy[i]

		for x in listOfFields:
			# Adding Label to the left-side of the grid.
			name = Label(self.root, text=x)
			name.grid(row=count, column=0, padx=12, pady=0, sticky='nsew')
			# Adding Entry to the right-side of the grid.
			nameEntry = Entry(self.root)
			listOfButtons.append(nameEntry)
			nameEntry.grid(row=count, column=1, padx=12, pady=1, sticky='nsew')
			# Re-adjust the height of the window.
			count = count + 1

		# Submit Button
		b = Button(self.root, text="Submit", command=submit_Fields)
		b.grid(row=count, column=1, padx=12, pady=0, sticky='nsew')

		# Autofill Button with dummy input
		b2 = Button(self.root, text="Autofill", command=auto_Fill)
		b2.grid(row=count, column=0, padx=12, pady=0, sticky='nsew')

#
#	def sendJSON():
#		data = {
#			'name' : 'ACME',
#			'breed' : ,
#			'gender' : 542.23
#		}

		



# The JsonData class that is used to contain all relevant data.
# class JsonData:

###### The main execution of this script.

# Declaring an Application instance.
jsonGene = App("JSON Generator")
# Creating the Application interface.
jsonGene.create_Window()

jsonGene.add_Fields()

jsonGene.show_Window()
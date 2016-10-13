#!/usr/bin/python
import Tkinter
from Tkinter import *
import json

##### The class definitions that support this script.

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
	def add_TextField(self, tag_name, max_char):
		# Adding Label to the left-side of the grid.
		new_label = Label(self.root, text=tag_name)
		new_label.grid(row=self.wm_num, column=0, padx=12, pady=0, sticky='nsew')
		# Adding Entry to the right-side of the grid.
		new_entry = Entry(self.root)
		new_entry.grid(row=self.wm_num, column=1, padx=12, pady=1, sticky='nsew')
		# Re-adjust the height of the window.
		#self.wm_height += 21
		# Tracking the number of widgets.
		self.wm_num += 1;

# The JsonData class that is used to contain all relevant data.
# class JsonData:

###### The main execution of this script.

# Declaring an Application instance.
jsonGene = App("JSON Generator")
# Creating the Application interface.
jsonGene.create_Window()

jsonGene.add_TextField("Cat's Name", 20)
jsonGene.add_TextField("Cat's Breed", 20)
jsonGene.add_TextField("Cat's Gender", 20)

jsonGene.show_Window()
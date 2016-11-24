#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from collections import *
import json
from jsonTest import *

# The Application class that is used to encapsulate the GUI object.
class login:
	# Creates an Application instance.
	#	@param:  The name of the Application. 
	def __init__(self, title):
		self.windowTitle = title

	#login function that validates user credentials
	def loginFunction(self):
		#print (username.get() + "\n" + password.get() + "\n")
		#print (password.get())

		if (username.get() != "sameer" or password.get() != "password"):
			print ("Wrong password")
		else:
			print ("Correct")
			self.root.destroy()

	# Creates a non-resizable window instance (other variables are set separately).
	#	@param:	 The list of prompts to be included in the App.
	def create_Window(self):
		# Main root instance for the window.
		self.root = Tk()
		self.root.wm_title(self.windowTitle);
		self.root.geometry('300x300')
		self.root.resizable(width=False, height=False)

		Label(self.root, text="Username: ").grid(row=0, column=0, padx=(20), pady=(50,0), sticky='nsew')
		global username 
		username = Entry(self.root)
		username.grid(row=0, column=1, columnspan=5, padx=(0,6), pady=(50,0), sticky='nsew')
		#self.setOfWidgets.append(widgetOwnerID)

		Label(self.root, text="Password: ").grid(row=1, column=0, padx=0, pady=(6,0), sticky='nsew')
		global password
		password = Entry(self.root)
		password.grid(row=1, column=1, columnspan=5, padx=(0,6), pady=(6,0), sticky='nsew')

		# Search button that takes all input and constructs a JSON object to query to the database
		loginButton = Button(self.root, text="Sign In", command=self.loginFunction)
		loginButton.grid(row=2, column=0, columnspan=2, padx=(100,0), pady=(30), sticky='nsew')

	def show_Window(self):
		self.root.mainloop();

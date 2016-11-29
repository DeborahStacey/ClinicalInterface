#!c:/Python34/python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from middleware import *

class LoginInterface:
	# Creates a LoginInterface Instance.
	# 	@param:		The Name of the Interface.
	#	@return:	None.
	def __init__(self):
		self.loginUserName = ""
		self.loginStatus = False

	# Retrieves the username of the login credentials
	# 	@param:		None.
	#	@return:	The string that represents the username.
	def getUserName(self):
		return self.loginUserName

	# Identifies whether the login was successful/failure.
	# 	@param:		None.
	#	@return:	True, if successful. False, otherwise.
	def getLoginStatus(self):
		return self.loginStatus

	# Checks if the login credentials entered are valid to the backend.
	# 	@param:		The Label that will be used to notify the user.
	#				The TextArea of the UserName entered.
	#				The TextArea of the PassWord entered.
	#	@return:	None.
	def checkLogin(self, widgetFlavorText, widgetUserName, widgetPassWord):
		##### TO-DO: Implement the actual login-checking.
		if (widgetUserName.get() == "taha@mymail.com" and widgetPassWord.get() == "soccer123"):
			self.loginUserName = widgetUserName.get()
			self.loginStatus = True
			self.root.destroy()
		else:
			widgetFlavorText.config(text="Login failed. Try Again...")
			widgetUserName.delete(0, "end")
			widgetPassWord.delete(0, "end")

	# Creates the Interface, along with all its required content.
	#	@param:		None.
	#	@return:	None.
	def promptLogin(self):
		# Creating the root-frame of the interface.
		self.root = Tk()
		self.root.wm_title("Login Here");
		# Restricting the user from resizing the interface.
		self.root.resizable(width=False, height=False)
		for i in range(0, 2):
			self.root.grid_columnconfigure(i, weight=1)

		# Flavor Text that notifies to the user about the state of the login prompt.
		widgetFlavorText = Label(self.root, text="Please enter your login credentials:")
		widgetFlavorText.grid(row=0, column=0, columnspan=2, padx=0, pady=(6,0), sticky='nsew')
		ttk.Separator(self.root, orient="horizontal").grid(row=1, columnspan=2, padx=3, pady=(6,0), sticky='nsew')
		
		# Standard TextField widget for the UserName.
		Label(self.root, text="Username:").grid(row=2, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetUserName = Entry(self.root, width=25)
		widgetUserName.grid(row=2, column=1, columnspan=11, padx=(0,6), pady=(6,0), sticky='nsew')

		# Standard TextField widget for the PassWord.
		Label(self.root, text="Password:").grid(row=3, column=0, padx=0, pady=(6,0), sticky='nsew')
		widgetPassWord = Entry(self.root, width=25, show="*")
		widgetPassWord.grid(row=3, column=1, columnspan=11, padx=(0,6), pady=(6,0), sticky='nsew')
		ttk.Separator(self.root, orient="horizontal").grid(row=4, columnspan=2, padx=3, pady=(6,0), sticky='nsew')

		# Bind the TextAreas to the 'Enter' key for faster use.
		widgetUserName.bind("<Return>", lambda e:self.checkLogin(widgetFlavorText, widgetUserName, widgetPassWord))
		widgetPassWord.bind("<Return>", lambda e:self.checkLogin(widgetFlavorText, widgetUserName, widgetPassWord))

		# Creating a separate frame for the Login Button (for independant alignment).
		loginButton = Button(self.root, text="Login", command=lambda:self.checkLogin(widgetFlavorText, widgetUserName, widgetPassWord))
		loginButton.grid(row=5, column=0, columnspan=2, padx=(6,6), pady=(4,6), sticky='nsew')

		# Updates the Interface of all occurring events.
		self.root.mainloop();
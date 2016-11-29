#!/usr/bin/python3
from ClinicalGui import *
from login import *


# Declaring an Application interface and initializing all related variables.
interfaceApp = ClinicalGui("Clinical Interface")
loginApp = login("Login", 0)


# Open the login window
#loginApp.create_Window()
#temp = loginApp.show_Window()
#status = loginApp.get_loginStatus()

#if (status == True):
	# Open the Clinical Interface window
interfaceApp.create_Window()
interfaceApp.show_Window()
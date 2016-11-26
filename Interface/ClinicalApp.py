#!/usr/bin/python3
from ClinicalGui import *
from login import *


# Declaring an Application interface and initializing all related variables.
interfaceApp = ClinicalGui("Clinical Interface")
loginApp = login("Login")


# Assembling the Application interface and presenting it to the user.
loginApp.create_Window()
temp = loginApp.show_Window()

interfaceApp.create_Window()
interfaceApp.show_Window()
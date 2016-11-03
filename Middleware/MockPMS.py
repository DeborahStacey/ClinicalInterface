#!c:/Python34/python
from MockInterface import *

# Declaring an interface for the mock Practice-Managment-System.
mainApp = MockInterface("Mock Practice-Management-System (JSON)")
# Assembling the interface and checking for events.
mainApp.createWindow()
mainApp.update()
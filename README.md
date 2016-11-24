# Clinical Interface

##Description

The Clinical Interface team is in charge of creating systems for the use of clinicians wanting to add, update and search more advanced data in the wellcat database. The systems created include the Practice Management System Generator, Middleware, and the Clinical Interface. The Practice Management System (Mock PMS) is tasked with generating “dummy” data that we can use to test the functionality of our Middleware's API. The Middleware provides an interface that is tasked with receiving data and validating it in order to be inserted into the backend (database). Finally, the Clinical Interface is tasked with displaying a user friendly graphical interface that allows the clinicians to search for specific data stored within the backend. The Middleware, Practice Management System, and backend (provided by a different team) interact with each other in order to send and receive data, while the Clinical Interface interacts directly with the backend (with no direct association to the practice management system and the middleware).


## Version Information

* Currently works on Windows, Mac OS X, and Ubuntu
* Requires Python v.3.5
        * Python Requests library maybe need to be additionally installed  


## How to run the Mock PMS System: 
* We have provided a Mock PMS system as an example of how to integrate the middlware API with a system 
* Navigate to the middleware directory
* run `python3 MockPMS.py`

## How to run the Clinical interface 
* Navigate to the interface directory 
* run `python3 ClinicalApp.py`

## Middleware API 

| Function  | Use |
| ------------- | ------------- |
| convertJson(objName)  | Accepts a json obj file path, returns a json object in string format  | 
| sendJson(jsonString, action)  | Sends the jsonString to the middleware. Action needs to either be "add" or "update". Returns true on succesful creation/update of data in the backend, false on failure |
| checkJson(parsedObj) | Tests the object to ensure all values are valid before sending the parseObj to the database | 
| checkDate(date) | Checks the format of the date to ensure it matches standards |
| printError(flag, field) | Prints errors depending on the flag triggered |
| login(userEmail, password, parseObj) | Starts a login session with the users email and password, sends parsedObj after successful login complete |
| sendData(session, obj)| Validates session and sends data to backend |

## API example use 
```
message = convertJson("example.json")
status = sendJson(message,"add")
if(status == True):
	print ("Json object successfully sent")
else:
	print ("Error sending json obj")
```
	 

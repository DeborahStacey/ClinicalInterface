# Clinical Interface

* Currently works on Windows, Mac OS X, and Ubuntu
* Requires Python v.3.5
* We have provided a Mock PMS system as an example of how to use the middlware API 

## How to run the Mock PMS System: 
* Navigate to the Middleware Directory
* run `python3 MockPMS.py`

## How to run the Clinical interface 


## Middleware API 

| Function  | Use |
| ------------- | ------------- |
| convertJson(objName)  | Accepts a json obj file path, returns a json object in string format  | 
| sendJson(jsonString, action)  | Sends the jsonString to the middleware. Action needs to either be "add" or "update". Returns true on succesful creation/update of data in the backend, false on failure |
| checkJson(parsedObj) || Tests the object to ensure all values are valid before sending the parseObj to the database | 


## API example use 
```
message = convertJson("example.json")
status = sendJson(message,"add")
if(status == True):
	print ("Json object successfully sent")
else:
	print ("Error sending json obj")
```
	 

#!c:/Python34/python
from JsonApp import *

# A generalized compilation of all available speices (feline-only).
constSpecies = [
	"Feline"]
# A generalized compilation of all available breeds (feline-only).	
constBreed = [
	"Abyssinian", "American Bobtail", "American Curl",
	"American Shorthair", "American Wirehair", "Balinese",
	"Bengal", "Birman", "Bombay", "British Shorthair",
	"Burmese", "Burmilla", "Chartreux", "Chinese Li Hua",
	"Colorpoint Shorthair", "Cornish Rex", "Cymric",
	"Devon Rex", "Egyptian Mau", "European Burmese", "Exotic",
	"Havan Brown", "Himalayan", "Japanese Bobtail", "Javanese",
	"Korat", "LaPerm", "Maine Coon", "Manx", "Nebulung", 
	"Norwegian Forest", "Ocicat", "Oriental", "Persian",
	"Ragamuffin", "Ragdoll", "Russian Blue", "Savannah",
	"Scottish Fold", "Selkirk Rex", "Siamese", "Siberian",
	"Singapura", "Snowshoe", "Somali", "Sphynx", "Tonkinese",
	"Turkish Angora", "Turkish Van"]
# A generalized compilation of all available sexes.
constSex = [
	"Male", "Male(Neutered)", "Female", "Female(Spayed)"]
# A generalized compilation of all available age units.
constAge = [
	"Year(s)", "Month(s)", "Week(s)", "Day(s)"]

# A generalized list of prompts that are used in the Application.
listOfAccountPrompts = [
	["First Name:", "firstName", 0, 0, 1, 3, True, "text"],
	["Last Name:", "lastName", 0, 3, 1, 3, True, "text"],
	["E-Mail:", "eMail", 1, 0, 1, 6, True, "text"],
	["Address:", "address", 2, 0, 1, 6, False, "text"]]
listOfPatientPrompts = [
	["Name:", "name", 0, 0, 1, 6, True, "text"],
	["Species:", "species",	1, 0, 1, 3, True, "menu", constSpecies],
	["Gender:", "gender", 1, 3, 1, 3, True, "text"],
	["Breed:", "breed",	2, 0, 1, 3, True, "menu", constBreed],
	["Sex:", "sex",	2, 3, 1, 3, True, "text", constSex],
	["Color:", "color",	3, 0, 1, 6, False, "text"],
	["--divider--",	4, 0, 1, 6],

	["Age:", "age",	5, 0, 1, 2, True, "spinbox-i", [0, 99, 1], ""],
		["--none--", 5, 2, 1, 2, True, "menu", constAge],
	["Weight:", "weight", 5, 3, 1, 2, True, "spinbox-f", [0, 99, 0.1]],
	["Height:", "height", 6, 0, 1, 3, True, "spinbox-f", [0, 99, 0.1]],
	["Length:", "length", 6, 3, 1, 3, True, "spinbox-f", [0, 99, 0.1]],
	["--divider--",	7, 0, 1, 6],

	["MicroChip No:", "microchipNum", 8, 0, 1, 3, False, "text"],
	["Tag Number:", "tagNum", 8, 3, 1, 3, False, "text"]]

# Declaring an Application interface and initializing all related variables.
jsonGene = JsonApp("Mock Practice-Management-System (JSON)")
# Assembling the Application interface and presenting it to the user.
jsonGene.create_Window(listOfAccountPrompts, listOfPatientPrompts)
jsonGene.show_Window()
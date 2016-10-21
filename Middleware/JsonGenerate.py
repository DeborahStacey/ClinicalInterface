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

# A generalized list of prompts that are used in the Application.
listOfAccountPrompts = [
    ["First Name", "firstName", 0, 0, 1, 5, "text", True],
    ["Last Name", "lastName", 0, 6, 1, 5, "text", True],
    ["E-Mail", "eMail", 1, 0, 1, 11, "text", True],
    ["Address", "address", 2, 0, 1, 11, "text", False]]
listOfPatientPrompts = [
    ["Name", "name", 0, 0, 1, 11, "text", True],
    ["Species", "species", 1, 0, 1, 5, "menu", True, constSpecies],
    ["Gender", "gender", 1, 6, 1, 5, "text", True],
    ["Breed", "breed", 2, 0, 1, 5, "menu", True, constBreed],
    ["Sex", "sex", 2, 6, 1, 5, "menu", True, constSex],
    ["Color", "color", 3, 0, 1, 12, "text", False],
    ["--divider--", 4, 0, 1, 12],

    ["Age", "age", 5, 0, 1, 3, "spinbox-i", True, [0, 99, 1]],
        ["--none--", 5, 4, 1, 1, "menu", ["Year(s)", "Month(s)", "Week(s)", "Day(s)"]],
    ["Weight", "weight", 5, 6, 1, 3, "spinbox-f", True, [0, 99, 0.1]],
        ["--none--", 5, 10, 1, 1, "menu", ["kg", "g", "lbs", "oz"]],
    ["Height", "height", 6, 0, 1, 3, "spinbox-f", True, [0, 99, 0.1]],
        ["--none--", 6, 4, 1, 1, "menu", ["m", "cm", "ft", "in"]],
    ["Length", "length", 6, 6, 1, 3, "spinbox-f", True, [0, 99, 0.1]],
        ["--none--", 6, 10, 1, 1, "menu", ["m", "cm", "ft", "in"]],
    ["--divider--", 7, 0, 1, 12],

    ["Micro-Num", "microchipNum", 8, 0, 1, 5, "text", True],
    ["Tag-Num", "tagNum", 8, 6, 1, 5, "text", True],
    ["--divider--", 9, 0, 1, 12]]

# Declaring an Application interface and initializing all related variables.
jsonGene = JsonApp("Mock Practice-Management-System (JSON)")
# Assembling the Application interface and presenting it to the user.
jsonGene.create_Window(listOfAccountPrompts, listOfPatientPrompts)
jsonGene.show_Window()
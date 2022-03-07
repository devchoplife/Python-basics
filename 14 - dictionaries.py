# Dictionaries are used to store data values in key:value pairs
"""
Dictionaries have the folowing attributes 
- ordered 
- changeable 
- do not allow duplicates 
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values
# len() can be used to get the length of the dictionary
# values in a dictionary of can be of any data type
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

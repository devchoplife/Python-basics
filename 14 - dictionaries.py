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

# Access Dictionary Items
"""You can access the items of a dictionary by referring to its key name, inside square brackets:"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# the get() method will give the same result too
x = thisdict.get("model")

# the keys() method will return a list of all the keys in the dictionary
x = thisdict.keys()

# the values() method will return all the values in the dictionary
x = thisdict.values()

# the items() method will return ach items in a dictionary, as tuples in a list
x = thisdict.items()

# Checking if key exist
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Dictionary item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# using the update() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

# Add dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

"""The update() method will update the dictionary with the items from a given argument. 
If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs."""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

# Remove dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")  # removes item with the specified key name
print(thisdict)

# popitem() removes the last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# this will cause an error because "thisdict" no longer exists.
print(thisdict)

# The clear() method empties the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

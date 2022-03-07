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

# Loop Dictionaries
# Print all key names in the dictionary, one by one
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])

# You can also use the values() method to return values of a dictionary
for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
    print(x, y)

# Copy DIctionaries
"""
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to 
dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

"""Or, if you want to add three dictionaries into a new dictionary:"""
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

"""
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
"""
# Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple items
"""
Tuple items:
- are ordered: When we say that tuples are ordered, it means that the items have a defined order, 
and that order will not change.

- are unchangeable: Tuples are unchangeable, meaning that we cannot change, add or remove items 
after the tuple has been created.

- allow duplicate values 
- are indexed
"""
# len() is used to check tuple length
# Creating a tuple with one item, always remember the comma
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# A tuple can contain different data types
# the type() function returns the type of the tuple

# The tuple() constructor
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

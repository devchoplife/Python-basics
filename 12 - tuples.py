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

# Update tuples
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable 
as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, 
and convert the list back into a tuple.
"""
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Additems to a tuple
"""
Since tuples are immutable, they do not have a build-in append() method, but there are other 
ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it 
into a list, add your item(s), and convert it back into a tuple.
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
"""
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one 
item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove items
'''
Tuples are unchangeable, so you cannot remove items from it, but you can use the same 
workaround as we used for changing and adding tuple items:
'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Delete the tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists

# UNPACK TUPLES
# Unpacking a tuple
# WHen we creat e tuple, we normally assign a value to it. This is called "packing" a tuple.
fruits = ("apple", "banana", "cherry")  # packing

# We are also allowec the extract thevalues back ito vars. Called Unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits  # vars to unpack into

print(green)
print(yellow)
print(red)

# Using an asterisk (*)
"""
If the number of variables is less than the number of values, you can add an * to the 
variable name and the values will be assigned to the variable as a list:
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

"""
If the asterisk is added to another variable name than the last, Python will assign values 
to the variable until the number of values left matches the number of variables left.
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

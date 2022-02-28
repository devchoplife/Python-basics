"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:
"""

myList = ["apple", "banana", "cherry"]
print(myList)

# List items
"""
List items are 
- ordered: the lists have a defined order and that order will not change.new items are added 
to the end of the list. There are some list methods that will change the order of a list 
but generally the order of list items will not change.

- changeable: the list is changeable, meaning we can change, add, and remove tems in a list 
after it has been created .

- allow duplicate values: since lists are indexed, they can have items with the same value
- indexed
"""

# List length
myList = ["apple", "banana", "cherry"]
print(len(myList))

# List items - data types
# a list can contain different data tyoes and they can be of any data type
list1 = ["abc", 34, True, 40, "male"]

# THe list() constructor
# it is also possible to use the list() constructor when creating a new list
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a range of list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert items into list
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append items to a list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend list
# this appends elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add any iterable
# The extend() method does not have to append lists, you can add any
# iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove specified list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove specified index
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# the del keyword also removes the specified index as seen below
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# the del keyword can delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# LOOP LISTS
# Loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop through the index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping using a list comprehension
# list comprehension offers the shortest syntax for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

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
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
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


# LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# can be simplified with list comprehension to:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# List comprehension syntax
# The condition is like a filter that only accepts the items that valuate to True.
# newlist = [expression for item in iterable if condition == True]
# the iterable can be any iterable object like a list, tuple, set etc.
# You can also use range to create an iterable
newlist = [x for x in range(10)]
"""
The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:
"""
newlist = [x.upper() for x in fruits]
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]

# SORT LISTS
# Sort lists alphanumerically (ascending by default)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Customize the sort function e.g.


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case insensitive sort
"""
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
Luckily we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

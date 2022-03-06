"""
Sets have the following attributes:
- unordered 
- unchangeable 
- unindexed 
- do not allow duplicate values 
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

# len() can be used to get the length of a set
# Set items can be of any data type
set1 = {"abc", 34, True, 40, "male"}

# The set constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# Access set items
"""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified 
value is present in a set, by using the in keyword
"""
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# or
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Add set items
"""To add one item to a set use the add() method."""
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

"""To add items from another set into the current set, use the update() method."""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add any iterable
"""
The object in the update() method does not have to be a set, it can be any iterable 
object (tuples, lists, dictionaries etc.)
"""
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove set items
"""To remove an item in a set, use the remove(), or the discard() method."""
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# or

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# the difference between remove and discard is that if the item to remove does not exist
# remove will raise an error while discard will not raise an error

"""
You can also use the pop() method to remove an item, but this method will remove the 
last item. Remember that sets are unordered, so you will not know what item that gets 
removed.

The return value of the pop() method is the removed item.
"""
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

"""The clear() method empties the set"""
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""The del keyword will delete the set completely:"""
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# Joining sets
# Join two sets
"""
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both 
sets, or the update() method that inserts all the items from one set into another
"""
# The union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# The update() method inserts the items in set2 into set1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

"""Both union() and update() methods will exclude any duplicate items """

# Keep only the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)  # this returns a set with the duplicates
print(x)

# Keep all but not the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# returns a set with elements that are not duplicates
x.symmetric_difference_update(y)
print(x)

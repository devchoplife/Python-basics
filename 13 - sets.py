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

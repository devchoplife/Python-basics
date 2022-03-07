# THe break statement can also stop a loop based on a condition
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

"""With the continue statement we can stop the current iteration of the loop, and 
continue with the next:"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() function
"""To loop through a set of code a specified number of times, we can use the range() 
function,

The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number."""
for x in range(6):
    print(x)

"""The range() function defaults to 0 as a starting value, however it is possible to 
specify the starting value by adding a parameter: range(2, 6), which means values 
from 2 to 6 (but not including 6):"""
for x in range(2, 6):
    print(x)

"""The range() function defaults to increment the sequence by 1, however it is possible 
to specify the increment value by adding a third parameter: range(2, 30, 3)"""
for x in range(2, 30, 3):
    print(x)

# The else keyword in a for loop specifies a block of code to be executed when the
# loop is finished

# Note that the else block will not be executed if the loop is stopped by a break statement

# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error
for x in [0, 1, 2]:
    pass

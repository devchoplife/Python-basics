# Declaring vars
x = 5
y = "John"
print(x)
print(y)

# Casting - used to specify the data type of a var
X = str(3)
Y = int(3)
z = float(3)

# Get var type
print(type(x))
print(type(y))

# String vars can be declared either by using single or double quotes
a = "John"
# is the same as
b = 'John'

# Var names are case sensitive

# Legal Var names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel case
myVarName = "John"

# Pascal case
MyVarName = "John"

# Snake case
my_variable_name = "John"

# Multiple values to multiple variables
d, e, f = "Orange", "Banana", "Cherry"

# One value to multiple varia
g = h = i = "Orange"

# Unpack a collection
"""
If you have a collection of values in a list, tuple etc. Python allows you to extract 
the values into variables. This is called unpacking.
"""
fruits = ["apple", "banana", "cherry"]
k, l, m = fruits

# Output vars
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

# For numbers the + character works as a mathematical operator
# if you try to combine a string and a number, python will give you an error

# Global vars
x = 'awesome'


def myFunc():
    print("Python is " + x)


myFunc()

# if you use the global keyword, the var belongs to the global scope


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

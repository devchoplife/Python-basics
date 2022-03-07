# Creating a function
def my_function():
    print("hello from a function")


"""From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called."""

# Number of arguments
"""By default, a function must be called with the correct number of arguments.
Meaning that if your function expects 2 arguments, you have to call the function
with 2 arguments, not more, and not less."""

# Arbitrary arguments *args
"""If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items
accordingly:"""


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# kayword arguments
"""You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
"""


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

# Arbitrary keyword arguments **kwargs
"""If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items
accordingly:"""


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# Default Parameter Value
# If we call the function without argument, it uses the default value


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a list as an argument
"""You can send any data types of argument to a function (string, number, list,
dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the
function:"""


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return values from a function
# To let a function return a value, use the return statement


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement
"""function definitions cannot be empty, but if you for some reason have a function
definition with no content, put in the pass statement to avoid getting an error."""

# Recursion
"""Python also accepts function recursion, which means a defined function can call itself
Recursion is a common mathematical and programming concept. It means that a function
calls itself. This has the benefit of meaning that you can loop through data to reach
a result

The developer should be very careful with recursion as it can be quite easy to slip
into writing a function which never terminates, or one that uses excess amounts of
memory or processor power. However, when written correctly recursion can be a
very efficient and mathematically-elegant approach to programming"""


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

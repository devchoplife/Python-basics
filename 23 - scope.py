# Scope
"""A variable is only available from inside the region it is created. This is called scope."""

# Local Scope
"""A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function."""


def myfunc():
    x = 300
    print(x)


myfunc()

# Function inside a function
"""As explained in the example above, the variable x is not available outside the function, 
but it is available for any function inside the function:"""


def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()

# Global scope
"""A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local"""
x = 300


def myfunc():
    print(x)


myfunc()

print(x)

# Global keyword
"""If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global"""


def myfunc():
    global x
    x = 300


myfunc()

print(x)

# also use the global keyword if you want to make changes to a global var inside a function
x = 300


def myfunc():
    global x
    x = 200


myfunc()

print(x)

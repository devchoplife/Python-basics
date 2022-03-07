# Short Hand if
"""If you have only one statement to execute, you can put it on the same 
line as the if statement."""
a = 200
b = 33
if a > b:
    print("a is greater than b")

# Short Hand if-else
a = 2
b = 330
print("A") if a > b else print("B")

"""You can also have multiple else statements on the same line:"""
print("A") if a > b else print("=") if a == b else print("B")

# The pass statement
"""if statements cannot be empty, but if you for some reason have an if statement 
with no content, put in the pass statement to avoid getting an error."""
a = 33
b = 200

if b > a:
    pass


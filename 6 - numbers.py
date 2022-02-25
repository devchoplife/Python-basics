"""
There are 3 numeric types in pythn 

- int 
- float 
- complex
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Int 
"""
Int, or integer, is a whole number, positive or negative, without 
decimals, of unlimited length.
"""

# Float 
"""
Float, or "floating point number" is a number, positive or negative, 
containing one or more decimals.
"""

# Complex
"""
Complex numbers are written with a "j" as the imaginary part:
"""

# Type Conversion 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert int to float 
a = float(x)

# convert float to int 
b = int(y)

# convert int to complex 
c = complex(x)

# Generate Random number 
"""
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used 
to make random numbers:
"""
import random 
print(random.randrange(1, 10))
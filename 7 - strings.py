# assign string to a variable
a = "Hello"

# Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""  # single quotes also apply

# Strings are arrays
"""Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string."""

a = "Hello, World!!"
print(a[1])

# Looping through a string
for x in "banana":
    print(x)

# string length
a = "orange"
print(len(a))

# To check if a certain phrase or char is in a string
txt = "Thebest things in life are free"
print("free" in txt)  # this returns a bool

# or

if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
print("expensive" not in txt)

# or

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing strings 
b = "Hello, World!"
print(b[2:5])

# Slice from the start
b = "Hello, World!"
print(b[:5])

# Slice to the end
b = "Hello, World!"
print(b[2:])

# Negative indexing 
# use negative indexing to start the slice from the end of the string
# Slice from the start
b = "Hello, World!"
print(b[-5:-2]) 

# Modfy strings 
# Upper case 
a = "hello, World!"
print(a.upper())

# Lower case 
a = "hello, World!"
print(a.lower())

# Remove whitespace 
a = "hello, World!"
print(a.strip())

# Replace string 
a = "hello, World!"
print(a.replace('H', 'J'))

# Split string 
a = "hello, World!"
print(a.split(","))
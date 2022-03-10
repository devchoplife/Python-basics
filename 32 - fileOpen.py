# Open a file on the server
"""
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for 
reading the content of the file
"""
f = open("demofile.txt", "r")
print(f.read())

# or

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# Read only parts of the file
"""By default the read() method returns the whole text, but you can also specify 
how many characters you want to return"""
f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines
f = open("demofile.txt", "r")
print(f.readline())

# By calling readline() twice, you can read the first two lines
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Looping through the file to read the lines one by one
f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close files
f = open("demofile.txt", "r")
print(f.readline())
f.close()

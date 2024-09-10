# How to open  a file for reading in python.

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# line1 = f.readline() # Read the file line by line
# print(line1)

# f.close()

f = open("demo.txt","r")
line1 = f.read(10) # Passing parameter to the line thats starts from index 0.
print(line1)

f.close()

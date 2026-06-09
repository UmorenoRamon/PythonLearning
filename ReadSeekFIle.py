f1 = open("README.md", "r")
x1 = f1.read(15) # read first 15 characters
print(x1)
x = f1.read(10)  # read next 10 characters from current file position
print(x)

f1.seek(25) # seek is built in function which moves the file pointer
print(f1.read(5))
p = f1.tell() # tell is built in function which returns the current file pointer position
f1.close()
'''
f1 = open ("file1.txt", "r")
#x  = f1.read()
x = f1.read(10) # it will read first 10 characters of the file
f1.close()
print(x)
'''
# using with statement file gets closed automatically after the block of code is executed
with open ("file1.txt", "r") as f1:
    x = f1.read()
print(x)    
# the scope of variable x is outside the with block, so we can use it after the block as well.
# because the file is closed after the block, we cannot use f1 after the block. It will give an error.
# but more on the x scope is that it is not limited to the with block, it can be used outside the block as well. It is not a local variable to the block, it is a global variable in the script.
# with other branching statements like if, for, while, the scope of variables defined inside those blocks is limited to those blocks. But with with statement, the scope of variables defined inside the block is not limited to the block, it is global in the script.

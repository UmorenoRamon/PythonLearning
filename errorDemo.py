#Error which occurs at runtime is called as an exception.
#to handle exception in python, we have to use the keywords try and exception.
try:
    no = int(input("Enter any number "))
    print(no)
except ValueError:
    print("Please enter a valid integer.")

print("End of program")
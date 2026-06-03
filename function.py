'''
# This is a simple Python function that demonstrates how to define and use a function.
def greeting():
    print("Hello, World!")
    print("This function demonstrates basic function definition and usage in Python."
          " It can be called to execute the code within it.")
    print("Functions are reusable blocks of code that perform a specific task." )

print("Defining greeting function...")

# Calling the function to execute its code
greeting()
greeting()  # Calling it again to show that it can be reused
print("greeting function has been called and executed.")
'''

def greeting(name):
    print(f"Hello, {name}!")
    print("Good morning, everyone!")
    print("Have a great day!" )


greeting("Alice") # Calling the function with an argument to show that it can accept parameters and use them in its execution
greeting("Bob")  # Calling it again with a different argument to show that it can be reused with different inputs
print("greeting function has been called and executed with different names.")   

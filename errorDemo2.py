'''
dict1= {"name": "John", "age": 30, "city": "New York"}
print(dict1["name"])
print(dict1["age"])
print(dict1["phone"])
'''
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The sum is:", a + b)
    print("The product is:", a * b)
    print("The quotient is:", a / b)
    print("The difference is:", a - b)
except (ZeroDivisionError, ValueError):
    print("An error occurred. Please check your input and try again.")
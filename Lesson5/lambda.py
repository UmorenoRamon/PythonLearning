'''
def square(x):
    return x * x 
'''
s = lambda x: x * x

print(s(5))
'''
def greet(name):
    return 'Hello ' + name

print(greet('Alice'))
'''
greet = lambda name, message: 'Hello ' + name + ' ' + message
print(greet('Alice', 'Have a nice day'))
class Book:
    def __init__(self) :
        self.title = input("Enter the book title ")
        self.author = input("Enter the book author ")
        self.price = float(input("Enter the book price "))

    def __str__(self):
        return f"Book title {self.title} Author {self.author} Price {self.price}"
    
b1 = Book() # when we create the objects, the __init__ method gets called automatically
print(b1) # when we print the object, the __str__ method gets called automatically

b2 = Book()
print(b2)
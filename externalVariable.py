x = 20

def show():
    print("inside show() function, x =", x)

    def test():

    test()

print("before calling show() function, x =", x)
show()
print("after calling show() function, x =", x)

def f1():
    print("This is function 1")

def f2(fun1):
    fun1()
    print("This is function 2")

f2(f1)
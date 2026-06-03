def add(*a):
    total = 0
    for i in a:
        print("No ", i)
        total += i
    print("Sum is: ", total)

add(10,45,73)
add(10,45,73,100)
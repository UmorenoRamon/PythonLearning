def test(ch, no = 10): #default value for no is 10
    print("Character: ", ch)
    print("Number: ", no)
    print(ch*no)

test('A', 5) #positional arguments
test(ch = 'B', no = 3) #keyword arguments   
test("+", no = 4) #mixed arguments (positional and keyword)
test("#")
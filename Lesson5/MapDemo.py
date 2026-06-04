#map is used to map each used value from a collection to a predefined function
'''
def showsquare(no):
    return no * no

list1 = [1, 2, 3, 4, 5]

list2 = list(map(showsquare, list1))
print(list2)    

'''


list1 = [1, 2, 3, 4, 5]
list2 = list(map(lambda no: no * no, list1))
print(list2)
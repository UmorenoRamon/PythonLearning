list1 = [10, 63, 6, 7 , 24, 74, 75, 9, 10]
set1 = set(list1)
print(list1)
print(set1)

list2 = [] #empty list
for n in list1:
    if n not in list2:
        list2.append(n)

print(list2)
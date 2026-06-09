'''
list1 = [1, 2, 3, 4, 5]
# create another list having squares of each number from list

list2 = [x**2 for x in list1]
print(list2)

# list comprehension
# newlist = [expression for item in iterable if condition]

list2 = [n*n for n in list1]
print(list2)    
'''
'''
list1 = ["Megha", "Darren", "Igor", "Jess", "Ulises", "Zach", "Justin"]
list2 = []
for name in list1:
    list2.append(len(name))
print(list2)

# using list comprehension
list2 = [len(name) for name in list1]
print(list2)    
'''
# listofsalaries by paying 5% bonus for all employees
listoforiginalsalary = [10000, 20000, 30000, 40000, 50000]

listofsalafterbonus = [salary + (salary * 0.05) for salary in listoforiginalsalary]
'''
for salary in listoforiginalsalary:
    sal = salary + (salary * 0.05)
    listofsalafterbonus.append(sal)
'''
print(listofsalafterbonus)
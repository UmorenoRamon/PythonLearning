# dictionary is key:value pair
d1 = {1001: 45000, 1002: 55000, 1003: 60000}
'''
d2 = {}

for key in d1:
    d2[key] = d1[key] + d1[key] * 5 / 100
'''
'''
d2 = {key: d1[key] + d1[key] * 5 / 100 for key in d1}
print(d2)
'''
list1 = ["C", "C++", "Java", "Python", "JavaScript", "Go", "Rust", "Kotlin", "Swift", "Dart"]
d1 = {key: len(key) for key in list1}
print(d1)
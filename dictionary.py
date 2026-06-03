dict1 = {101: 'Alice', 102: 'Bob', 101: 'Charlie'}
print(dict1)  # Output: {101: 'Charlie', 102: 'Bob'}
print(dict1[102])  # Output: 'Bob'
print(dict1.keys())  # Output: dict_keys([101, 102]
print(dict1.values())  # Output: dict_values(['Charlie', 'Bob'])

for key in dict1:
    print(key, dict1[key])  # Output: 101 Charlie, 102 Bob
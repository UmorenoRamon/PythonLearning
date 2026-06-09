name = "Megha Sumant"
age = 34
address = "Pune"

print(name, age, address) #default separator is space
#print("Name : ", name, " Age : ", age, " Address : ", address)
print(f"Name : {name} Age : {age} Address : {address}") #f-string introduced after version 3.6
print("Name : {} Age: {} , Address : {}".format(name, age, address)) #format method
print(" {2}  {0}  {1}".format(name, age, address)) #format method

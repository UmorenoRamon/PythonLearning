'''
import pickle
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
f1 = open("data.pkl", "wb") # open a file in binary write mode
pickle.dump(data, f1) # write the data to the file
f1.close() # close the file 
'''
# using with statement to write data to a file using pickle
import pickle
with open("data.pkl", "rb") as f1:
    data = pickle.load(f1)
print(data)

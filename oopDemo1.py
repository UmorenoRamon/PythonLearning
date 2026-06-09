class Student:
    def setData(self):
        print("Hi from student")

    def showdata(self):
        print("Name:Megha")

#create the object;
s1=Student()
# to call function, we must call as objectnae.methodname()
s1.setData() #internally python will pass the object along with the function
s1.showdata()
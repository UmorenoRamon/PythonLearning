class Employee:
    def setdata(self, e, n ,s):
        self.empid = e
        self.empname = n
        self.salary = s

    def printdata(self):
        print(f"Employee ID {self.empid} Employee Name {self.empname} Salary {self.salary}")

e1 = Employee()
e1.setdata(101, "Megha", 50000)
e1.printdata()

e2 = Employee()
e2.setdata(102, "Pravin", 70000)
e2.printdata()
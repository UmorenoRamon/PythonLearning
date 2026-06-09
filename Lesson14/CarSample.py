class Car:
    def acceptData(self):
        self.model = input("Enter the car modell")
        self.price = float(input("Enter the car price"))
        self.color = input("Enter the car color")

    def showdata(self):
        print(f"Car model : {self.model} Price : {self.price}, Color: {self.color}")

#creating object
c1 = Car()
c2 = Car()
c3 = Car()

# call methods
c1.acceptData()
c2.acceptData()
c3.acceptData()

c1.showdata()
c2.showdata()
c3.showdata()

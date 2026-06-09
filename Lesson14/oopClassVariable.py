class Doctor:
    #class variable
    hospitalName = "Super Hospital"

    def __init__(self,did,dname,specialization):
        self.did = did
        self.dname = dname
        self.specialization = specialization

    def __str__(self):
        return f"{self.did} {self.dname} {self.specialization}"
    
print(Doctor.hospitalName) #to access class variable, classnae.classvariable
d1 = Doctor(1001, "Dr.Sam", "Orthopedic")
d2 = Doctor(1003, "Dr. Marsh", "Dentist")
print(d1)
print(d2)
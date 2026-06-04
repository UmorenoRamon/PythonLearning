from datetime import date

birth = date(1970, 11, 10)
today = date.today()

age = today.year - birth.year

print("Age: ", age)
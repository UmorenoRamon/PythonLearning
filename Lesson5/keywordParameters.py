def test(**kwargsies):
    for key, value in kwargsies.items():
        print(f"{key}: {value}")

test(name="Megha", age=25, city="Bangalore")
test(name="Rahul", age=30, salary="Mumbai", education="MS", birthdate="1990-01-01")
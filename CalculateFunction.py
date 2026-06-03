def Calculate(qty, price):
    bill = qty * price
    # print("The bill is: ", bill)
    return bill

qty = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
b = Calculate(qty, price)
print("The bill is: ", b)
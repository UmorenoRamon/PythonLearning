balance = 25000
amount = float(input("Enter the amount to be withdrawn: "))
if amount > balance:
    raise ValueError("Insufficient funds")
else:
    print(f"Withdrawal successful. Remaining balance: {balance}")

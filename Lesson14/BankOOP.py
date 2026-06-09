class BankAccount:
    def __init__(self):
        self.acno = int(input("Enter the account number "))
        self.acnmae = input("Enter the account holders name ")
        self.balance = float(input("Enter the initial balance "))

    # constructor with parameters
    def __init__(self, acno, acname, balance):
        self.acno = acno
        self.acnmae = acname
        self.balance = balance

    def __str__(self):
        return f"{self.acno} {self.acnmae} {self.balance}"
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Balance is less than withdraw amount! So cannot withdraw")
        self.balance = self.balance - amount
    
'''
b1 = BankAccount()
b2 = BankAccount()
b3 = BankAccount()


b1.deposit(3000)
b2.withdraw(500)


print(b1)
print(b2)
print(b3)
'''
accounts = []
while True:
    print("1. Create a new Bank account")
    print("2. Show all bank accounts ")
    print("3. Deposit amount in Bank account ")
    print("4. Withdraw amount from Bank account ")
    print("5. Check balance for any bank account ")
    print("6. Exit ")

    ch = int(input("Enter your chice "))
    if ch == 1:
        b1 = BankAccount()
        b1.acno = int(input("Enter the account number "))
        b1.acnmae = input("Enter the account holders name ")
        b1.balance = float(input("Enter the initial balance "))

        accounts.append(b1)

    elif ch == 2:
        for account in accounts:
            print(account)
    elif ch ==3:
        a = int(input("Enter the account number "))
        b = float(input("Enter the amount to deposit "))
        for acc in accounts:
            if acc.acno == a:
                acc.deposit(b)
                print("amount dposited succesfully ")

    elif ch == 4:
        a = int(input("Enter the account number "))
        b = float(input("Enter the amount to withdraw "))
        for acc in accounts:
            if acc.acno == a:
                acc.withdraw(b)
                print("amount withdrawn succesfully ")

    elif ch == 5:
        a = int(input("Enter the account number to check balance "))
        for acc in accounts:
            if acc.acno == a:
                print(acc.balance)

    elif ch == 6:
        break
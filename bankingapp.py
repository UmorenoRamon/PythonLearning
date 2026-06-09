# -----------------------------------
# USA BANKING SYSTEM - MINI PROJECT
# -----------------------------------

accounts = []  # list to store all bank accounts

# Lambda function to calculate annual interest (4%)
interest_calc = lambda balance: balance * 0.04

MIN_BALANCE = 100.0

# Create new bank account
def create_account():
    try:
        acc_no = 1001 + len(accounts)
        name = input("Enter customer name: ")
        balance = float(input("Enter initial deposit ($): "))

        if balance < MIN_BALANCE:
            raise ValueError("Minimum opening balance is $100")

        account = {
            "acc_no": acc_no,
            "name": name,
            "balance": balance,
            "currency": "USD"
        }

        accounts.append(account)
        print("\n✅ USA Bank Account Created Successfully")
        print(f"Account Number: {acc_no}")

    except ValueError as e:
        print("❌ Error:", e)

# Deposit money
def deposit():
    try:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount ($): "))

        if amount <= 0:
            raise ValueError("Deposit must be positive")

        for acc in accounts:
            if acc["acc_no"] == acc_no:
                acc["balance"] += amount
                print(f"✅ ${amount} deposited successfully")
                return

        print("❌ Account not found")

    except ValueError as e:
        print("❌ Error:", e)

# Withdraw money
def withdraw():
    try:
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount ($): "))

        for acc in accounts:
            if acc["acc_no"] == acc_no:
                if amount > acc["balance"]+100:
                    raise ValueError("Insufficient funds – overdraft not allowed")
                acc["balance"] -= amount
                print(f"✅ ${amount} withdrawn successfully")
                return

        print("❌ Account not found")

    except ValueError as e:
        print("❌ Error:", e)

# Check balance
def check_balance():
    try:
        acc_no = int(input("Enter account number: "))

        for acc in accounts:
            if acc["acc_no"] == acc_no:
                print(f"💵 Current Balance: ${acc['balance']}")
                return

        print("❌ Account not found")

    except ValueError:
        print("❌ Invalid account number")

# Calculate annual interest
def calculate_interest():
    try:
        acc_no = int(input("Enter account number: "))

        for acc in accounts:
            if acc["acc_no"] == acc_no:
                interest = interest_calc(acc["balance"])
                print(f"📈 Annual Interest: ${interest}")
                return

        print("❌ Account not found")

    except ValueError:
        print("❌ Invalid input")

# View all accounts (Bank Admin)
def view_accounts():
    if not accounts:
        print("❌ No accounts available")
        return

    print("\n--- USA Bank Account Details ---")
    for acc in accounts:
        print(
            f"Acc No: {acc['acc_no']} | "
            f"Name: {acc['name']} | "
            f"Balance: ${acc['balance']} | "
            f"Currency: {acc['currency']}"
        )

# -------------------------------
# MAIN MENU
# -------------------------------
while True:
    print("\n===== USA BANK MENU =====")
    print("1. Open Bank Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Calculate Annual Interest")
    print("6. View All Accounts (Admin)")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            calculate_interest()
        elif choice == 6:
            view_accounts()
        elif choice == 7:
            print("👋 Thank you for banking with USA Bank")
            break
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Please enter a valid number")

# -----------------------------------
# SHOPPING CART SYSTEM - MINI PROJECT
# -----------------------------------

cart = []   # list to store cart items

# Lambda function to calculate 10% discount
discount_calc = lambda total: total * 0.10


# Add item to cart
def add_item():
    try:
        name = input("Enter item name: ")
        price = float(input("Enter item price ($): "))
        quantity = int(input("Enter quantity: "))

        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        cart.append(item)
        print(f"\n✅ {name} added to cart successfully")

    except ValueError as e:
        print("❌ Error:", e)


# Remove item from cart
def remove_item():
    try:
        name = input("Enter item name to remove: ")

        for item in cart:
            if item["name"].lower() == name.lower():
                cart.remove(item)
                print(f"✅ {name} removed from cart")
                return

        print("❌ Item not found in cart")

    except ValueError as e:
        print("❌ Error:", e)


# View cart
def view_cart():
    if not cart:
        print("❌ Cart is empty")
        return

    print("\n--- Shopping Cart Details ---")
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        print(
            f"Item: {item['name']} | "
            f"Price: ${item['price']} | "
            f"Quantity: {item['quantity']} | "
            f"Subtotal: ${subtotal}"
        )


# Calculate total
def calculate_total():
    if not cart:
        print("❌ Cart is empty")
        return

    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]

    print(f"🛒 Total Bill: ${total}")


# Apply discount
def apply_discount():
    if not cart:
        print("❌ Cart is empty")
        return

    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]

    discount = discount_calc(total)
    final_total = total - discount

    print(f"🏷️ Discount: ${discount}")
    print(f"💳 Final Total after Discount: ${final_total}")


# Checkout
def checkout():
    if not cart:
        print("❌ Cart is empty")
        return

    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]

    print(f"\n🧾 Checkout Complete")
    print(f"Total Amount to Pay: ${total}")
    print("👋 Thank you for shopping with us!")


# -------------------------------
# MAIN MENU
# -------------------------------
while True:
    print("\n===== SHOPPING CART MENU =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Apply Discount")
    print("6. Checkout")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_cart()
        elif choice == 4:
            calculate_total()
        elif choice == 5:
            apply_discount()
        elif choice == 6:
            checkout()
        elif choice == 7:
            print("👋 Exiting Shopping Cart Program")
            break
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Please enter a valid number")
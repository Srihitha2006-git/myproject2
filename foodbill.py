canteen_menu = {
    1: {"item": "Tea", "price": 10},
    2: {"item": "Coffee", "price": 15},
    3: {"item": "Samosa", "price": 20}, 
    4: {"item": "Sandwich", "price": 50},
    5: {"item": "Burger", "price": 70}, 
    6: {"item": "Pizza", "price": 100},
    7: {"item": "Fries", "price": 40}, 
    8: {"item": "Ice Cream", "price": 60},
    9: {"item": "Cold Drink", "price": 30}, 
    10: {"item": "Chocolate", "price": 25}
}

def display_menu():
    print("\nCanteen Menu:")
    for key, value in canteen_menu.items():
        print(f"{key}. {value['item']} - ₹{value['price']}")

def main():
    print("Welcome to College Canteen Billing System")
    selected_items = {}
    
    while True:
        display_menu()
        choice = int(input("\nEnter item number (or 0 to finish): "))
        if choice == 0: break
        if choice in canteen_menu:
            qty = int(input(f"Enter quantity for {canteen_menu[choice]['item']}: "))
            selected_items[choice] = selected_items.get(choice, 0) + qty
        else:
            print("Invalid choice!")

    print("\nBill Summary:")
    total = sum(canteen_menu[choice]["price"] * qty for choice, qty in selected_items.items())
    for choice, qty in selected_items.items():
        print(f"{canteen_menu[choice]['item']} x {qty} = ₹{canteen_menu[choice]['price'] * qty}")
    print(f"Total: ₹{total}")
main()
def vending_machine():
    menu = {
        "1": {"name": "Coke", "price": 2.50, "stock": 8},
        "2": {"name": "Sparkling Water", "price": 2.40, "stock": 5},
        "3": {"name": "Water", "price": 1.00, "stock": 10},
        "4": {"name": "Orange Juice", "price": 1.80, "stock": 8},
        "5": {"name": "Lemozin", "price": 2.00, "stock": 8},
        "6": {"name": "Iced Tea", "price": 2.10, "stock": 8}
    }

    while True:
        print("\nWelcome to Reliovi's Vending Machine!")
        print("Here are the options:")

        # Display the options with stock
        for key, item in menu.items():
            stock_status = f"(Stock: {item['stock']})" if item['stock'] > 0 else "(Out of stock)"
            print(f"{key}. {item['name']} - ${item['price']:.2f} {stock_status}")

        # User selects the items
        selected_items = []
        for _ in range(3):
            choice = input("Select an item by number (or press Enter to stop selecting): ")
            if not choice:
                break
            if choice in menu:
                item = menu[choice]
                if item['stock'] > 0:
                    selected_items.append(item)
                    item['stock'] -= 1
                else:
                    print(f"Sorry, {item['name']} is out of stock.")
            else:
                print("Invalid choice. Please try again.")

        if not selected_items:
            print("You didn't select any items. Exiting...")
            break

        # Confirm selection
        print("\nYou have selected:")
        for item in selected_items:
            print(f"- {item['name']} - ${item['price']:.2f}")
        confirm = input("Do you want to proceed with the purchase? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Purchase canceled. Returning to main menu...")
            # Restock the items if canceled
            for item in selected_items:
                item['stock'] += 1
            continue

        # Calculate total price and add 20% VAT
        total_price = sum(item['price'] for item in selected_items)
        vat = total_price * 0.20
        total_price_with_vat = total_price + vat

        print(f"\nYour selected items:")
        for item in selected_items:
            print(f"- {item['name']} - ${item['price']:.2f}")
        print(f"Subtotal: ${total_price:.2f}")
        print(f"VAT (20%): ${vat:.2f}")
        print(f"Total (with VAT): ${total_price_with_vat:.2f}")

        # User pays
        while True:
            try:
                payment = float(input(f"Enter payment amount (must be at least ${total_price_with_vat:.2f}): "))
                if payment >= total_price_with_vat:
                    change = payment - total_price_with_vat
                    print(f"Payment accepted. Your change: ${change:.2f}")
                    break
                else:
                    print("Insufficient payment. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Print receipt
        print("\n--- Receipt ---")
        for item in selected_items:
            print(f"{item['name']} - ${item['price']:.2f}")
        print(f"Subtotal: ${total_price:.2f}")
        print(f"VAT (20%): ${vat:.2f}")
        print(f"Total: ${total_price_with_vat:.2f}")
        print(f"Paid: ${payment:.2f}")
        print(f"Change: ${change:.2f}")
        print("Thank you for your purchase!")
        print("-----------------")

        # Ask if the user wants to run the program again or terminate
        while True:
            run_again = input("\nWould you like to buy more beverages or end the program? (buy/end): ").strip().lower()
            if run_again == "buy":
                break
            elif run_again == "end":
                print("Thank you for choosing the Reliovi's vending machine. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'buy' to start again or 'end' to exit.")

vending_machine()
    
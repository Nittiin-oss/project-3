# Cafe Management System in Python

class Cafe:
    def __init__(self):
        # Menu with item: price
        self.menu = {
            "Coffee": 50,
            "Tea": 30,
            "Sandwich": 80,
            "Burger": 120,
            "Pasta": 150,
            "Cold Drink": 40
        }
        self.order = {}

    def show_menu(self):
        print("\n------ Cafe Menu ------")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        print("-----------------------\n")

    def take_order(self):
        while True:
            self.show_menu()
            item = input("Enter the item you want to order (or type 'done' to finish): ").title()
            
            if item.lower() == "done":
                break
            elif item in self.menu:
                qty = int(input(f"Enter quantity of {item}: "))
                if item in self.order:
                    self.order[item] += qty
                else:
                    self.order[item] = qty
                print(f"✅ {qty} x {item} added to order")
            else:
                print("❌ Item not available, please choose from the menu")

    def generate_bill(self):
        print("\n====== BILL ======")
        total = 0
        for item, qty in self.order.items():
            price = self.menu[item] * qty
            print(f"{item} x {qty} = ₹{price}")
            total += price
        print("-------------------")
        print(f"Total Amount: ₹{total}")
        print("===================\n")
        print("Thank you! Visit Again 😊")

# -------- Main Program --------
if __name__ == "__main__":
    cafe = Cafe()
    while True:
        print("\n--- Cafe Management System ---")
        print("1. Show Menu")
        print("2. Take Order")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            cafe.show_menu()
        elif choice == "2":
            cafe.take_order()
        elif choice == "3":
            cafe.generate_bill()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

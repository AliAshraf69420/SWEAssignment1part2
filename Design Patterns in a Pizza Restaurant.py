from abc import ABC, abstractmethod


class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InventoryManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


class Pizza:
    def __init__(self, base: str):
        self.base = base
        self.toppings = []
        if base == "Margherita":
            self.cost = 5.0
        elif base == "Pepperoni":
            self.cost = 6.0

    def add_topping(self, topping: str, cost: float):
        self.toppings.append(topping)
        self.cost += cost

    def get_description(self):
        return f"{self.base} pizza with {' and '.join(self.toppings)}"

    def get_cost(self):
        return self.cost


class PaymentStrategy:
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using PayPal.")


def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")


    while True:

        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        if pizza_choice == '1' and inventory_manager.check_and_decrement("Margherita"):
            pizza = Pizza("Margherita")
        elif pizza_choice == '2' and inventory_manager.check_and_decrement("Pepperoni"):
            pizza = Pizza("Pepperoni")
        else:
            print("Pizza unavailable or out of stock!")
            continue

       
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")
            
            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza.add_topping("Cheese", 1.0)
           
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza.add_topping("Olives", 0.5)
            
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza.add_topping("Mushrooms", 0.7)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

      
        payment_method = CreditCardPayment()
        payment_method.pay(pizza.get_cost())


        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()

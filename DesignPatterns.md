# Design Patterns
## Signleton Pattern
### Description
The Singleton pattern ensures that a class has only one instance
and provides a global point of access to it.

---
### Application
In this system, the Singleton pattern is applied to the 
InventoryManager class to ensure that there is only one instance 
managing the inventory.

---
### Before Applying the Pattern
Before applying the Singleton pattern, multiple instances of 
InventoryManager could be created, leading to inconsistent 
inventory management.

---
### After Applying the Pattern
The Singleton pattern ensures that there is only one instance of 
InventoryManager, providing consistent inventory management.

---
```Python
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
```
---
## Builder Pattern
### Description
The Builder pattern is used to construct a complex object step by 
step. It separates the construction of a complex object from its 
representation.

---
### Application
In this system, the Builder pattern is applied to create a Pizza 
object with various toppings.

---
### Before Applying the Pattern
Before applying the Builder pattern, the Pizza creation and 
topping addition were done directly in the main function, making 
the code less modular and harder to maintain.

---
### After Applying the Pattern
The Builder pattern improves maintainability and extensibility by
encapsulating the Pizza creation logic within the Pizza class.

---
### Code Snippet
```python
class Pizza:
    def __init__(self, base: str):
        self.base = base
        self.toppings = []
        self.cost = 5  # base cost

    def add_topping(self, topping: str, cost: float):
        self.toppings.append(topping)
        self.cost += cost

    def get_description(self):
        return f"{self.base} pizza with {' and '.join(self.toppings)}"

    def get_cost(self):
        return self.cost
```
---
## Strategy Pattern
### Description
The Strategy pattern defines a family of algorithms, encapsulates 
each one, and makes them interchangeable. It lets the algorithm 
vary independently from clients that use it.

---
### Application
In this system, the Strategy pattern is applied to implement 
different payment methods.

---
### Before Applying the Pattern
Before applying the Strategy pattern, the payment logic was 
hardcoded, making it difficult to add new payment methods.

---
### After Applying the Pattern
The Strategy pattern improves maintainability and extensibility 
by allowing new payment methods to be added without modifying 
existing code.

---
```python
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using PayPal.")
```
---
# Design Patterns and their implemintation of SOLID principles

## Singleton Pattern
### Single Responsibility Principle (SRP)
The Singleton pattern helps implement SRP by ensuring that there is only one instance of the InventoryManager class, which is responsible for managing the inventory.

### Open/Closed Principle (OCP)
The Singleton pattern aligns with OCP by allowing the InventoryManager class to be extended with new functionality without modifying its existing code.

### Dependency Inversion Principle (DIP)
The Singleton pattern aligns with DIP by ensuring that the InventoryManager class depends on abstractions rather than concrete implementations, promoting loose coupling.

---
## Builder Pattern
### Single Responsibility Principle (SRP)
The Builder pattern helps implement SRP by separating the construction of a complex object (Pizza) from its representation. Each class has a single responsibility.

### Open/Closed Principle (OCP)
The Builder pattern aligns with OCP by allowing new types of pizzas or toppings to be added without modifying existing code.

---
## Strategy Pattern
### Single Responsibility Principle (SRP)
The Strategy pattern helps implement SRP by separating the payment logic from the main function. Each payment method has its own class.

### Open/Closed Principle (OCP)
The Strategy pattern aligns with OCP by allowing new payment methods to be added without modifying existing code.

### Dependency Inversion Principle (DIP)
The Strategy pattern aligns with DIP by depending on abstractions (PaymentStrategy) rather than concrete implementations (CreditCardPayment, PayPalPayment).

---
#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize internal storage for the property
        self._discount = 0
        
        # Setter handles validation automatically during initialization
        self.discount = discount
        
        # Initialize instance attributes
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # --- Properties ---
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer and between 0 and 100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # --- Methods ---
    def add_item(self, item, price, quantity):
        # Add total price (price * quantity) to the running total
        self.total += price * quantity
        
        # Add the item identifier to the items list
        self.items.append(item)
        
        # Record transaction object (dictionary) to history
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # If no items have been transacted, display message
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        
        # Apply discount as a percentage off the total
        self.total -= self.total * (self.discount / 100)

    def void_last_transaction(self):
        # Guard clause if there are no transactions to void
        if not self.previous_transactions:
            return
        
        # Remove and retrieve the last transaction dictionary
        last_transaction = self.previous_transactions.pop()
        
        # Ensure price reflects correctly by reversing the added item cost
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        
        # Ensure items reflects correctly by removing the item name
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self._last_transaction_amount = amount
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self._last_transaction_amount
        self._last_transaction_amount = 0

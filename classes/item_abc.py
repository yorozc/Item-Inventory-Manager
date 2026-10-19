from abc import ABC, abstractmethod
import re

class Item(ABC):

    # TODO: add more attributes if needed
    def __init__(self, name: str, price: float, quantity: int, description: str | None = None):
        self._id = None
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    @property
    def id(self):
        return self._id

    @id.setter 
    def id(self, _id):
        self._id = _id

    # name validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self._name = name.strip()

    # price validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        try:
            price = float(price)

        except (TypeError, ValueError):
            raise ValueError("ERROR: Price must be a number.")

        if price < 0 :
            raise ValueError("ERROR: Price cannot be negative.")

        self._price = price

    # quantity validation
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        try:
            quantity = int(quantity)

        except (TypeError, ValueError):
            raise ValueError("Quantity must be a number.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._quantity = quantity

    # description validation
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if description is not None and not isinstance(description, str):
            raise TypeError("Description must be a string or None")
        
        self._description = description

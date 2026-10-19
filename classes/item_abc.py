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
        if isinstance(price, int):
            price = float(price)

        if isinstance(price, str):
            # check if str fits a regex
            pattern = re.compile(r"[0-9]*\.[0-9]+", re.IGNORECASE)
            matched_ptrn = pattern.match(price)
            price = float(matched_ptrn.group(0))

        if not isinstance(price, float):
            raise TypeError("Price must be a float.")

        if price < 0 :
            raise ValueError("Price cannot be negative.")

        self._price = price

    # quantity validation
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, str):
            pattern = re.compile(r"[0-9]+", re.IGNORECASE)
            matched_ptrn = pattern.match(quantity)
            quantity = int(matched_ptrn.group(0))

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an int.")

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

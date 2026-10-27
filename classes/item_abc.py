from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP

class Item(ABC):

    def __init__(self, name: str, category: str, cost_price: float, retail_price: float, quantity: int, description: str | None = None):
        self._id = None
        self.name = name
        self.category = category
        self.cost_price = cost_price
        self.retail_price = retail_price
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

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        pass

    # cost price validation
    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, price):
        try:
            raw_price = Decimal(price)
            price = float(raw_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

        except (TypeError, ValueError):
            raise ValueError("ERROR: Price must be a number.")

        if price < 0 :
            raise ValueError("ERROR: Price cannot be negative.")

        self._cost_price = price

    # retail price validation
    @property
    def retail_price(self):
        return self._retail_price

    @retail_price.setter
    def retail_price(self, price):
        try:
            raw_price = Decimal(price)
            price = float(raw_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

        except (TypeError, ValueError):
            raise ValueError("ERROR: Price must be a number.")

        if price < 0 :
            raise ValueError("ERROR: Price cannot be negative.")

        self._retail_price = price

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

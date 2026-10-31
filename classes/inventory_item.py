from classes.item_abc import Item

class InventoryItem(Item):
    def __init__(self,  name, profile, category, cost_price, retail_price, quantity, description):
        super().__init__( name, profile, category, cost_price, retail_price, quantity, description)

    def __repr__(self):
        return f"{self.name} costs {self.price} and has a quantity of {self.quantity}."

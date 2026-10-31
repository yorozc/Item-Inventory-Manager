from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

class ItemRepository:
    def __init__(self):
        create_table() # creates inventory table if it doesn't exist
        self._db = "inventory.db" 
        self._columns = ["name", "category", "cost_price", "retail_price", "quantity", "description"]

    # ITEM RELATED FUNCTIONS

    def add_item(self, item: InventoryItem) -> None:
        query = f"""
                INSERT INTO {self.profile} (name, category, cost_price, retail_price, quantity, description) VALUES (?, ?, ?, ?, ?, ?)
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (item.name, item.category, item.cost_price, item.retail_price, item.quantity, item.description)) 

            item.id = c.lastrowid

    # TODO: use LIKE instead of id
    def del_from_db(self, id: int):
        query = f"""
                DELETE FROM {self.profile} WHERE id = ?;
                """
        
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            cursor = c.execute(query, (id,))
            if cursor.rowcount == 0:
                raise Exception(f"Item with id {id} does not exist.")

    # TODO: use like instead of id
    def edit_item(self, column: str, value: str, id: int):

        if column not in self._columns:
            raise Exception(f"Invalid property: {column}. Allowed: {', '.join(self._columns)}")
        
        query = f"""
                UPDATE {self.profile}
                SET {column} = ?
                WHERE id = ?;
                """
        
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (value, id))

    # allow for fuzzy matching using LIKE
    def get_item(self, id: int):
        query = f"""
                SELECT * FROM {self.profile} WHERE id = ?;
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (id,))

            data = c.fetchone()

        if data != None:
            return data

    def get_all_items(self) -> list:
        query = f"""
                SELECT * FROM {self.profile};
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query)

            inv_data = c.fetchall()

        return inv_data
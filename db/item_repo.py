from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

class ItemRepository:
    def __init__(self):
        create_table() # creates inventory table if it doesn't exist
        self._db = "inventory.db"
        self._table = "" # preparing for inventory profile feature
        self._columns = ["name", "price", "quantity", "description"]

    def add_item(self, item: InventoryItem) -> None:
        query = """
                INSERT INTO inventory (name, price, quantity, description) VALUES (?, ?, ?, ?)
                """
        with sqlite3.connect(self._db) as conn: # commits and closes 
            c = conn.cursor()
            c.execute(query, (item.name, item.price, item.quantity, item.description)) 

            item.id = c.lastrowid

        
    def del_from_db(self, id: int):
        query = """
                DELETE FROM inventory WHERE id = ?;
                """
        
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            cursor = c.execute(query, (id,))
            if cursor.rowcount == 0:
                raise Exception(f"Item with id {id} does not exist.")

    def edit_item(self, column, value, id):

        if column not in self._columns:
            raise Exception(f"Invalid property: {column}. Allowed: {', '.join(self._columns)}")
        
        query = f"""
                UPDATE inventory
                SET {column} = ?
                WHERE id = ?;
                """
        
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (value, id))

    def get_item(self, id: int):
        query = """
                SELECT * FROM inventory WHERE id = ?;
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (id,))

            data = c.fetchone()

        if data != None:
            return data

    def get_all_items(self) -> list:
        query = """
                SELECT * FROM inventory;
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query)

            inv_data = c.fetchall()

        return inv_data
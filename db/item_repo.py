from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

# TODO: add error checking for del, and check items

class ItemRepository:
    def __init__(self):
        # creates inventory table if it doesn't exist
        create_table()
        self._db = "inventory.db"

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
            c.execute(query, (id,))

    def edit_item(self, id):
        pass

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
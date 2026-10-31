from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

class DBRepository:
    def __init__(self):
        create_table() # creates inventory table if it doesn't exist
        self._db = "inventory.db" 
        self._columns = ["name", "category", "cost_price", "retail_price", "quantity", "description"]
        self.profile = "default" # default: inventory
        self._profiles = self.show_all_profiles()
        
    # ITEM RELATED FUNCTIONS

    def add_item(self, item: InventoryItem) -> None:
        query = f"""
                INSERT INTO inventory (name, profile, category, cost_price, retail_price, quantity, description) VALUES (?, ?, ?, ?, ?, ?, ?)
                """
        item.profile = self.profile
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (item.name, item.profile, item.category, item.cost_price, item.retail_price, item.quantity, item.description)) 

            item.id = c.lastrowid

    # TODO: use LIKE instead of id
    def del_from_db(self, id: int):
        query = f"""
                DELETE FROM inventory WHERE id = ?;
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
                UPDATE inventory
                SET {column} = ?
                WHERE id = ?;
                """
        
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (value, id))

    # TODO:  use LIKE instead of id
    def get_item(self, id: int):
        query = f"""
                SELECT * FROM inventory WHERE id = ?;
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (id,))

            data = c.fetchone()

        if data != None:
            return data

    def get_all_items(self) -> list:
        query = f"""
                SELECT * FROM inventory;
                """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query)

            inv_data = c.fetchall()

        return inv_data

    @property
    def profile(self):
        return self._profile

    # TODO: add more error checking
    @profile.setter
    def profile(self, profile: str):
        
        self._profile = profile

    def create_profile(self, profile: str):
        query = """
            INSERT INTO profiles (name) VALUES (?);
        """
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor() 

            # create profile and switch 
            c.execute(query, (profile))

        self.profile = profile

    def switch_profile(self, profile_name: str):
        self._profiles = self.show_all_profiles()

        if profile_name not in self._profiles:
            raise ValueError("Profile does not exist.")

        self.profile = profile_name
        print(f"Switched to profile: {self.profile}")

    def delete_profile(self, profile_name: str):
        query = f"""
                DELETE FROM profiles WHERE name = ?
                """
        
        # check protected tables
        if profile_name.startswith("sqlite_") or profile_name == "inventory":
            raise ValueError(f"Cannot delete table: {profile_name}")

        # check if table dropped is current table and switch to default if true
        if profile_name == self.profile:
            self.profile = "inventory"

        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query, (profile_name))

        self._profiles = self.show_all_profiles()
        
    def show_all_profiles(self):
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor() 
            c.execute("SELECT name FROM profiles;")
            tables = c.fetchall()
        
        return tables
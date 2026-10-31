from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

class ItemRepository:
    def __init__(self):
        create_table() # creates inventory table if it doesn't exist
        self._db = "inventory.db" 
        self._columns = ["name", "category", "cost_price", "retail_price", "quantity", "description"]
        self._profiles = self.show_all_profiles() # tables that exist within db (profiles)
        self.profile = "inventory" 

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

    # PROFILE RELATED FUNCTIONS

    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, profile: str):
        if profile not in self._profiles:
            raise Exception
        
        self._profile = profile

    def create_profile(self, profile: str):
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor() 

            # create profile and switch 

            c.execute(f""" CREATE TABLE IF NOT EXISTS {profile}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            cost_price REAL NOT NULL,
            retail_price REAL NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 0,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        
            self._profiles = [row[0] for row in c.fetchall()]

    def switch_profile(self, profile_name: str):
        self._profiles = self.show_all_profiles()

        if profile_name not in self._profiles:
            raise ValueError("Profile does not exist.")

        self.profile = profile_name
        print(f"Switched to profile: {self.profile}")

    def delete_profile(self, profile_name: str):
        query = f"""
                DROP TABLE {profile_name}
                """
        
        # check protected tables
        if profile_name.startswith("sqlite_") or profile_name == "inventory":
            raise ValueError(f"Cannot delete table: {profile_name}")

        # check if table dropped is current table and switch to default if true
        if profile_name == self.profile:
            self.profile = "inventory"

        with sqlite3.connect(self._db) as conn:
            c = conn.cursor()
            c.execute(query)

        self._profiles = self.show_all_profiles()
        
    def show_all_profiles(self):
        with sqlite3.connect(self._db) as conn:
            c = conn.cursor() 
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in c.fetchall()]
        
        return tables
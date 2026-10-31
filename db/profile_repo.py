# PROFILE RELATED FUNCTIONS

from db.db_conn import create_table
import sqlite3

class ProfileRepository:
    def __init__(self):
        self._db = "inventory.db"
        self._profiles = self.show_all_profiles()
        self.profile = "inventory" 

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
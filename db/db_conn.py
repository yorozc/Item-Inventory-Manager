import sqlite3

def create_table():
    # creates db
    conn = sqlite3.connect('inventory.db')

    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS profiles(
        name TEXT PRIMARY KEY
        );
    """)

    c.execute(""" CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile TEXT NOT NULL,
    name TEXT NOT NULL,
    category TEXT,
    cost_price REAL NOT NULL,
    retail_price REAL NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(profile) REFERENCES profiles(name) ON DELETE CASCADE
    );
    """)

    # create table for logging 

    conn.commit()

    conn.close()
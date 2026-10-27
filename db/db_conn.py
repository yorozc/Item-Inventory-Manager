import sqlite3

def create_table():
    # creates db
    conn = sqlite3.connect('inventory.db')

    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    cost_price REAL NOT NULL,
    retail_price REAL NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
    );
    """)

    # create table for logging 


    conn.commit()

    conn.close()
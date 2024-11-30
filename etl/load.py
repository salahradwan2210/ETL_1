"""Data loading module."""
import sqlite3
import os

def init_database(db_path):
    """Initialize the SQLite database."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS covid_data (
            date TEXT,
            country TEXT,
            confirmed INTEGER,
            recovered INTEGER,
            deaths INTEGER,
            PRIMARY KEY (date, country)
        )
    ''')
    
    conn.commit()
    conn.close()

def load_data(records, db_path):
    """Load transformed data into the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    for record in records:
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO covid_data 
                (date, country, confirmed, recovered, deaths)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                record['date'],
                record['country'],
                record['confirmed'],
                record['recovered'],
                record['deaths']
            ))
        except sqlite3.Error as e:
            print(f"Error inserting record: {e}")
            continue
    
    conn.commit()
    conn.close()
# scripts/create_tables.py
import psycopg2
from config.settings import db_config

def create_tables(): 
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=db_config["name"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"]
    )
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_text (
            id SERIAL PRIMARY KEY,
            document_name TEXT,
            file_path TEXT,
            text TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preprocessed_text (
            id SERIAL PRIMARY KEY,
            document_name TEXT,
            file_path TEXT,
            text TEXT
        )
    """)

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
import sqlite3
import json
import os
from pathlib import Path

# Database file
FOLDER_PATH = Path(__file__).resolve().parent
DB_FILE = FOLDER_PATH.parent / 'test.db'

# JSON files
USERS_FILE = FOLDER_PATH / "users.json"
POSTS_FILE = FOLDER_PATH / "posts.json"
COMMENTS_FILE = FOLDER_PATH / "comments.json"

def create_tables(cursor):
    """Create tables in the database."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        website TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        body TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY (post_id) REFERENCES posts (id)
    )
    """)

def insert_data(cursor, table, data):
    """Insert data into the specified table."""
    if table == "users":
        cursor.executemany("""
        INSERT INTO users (id, name, email, phone, website) 
        VALUES (:id, :name, :email, :phone, :website)
        """, data)
    elif table == "posts":
        cursor.executemany("""
        INSERT INTO posts (id, title, body, user_id) 
        VALUES (:id, :title, :body, :userId)
        """, data)
    elif table == "comments":
        cursor.executemany("""
        INSERT INTO comments (id, name, email, body, post_id) 
        VALUES (:id, :name, :email, :body, :postId)
        """, data)

def load_json(file_path):
    """Load data from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    # Connect to SQLite database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Create tables
        create_tables(cursor)

        # Load data from JSON files
        users = load_json(USERS_FILE)
        print('executed 1')
        posts = load_json(POSTS_FILE)
        comments = load_json(COMMENTS_FILE)

        # Insert data into tables
        insert_data(cursor, "users", users)
        print('executed 2')

        insert_data(cursor, "posts", posts)
        print('executed 3')

        insert_data(cursor, "comments", comments)

        # Commit changes
        conn.commit()
        print("Database initialized and populated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        conn.close()

if __name__ == "__main__":
    main()

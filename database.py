import sqlite3

class WorkWithDatabase:
    def create_bd():
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER NOT NULL,
                permission VARCHAR(50) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS files(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key_tg VARCHAR(150) NOT NULL,
                blob_file BLOB NOT NULL,
                extension VARCHAR(50) NOT NULL 
            )
            """
            cursor.executescript(query)
            cursor.close()

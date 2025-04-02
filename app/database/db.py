import sqlite3 as sq

from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        load_dotenv()
        self.conn = sq.connect(os.getenv('db_file'), check_same_thread=False)
        self.cur = self.conn.cursor()

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT
            )
        ''')



    def add_user(self, tg_id, username, first_name):
        user = self.cur.execute('SELECT * FROM users WHERE tg_id=?', (tg_id,)).fetchone()
        if not user:
            self.cur.execute('INSERT INTO users (tg_id, username, first_name) VALUES (?, ?, ?)', (tg_id, username, first_name))
            self.conn.commit()

import sqlite3 as sq

from dotenv import load_dotenv
import os

from datetime import datetime, timedelta

class Database:
    def __init__(self):
        load_dotenv()
        self.conn = sq.connect(os.getenv('db_file'), check_same_thread=False)
        self.cur = self.conn.cursor()

        self.skills_conn = sq.connect(os.getenv('skills_db_file'), check_same_thread=False)
        self.skills_cur = self.skills_conn.cursor()

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT,
            study TEXT
            )
        ''')

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER NOT NULL,
            text TEXT,
            FOREIGN KEY (tg_id) REFERENCES users(tg_id)
            )
        ''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS game_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER NOT NULL,
        score INTEGER,
        FOREIGN KEY (tg_id) REFERENCES users(tg_id)
        )''')

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER NOT NULL,
        reminder_text TEXT,
        time DATETIME,
        FOREIGN KEY (tg_id) REFERENCES users(tg_id)
        )
        ''')

    def add_user(self, tg_id, username, first_name):
        user = self.cur.execute('SELECT * FROM users WHERE tg_id=?', (tg_id,)).fetchone()
        if not user:
            self.cur.execute('INSERT INTO users (tg_id, username, first_name) VALUES (?, ?, ?)', (tg_id, username, first_name))
            self.conn.commit()

    def set_study_field(self, tg_id, field):
        self.cur.execute('''UPDATE users SET study = ? WHERE tg_id = ?''', (field, tg_id))
        self.conn.commit()

    def get_reviews(self):
        reviews = self.cur.execute('SELECT * FROM feedbacks').fetchall()
        return reviews
    
    def get_user_reviews(self, tg_id):
        reviews = self.cur.execute('SELECT * FROM feedbacks WHERE tg_id=?', (tg_id,)).fetchall()
        return reviews

    def add_review(self, tg_id, text):
        self.cur.execute('INSERT INTO feedbacks (tg_id, text) VALUES (?, ?)', (tg_id, text))
        self.conn.commit()

    def review_by_id(self, review_id):
        review = self.cur.execute('SELECT * FROM feedbacks WHERE id=?', (review_id,)).fetchone()
        return review
    
    def add_reminder(self, tg_id, reminder_text, time):
        time = datetime.now() + timedelta(seconds=int(time))
        self.cur.execute('INSERT INTO reminders (tg_id, reminder_text, time) VALUES (?, ?, ?)', (tg_id, reminder_text, time))
        self.conn.commit()

    def user_reminders(self, tg_id):
        reminders = self.cur.execute('SELECT * FROM reminders WHERE tg_id=?', (tg_id,)).fetchall()
        return reminders
    
    def get_reminder_by_id(self, reminder_id):
        reminder = self.cur.execute('SELECT * FROM reminders WHERE id=?', (reminder_id,)).fetchone()
        return reminder
    
    def delete_reminder(self, tg_id, reminder_text):
        self.cur.execute('DELETE FROM reminders WHERE tg_id=? AND reminder_text=?', (tg_id, reminder_text))
        self.conn.commit()
import sqlite3
from datetime import datetime


DB_FILE = 'expenses.db'


def get_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    note TEXT
    )
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
    print('db initialized')
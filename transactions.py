from db import get_conn
from datetime import datetime


def add_tx(date_str, amount, category, note):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO transactions (date, amount, category, note) VALUES (?, ?, ?, ?)',
    (date_str, amount, category, note))
    conn.commit()
    conn.close()


def list_tx(limit=100):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM transactions ORDER BY date DESC LIMIT ?', (limit,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_tx(tx_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM transactions WHERE id = ?', (tx_id,))
    row = cur.fetchone()
    conn.close()
    return row


def update_tx(tx_id, date_str, amount, category, note):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('UPDATE transactions SET date=?, amount=?, category=?, note=? WHERE id=?',
    (date_str, amount, category, note, tx_id))
    conn.commit()
    conn.close()


def delete_tx(tx_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM transactions WHERE id=?', (tx_id,))
    conn.commit()
    conn.close()
# reports.py
# simple summary functions
from db import get_conn
from datetime import datetime


def monthly_total(year, month):
    conn = get_conn()
    cur = conn.cursor()
    start = f"{year:04d}-{month:02d}-01"
    if month == 12:
        end = f"{year+1:04d}-01-01"
    else:
        end = f"{year:04d}-{month+1:02d}-01"
    cur.execute('SELECT SUM(amount) as total FROM transactions WHERE date >= ? AND date < ?', (start, end))
    r = cur.fetchone()
    conn.close()
    return r['total'] if r and r['total'] is not None else 0.0


def category_summary(year, month=None):
    conn = get_conn()
    cur = conn.cursor()
    if year is None:
        cur.execute('SELECT category, SUM(amount) as total FROM transactions GROUP BY category')
    else:
        if month:
            start = f"{year:04d}-{month:02d}-01"
            if month == 12:
                end = f"{year+1:04d}-01-01"
            else:
                end = f"{year:04d}-{month+1:02d}-01"
            cur.execute(
                'SELECT category, SUM(amount) as total FROM transactions WHERE date >= ? AND date < ? GROUP BY category',
                (start, end)
            )
        else:
            cur.execute(
                'SELECT category, SUM(amount) as total FROM transactions WHERE strftime("%Y", date) = ? GROUP BY category',
                (str(year),)
            )
    rows = cur.fetchall()
    conn.close()
    return rows

# app.py
# main program with simple menu
from db import init_db
import transactions as tx
import reports
from datetime import datetime
try:
    from tabulate import tabulate
except Exception:
    tabulate = None


def input_date(prompt):
    s = input(prompt + ' (YYYY-MM-DD) [leave empty for today]: ').strip()
    if s == '':
        return datetime.today().strftime('%Y-%m-%d')
    try:
        datetime.strptime(s, '%Y-%m-%d')
        return s
    except Exception:
        print('bad date, using today')
        return datetime.today().strftime('%Y-%m-%d')


def input_amount(prompt):
    s = input(prompt + ': ').strip()
    try:
        return float(s)
    except Exception:
        print('bad number, using 0')
        return 0.0


def add_flow():
    d = input_date('date')
    a = input_amount('amount')
    c = input('category: ').strip() or 'misc'
    n = input('note (optional): ').strip()
    tx.add_tx(d, a, c, n)
    print('added')


def list_flow():
    rows = tx.list_tx(200)
    if not rows:
        print('no records')
        return
    out = []
    for r in rows:
        out.append([r['id'], r['date'], r['amount'], r['category'], r['note']])
    if tabulate:
        print(tabulate(out, headers=['id', 'date', 'amount', 'category', 'note']))
    else:
        for r in out:
            print(r)


def edit_flow():
    try:
        idn = int(input('enter id to edit: '))
    except Exception:
        print('bad id')
        return
    r = tx.get_tx(idn)
    if not r:
        print('not found')
        return
    print('leave empty to keep old')
    d = input('date (YYYY-MM-DD) [' + r['date'] + ']: ').strip() or r['date']
    a_s = input('amount [' + str(r['amount']) + ']: ').strip()
    try:
        a = float(a_s) if a_s != '' else r['amount']
    except Exception:
        a = r['amount']
    c = input('category [' + r['category'] + ']: ').strip() or r['category']
    n = input('note [' + (r['note'] or '') + ']: ').strip() or r['note']
    tx.update_tx(idn, d, a, c, n)
    print('updated')


def delete_flow():
    try:
        idn = int(input('enter id to delete: '))
    except Exception:
        print('bad id')
        return
    r = tx.get_tx(idn)
    if not r:
        print('not found')
        return
    confirm = input('type yes to confirm deletion: ')
    if confirm.lower() == 'yes':
        tx.delete_tx(idn)
        print('deleted')
    else:
        print('cancelled')


def month_total_flow():
    y = input('year (YYYY) [empty=this year]: ').strip()
    m = input('month (1-12) [empty=this month]: ').strip()
    t = datetime.today()
    try:
        yy = int(y) if y else t.year
    except:
        yy = t.year
    try:
        mm = int(m) if m else t.month
    except:
        mm = t.month
    total = reports.monthly_total(yy, mm)
    print(f'Total for {yy}-{mm:02d} = {total}')


def cat_summary_flow():
    y = input('year (YYYY) [empty=all time]: ').strip()
    if y == '':
        rows = reports.category_summary(None)
    else:
        try:
            yy = int(y)
        except:
            print('bad year')
            return
        m = input('month (1-12) [empty=whole year]: ').strip()
        if m == '':
            rows = reports.category_summary(yy)
        else:
            try:
                mm = int(m)
            except:
                print('bad month')
                return
            rows = reports.category_summary(yy, mm)
    if not rows:
        print('no data')
        return
    for r in rows:
        print(r['category'], r['total'])


def main():
    init_db()
    while True:
        print('\n--- simple expense tracker ---')
        print('1. add expense')
        print('2. list expenses')
        print('3. edit expense')
        print('4. delete expense')
        print('5. month total')
        print('6. category summary')
        print('0. quit')
        s = input('choose: ').strip()
        if s == '1':
            add_flow()
        elif s == '2':
            list_flow()
        elif s == '3':
            edit_flow()
        elif s == '4':
            delete_flow()
        elif s == '5':
            month_total_flow()
        elif s == '6':
            cat_summary_flow()
        elif s == '0':
            print('bye')
            break
        else:
            print('bad option')


if __name__ == '__main__':
    main()

Expense Tracker (Python + SQLite)
=================================

This is a simple command-line Expense Tracker built using basic Python and SQLite. It helps users record and organize their daily expenses without any complex setup or online tools. Everything is stored locally inside a single SQLite database file.

* * *

1\. Features
------------

*   Add a new expense with date, amount, category, and note
*   View all saved expenses
*   Edit existing records using their ID
*   Delete unwanted entries
*   View monthly total spending
*   View category-wise spending summary
*   Data stored locally in **expenses.db**

* * *

2\. Project Structure
---------------------

app.py            → main CLI program (menu and functions)
db.py             → database initialization and connection
transactions.py   → add, list, edit, delete operations
reports.py        → monthly and category summary logic
requirements.txt  → optional dependency (tabulate)
expenses.db       → created automatically when program runs

* * *

3\. How to Run
--------------

**Step 1:** Install Python 3.8 or above

**Step 2 (Optional):** Create a virtual environment

python -m venv venv

**Activate:**

Windows: venv\\Scripts\\activate
Mac/Linux: source venv/bin/activate

**Step 3:** Install optional dependencies

pip install -r requirements.txt

**Step 4:** Run the application

python app.py

You will see a menu:

\--- simple expense tracker ---
1. add expense
2. list expenses
3. edit expense
4. delete expense
5. month total
6. category summary
0. quit
choose:

* * *

4\. Database Information
------------------------

This project uses a simple SQLite database file named **expenses.db**. It contains one table:

transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    amount REAL,
    category TEXT,
    note TEXT
)

This structure keeps the project lightweight and easy to understand.

* * *

5\. Usage Examples
------------------

### Add an Expense

Enter date (YYYY-MM-DD):
Enter amount:
Enter category:
Enter note (optional):

### List Expenses

id   date         amount   category   note
1    2025-02-10   120      food       lunch
2    2025-02-11   60       travel     auto

### Edit an Expense

enter id to edit: 1
date \[2025-02-10\]:
amount \[120\]:
category \[food\]:
note \[lunch\]:

### Delete an Expense

enter id to delete: 2
type yes to confirm deletion: yes

* * *

6\. Testing Checklist
---------------------

*   Add multiple sample expenses
*   List expenses to confirm entries
*   Edit a record and verify changes
*   Delete an entry and check the list output
*   Use monthly summary to verify totals
*   Use category summary to check grouping

* * *

7\. Author
----------

**Name:** Aditya Shukla  
**Registration No:** 25BAI11125  
**Faculty Guide:** Dr. Monika Vyas



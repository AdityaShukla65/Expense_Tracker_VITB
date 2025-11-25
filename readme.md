<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Expense Tracker - README</title>

<style>
    body {
        font-family: "Segoe UI", Tahoma, sans-serif;
        margin: 0;
        padding: 0;
        background: #f2f4f8;
        color: #222;
        line-height: 1.6;
    }

    .container {
        width: 85%;
        max-width: 900px;
        margin: 40px auto;
        background: #ffffff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }

    h1, h2, h3 {
        color: #003366;
        margin-bottom: 12px;
    }

    h1 {
        text-align: center;
        margin-bottom: 30px;
    }

    pre, code {
        background: #f0f0f0;
        padding: 10px 15px;
        border-radius: 6px;
        font-family: Consolas, monospace;
        font-size: 14px;
        white-space: pre-wrap;
        border-left: 4px solid #003366;
    }

    ul {
        margin-top: 8px;
    }

    .section {
        margin-bottom: 40px;
    }

    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #555;
    }
</style>

</head>
<body>

<div class="container">

    <h1>Expense Tracker (Python + SQLite)</h1>

    <div class="section">
        <h2>Overview</h2>
        <p>
            The Expense Tracker is a small command-line application built using basic Python and SQLite.
            It helps users keep track of daily expenses locally without needing online accounts or 
            complicated tools. All records are stored in a simple SQLite database file.
        </p>
    </div>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li>Add a new expense with date, amount, category, and note.</li>
            <li>View all expenses in a clean table format.</li>
            <li>Edit an existing expense using its ID.</li>
            <li>Delete an expense permanently.</li>
            <li>View monthly total for a selected year and month.</li>
            <li>View category-wise total spending.</li>
            <li>Local storage using <code>expenses.db</code> (SQLite).</li>
        </ul>
    </div>

    <div class="section">
        <h2>Project Structure</h2>
<pre>
VITYARTHI_PROJECT/
│
├── app.py            # main CLI program
├── db.py             # sqlite connection + table creation
├── transactions.py   # add / list / edit / delete functions
├── reports.py        # summary calculations
├── requirements.txt  # optional dependency: tabulate
└── expenses.db       # auto-created database
</pre>
    </div>

    <div class="section">
        <h2>How to Run</h2>

        <h3>1. Make sure Python is installed</h3>
        <p>Python 3.8 or above is recommended.</p>

        <h3>2. (Optional) Create a Virtual Environment</h3>
<pre>
python -m venv venv
# activate:
# Windows:
venv\Scripts\activate
# mac/linux:
source venv/bin/activate
</pre>

        <h3>3. Install optional dependencies</h3>
        <p>The app works without <code>tabulate</code>, but table output looks better with it.</p>
<pre>pip install -r requirements.txt</pre>

        <h3>4. Run the Application</h3>
<pre>python app.py</pre>

        <p>After running, the menu appears:</p>
<pre>
--- simple expense tracker ---
1. add expense
2. list expenses
3. edit expense
4. delete expense
5. month total
6. category summary
0. quit
choose:
</pre>
    </div>

    <div class="section">
        <h2>Database Details</h2>
        <p>The application uses an SQLite database named <code>expenses.db</code>. It contains one table:</p>

<pre>
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    note TEXT
);
</pre>

        <p>
            This keeps the project lightweight and easy to understand while still having proper storage.
        </p>
    </div>

    <div class="section">
        <h2>Usage Examples</h2>

        <h3>Adding an expense</h3>
<pre>
Enter date (YYYY-MM-DD) [leave empty for today]:
Enter amount:
Enter category:
Enter note (optional):
</pre>

        <h3>Listing expenses</h3>
<pre>
id   date         amount   category   note
1    2025-02-10   120      food       lunch
2    2025-02-11   60       travel     auto
</pre>

        <h3>Editing an expense</h3>
<pre>
enter id to edit: 1
date [2025-02-10]:
amount [120]:
category [food]:
note [lunch]:
</pre>

        <h3>Deleting an expense</h3>
<pre>
enter id to delete: 2
type yes to confirm deletion: yes
</pre>

    </div>

    <div class="section">
        <h2>Testing Steps</h2>
        <ul>
            <li>Add multiple expenses and confirm they appear in the list.</li>
            <li>Edit a record and verify that the values change.</li>
            <li>Delete an entry and check the list again.</li>
            <li>View the monthly total and compare it with manual addition.</li>
            <li>Check category summary output for correctness.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Possible Improvements (Optional)</h2>
        <ul>
            <li>Separate income and expense tracking.</li>
            <li>Add export to CSV option.</li>
            <li>Add budget limits per category.</li>
            <li>Add a GUI version using Tkinter or a web version using Flask.</li>
            <li>Password lock or pin for privacy.</li>
        </ul>
    </div>

    <div class="footer">
        Made by <b>Aditya Shukla</b>  
        Registration No. <b>25BAI11125</b>  
        Under the guidance of <b>Dr. Monika Vyas</b>
    </div>

</div>

</body>
</html>

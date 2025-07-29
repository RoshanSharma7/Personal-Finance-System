import sqlite3

def connect_db():
    return sqlite3.connect('finance.db')

def gen_month_report(username, month, year):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''SELECT type, amount FROM transactions WHERE username = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ? ''', (username, f"{int(month):02}", str(year)))
    income = 0
    expense = 0

    for t_type, amount in cur.fetchall():
        if t_type == "Income":
            income += amount
        elif t_type == "Expense":
            expense += amount

    conn.close()

    print("----------------------------------")
    print(f"\n Report for {month}/{year}")
    print("----------------------------------")
    print(f" Total Income    :   ₹{income}")
    print(f" Total Expenses  :   ₹{expense}")
    print(f" Net Savings     :   ₹{income - expense}")

def gen_year_report(username, year):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT type, amount FROM transactions WHERE username = ? AND strftime('%Y', date) = ?''', (username, str(year)))
    income = 0
    expense = 0

    for t_type, amount in cur.fetchall():
        if t_type == "Income":
            income += amount
        elif t_type == "Expense":
            income += amount
    conn.close()

    print("----------------------------------")
    print(f" Report for Year {year}")
    print("----------------------------------")
    print(f" Total Income    : ₹{income}")
    print(f" Total Expenses  : ₹{expense}")
    print(f" Net Savings     : ₹{income - expense}")
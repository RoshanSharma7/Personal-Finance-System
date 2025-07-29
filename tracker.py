import sqlite3

# database connection function
def connect_db():
    return sqlite3.connect('finance.db')

#   ========== Table Creation Fields ============
# transaction table creation function
def create_transaction_tb():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT, 
        type TEXT, 
        category TEXT, 
        amount REAL, 
        date TEXT, 
        description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# budget table creation
def budget_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS budgets (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, category TEXT, month TEXT, year TEXT, amount REAL)''')
    conn.commit()
    conn.close()

# Adding translation function
def add_trans(username, type, category, amount, date, description=""):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO transactions (username, type, category, amount, date, description)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, type, category, amount, date, description))

    conn.commit()
    conn.close()
    if type == "Income":
        print(f"{amount}₹ Credited to your account.")
    else:
        print(f"{amount}₹ Debited from your account.")

#   ========== Function Creation Fields ============
# view transaction function
def view_trans(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT type, category, amount, date, description FROM transactions WHERE username = ? ORDER BY date DESC''', (username,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No Transactions Found.")
    else:
        print("\nYour Transaction: ")
        for row in rows:
            nature = "Credit" if row[0] == "Income" else "Debit"
            print(f" Date        :   {row[3]}")
            print(f" Type        :   {row[0]} ({nature})")
            print(f" Category    :   {row[1]}")
            print(f" Amount      :   {row[2]}₹")
            print(f" Description :   {row[4]}")
            print("----------------------------------")

# transaction list function
def list_trans(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT id, type, category, amount, date, description FROM transactions WHERE username = ? ORDER BY date DESC''', (username,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No Transaction Found.")
    else:
        print("Your Transaction:")
        for row in rows:
            nature = "Credit" if row[1] == "Income" else "Debit"
            print(f" ID          :   {row[0]}")
            print(f" Date        :   {row[4]}")
            print(f" Type        :   {row[1]} ({nature})")
            print(f" Category    :   {row[2]}")
            print(f" Amount      :   {row[3]}₹")
            print(f" Description :   {row[5]}")
            print("----------------------------------")

# transaction update function
def update_trans(trans_id, username, field, new_value):
    conn = connect_db()
    cur = conn.cursor()

    if field not in ["category", "amount", "date", "description"]:
        print("Invalid field. Choose from: Category, Amount, Date, Description.")
        return

    try:
        cur.execute(f'''UPDATE transactions SET {field} = ? WHERE id = ? AND username = ?''', (new_value, trans_id, username))
        if cur.rowcount == 0:
            print("No Transaction Found or Update Failed.")
        else:
            print("Transaction Updated Successfully.")
        conn.commit()

    finally:
        conn.close()

# transaction deletion function
def delete_trans(trans_id, username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''DELETE FROM transactions WHERE id = ? AND username = ?''', (trans_id, username))

    if cur.rowcount == 0:
        print("No Transaction Found or Deletion Failed.")
    else:
        print("Transaction Deleted Successfully.")

    conn.commit()
    conn.close()

def set_budget(username, category, month, year, amount):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT id FROM budgets WHERE username = ? AND category = ? AND month = ? AND year = ? ''', (username, category, month, year))
    result = cur.fetchone()

    if result:
        cur.execute('''UPDATE budgets SET amount = ? WHERE id = ?''', (amount, result[0]))
        print("Budget Update Successfully.")

    else:
        cur.execute('''INSERT INTO budgets (username, category, month, year, amount) VALUES (?, ?, ?, ?, ?)''', (username, category, month, year, amount))
        print("Budget Set Successfully.")

    conn.commit()
    conn.close()

# budget warning
def budget_warning(username, category, month, year):
    conn = connect_db()
    cur = conn.cursor()

    padded_month = f"{int(month):02}"

    cur.execute('''
        SELECT SUM(amount) FROM transactions 
        WHERE username = ? AND category = ? AND type = 'Expense'
        AND strftime('%m', date) = ? AND strftime('%Y', date) = ?
    ''', (username, category, padded_month, year))
    total_spent = cur.fetchone()[0] or 0

    cur.execute('''
        SELECT amount FROM budgets 
        WHERE username = ? AND category = ? AND month = ? AND year = ?
    ''', (username, category, month, year))
    budget = cur.fetchone()
    conn.close()

    if budget and total_spent > budget[0]:
        print(f"Warning: You have exceeded your budget for '{category}' by ₹{total_spent - budget[0]:.2f}")




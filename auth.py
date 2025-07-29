import sqlite3
import hashlib

# setup project database function
def create_user_table():
    conn = sqlite3.connect('finance.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

# login history table for the logout from the db
def log_history():
    conn = sqlite3.connect('finance.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS log_history (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Hiding the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register the user
def register(username, password):
    conn = sqlite3.connect('finance.db')
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        print("Registration Successful!")
    except sqlite3.IntegrityError:
        print("Username Already Exists.")
    finally:
        conn.close()


# Login function creation
def login(username, password):
    conn = sqlite3.connect('finance.db')
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cur.fetchone()
    conn.close()
    if result and result[0] == hash_password(password):
        print("Login Successfully")
        return True
    else:
        print("Invalid Username or Password.")
        return False

# login action for setup the user and ask to delete form the db
def login_action(username, action):
    conn = sqlite3.connect('finance.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO log_history (username, action) VALUES (?, ?)''', (username, action))
    conn.commit()
    conn.close()

# delete action for the setup the user and helping deleting from the db
def delete_action(username):
    conn = sqlite3.connect('finance.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE username = ?", (username, ))
    conn.commit()
    conn.close()
    print(f"User '{username}' Deleted from the detabase.")
import sqlite3

# Define connection and cursor
conn = sqlite3.connect('finance_app.db')

cursor = conn.cursor()

# Users Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

# Account Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    account(
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        balance REAL,
        savings REAL,
        currency TEXT,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES user(user_id)
    )""")

# Transactions Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    transact(
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        amount REAL,
        description TEXT,
        account_id INTEGER,
        FOREIGN KEY(account_id) REFERENCES account(account_id)
    )""")

# cursor.execute('drop table user')
# cursor.execute('drop table account')
# cursor.execute('drop table transact')

# cursor.execute("insert into user (first_name, last_name, email, password)"
#                "values ('David', 'Aznar', 'dae.aznar@gmail.com', '123')")

# cursor.execute("select * from user")
# print(cursor.fetchall())

# cursor.execute("delete from user where user_id=1")

conn.commit()

conn.close()

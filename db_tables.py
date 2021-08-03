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
        balance FLOAT DEFAULT 0 NOT NULL,
        savings FLOAT DEFAULT 0 NOT NULL,
        currency TEXT,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES user(user_id)
    )""")

# Transactions Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    transact(
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        amount FLOAT,
        description TEXT,
        account_id INTEGER,
        FOREIGN KEY(account_id) REFERENCES account(account_id)
    )""")

# cursor.execute('drop table user')
# cursor.execute('drop table account')
# cursor.execute('drop table transact')

# cursor.execute("SELECT user_id FROM user WHERE email = 'dae.aznar@git.com' ")
# print(cursor.fetchall())
# query = cursor.fetchone()[0]
# print(query)

# cursor.execute("INSERT INTO user(first_name, last_name, email, password)"
#                "VALUES('John', 'Doe', 'john.doe@git.com', '123')")

cursor.execute("select * from user")
print(cursor.fetchall())

cursor.execute("select * from account")
print(cursor.fetchall())

cursor.execute("select * from transact")
print(cursor.fetchall())

# cursor.execute("select * from transact where transaction_date > datetime('now', '-7 day')")
# print(cursor.fetchall())

# cursor.execute("delete from transact where transaction_id=3")

conn.commit()

conn.close()

import mask_password
import sqlite3
import pandas as pd

conn = sqlite3.connect('finance_app.db')
cursor = conn.cursor()


# User Class
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\n' \
               f'Email: {self.email}'

    def update_info(self):
        print(f"---Current Information---\n"
              f"First Name: {self.first_name}\n"
              f"Last Name: {self.last_name}\n"
              f"Email: {self.email}\n")
        while True:
            print("---Update Information---")
            print("(press 0 to cancel)")
            first_name = input("First Name: ")
            if first_name == '0':
                break
            last_name = input("Last Name: ")
            email = input("Email: ")

            cursor.execute("SELECT email FROM user WHERE email = :email", {'email': email})
            check_mail = cursor.fetchall()

            if len(check_mail) != 0:
                print("Email is already taken\n")
            else:
                print()
                while True:
                    temp_password = mask_password.hide_pass(
                        prompt='Current Password:')  # Prevent password from showing input
                    if temp_password == self.password:
                        password = mask_password.hide_pass(prompt='New Password: ')
                        break
                    else:
                        print("Error. Incorrect password\n")

                while True:
                    confirm = input("Update information? (y/n)>>")
                    if confirm == 'y':
                        with conn:
                            cursor.execute(
                                """UPDATE user SET first_name = :first_name, last_name = :last_name, email = :email,
                                password = :password, update_at = CURRENT_TIMESTAMP
                                WHERE email = :current_email""",
                                {'current_email': self.email, 'first_name': first_name, 'last_name': last_name,
                                 'email': email, 'password': password})
                        self.first_name = first_name
                        self.last_name = last_name
                        self.email = email
                        self.password = password
                        break
                    elif confirm == 'n':
                        print()
                        break
                    else:
                        print("Invalid Option\n")
                if confirm == 'y':
                    break
                break
            break


# Account Class
class Account:
    def __init__(self, account_id, balance, savings, currency, user_id):
        self.account_id = account_id
        self.balance = balance
        self.savings = savings
        self.currency = currency
        self.user_id = user_id

    def __str__(self):
        return f'Balance: {self.balance}\n' \
               f'Savings: {self.savings}\n' \
               f'Currency: {self.currency}'

    def balance_report(self):
        while True:
            print()
            print("Select time frame for de report\n"
                  "1. Today\n"
                  "2. This Week\n"
                  "3. This Month\n"
                  "4. Last 3 Months\n"
                  "0. Return\n")
            try:
                opt = int(input("Option: "))
                print()
            except:
                print("Invalid Option\n")
            else:
                # TODO: Show Balance Report as table
                if opt == 1:
                    # Use Pandas to give table structure
                    df = pd.read_sql_query("SELECT * FROM transact WHERE account_id = :account_id AND "
                                           "transaction_date > datetime('now', '-24 hour')",
                                           conn, params=({'account_id': self.account_id}))
                    print(df.head())
                elif opt == 2:
                    df = pd.read_sql_query("SELECT * FROM transact WHERE account_id = :account_id AND "
                                           "transaction_date > datetime('now', '-7 day')",
                                           conn, params=({'account_id': self.account_id}))
                    print(df.head())
                elif opt == 3:
                    df = pd.read_sql_query("SELECT * FROM transact WHERE account_id = :account_id AND "
                                           "transaction_date > datetime('now', '-1 month')",
                                           conn, params=({'account_id': self.account_id}))
                    print(df.head())
                elif opt == 4:
                    df = pd.read_sql_query("SELECT * FROM transact WHERE account_id = :account_id AND "
                                           "transaction_date > datetime('now', '-3 month')",
                                           conn, params=({'account_id': self.account_id}))
                    print(df.head())
                elif opt == 0:
                    break
                else:
                    print("Invalid Option\n")

    def add_savings(self):
        while True:
            try:
                print("Specify amount to Add to Savings (press 0 to cancel)")
                amount = float(input("Amount: "))
            except:
                print("Invalid Value\n")
            else:
                if amount == 0:
                    break
                else:
                    if amount > self.balance:
                        print("Error. There isn't enough in Balance")
                    else:
                        self.savings += amount
                        self.balance -= amount
                        with conn:
                            cursor.execute("""UPDATE account SET savings = :savings, balance = :balance
                                           WHERE account_id = :account_id""",
                                           {'savings': self.savings, 'balance': self.balance,
                                            'account_id': self.account_id})
                            print("*Movement Successful*")
                    break

    def withdraw_savings(self):
        while True:
            try:
                print("Specify amount to Add to Savings (press 0 to cancel)")
                amount = float(input("Amount: "))
            except:
                print("Invalid Value\n")
            else:
                if amount == 0:
                    break
                else:
                    if amount > self.savings:
                        print("Error. There isn't enough in Savings")
                    else:
                        self.savings -= amount
                        self.balance += amount
                        with conn:
                            cursor.execute("""UPDATE account SET savings = :savings, balance = :balance
                                           WHERE account_id = :account_id""",
                                           {'savings': self.savings, 'balance': self.balance,
                                            'account_id': self.account_id})
                            print("*Movement Successful*")
                    break

    def change_currency(self):
        # TODO: Function to change all
        print(f"""
    You're using: {self.currency}
    
    Change it for: 
    1. US Dollars
    2. Euros
    3. Mexican Peso
    0. Cancel
    """)
        try:
            opt = int(input("Option: "))
        except:
            print("Invalid Option\n")
        else:
            if opt == 1:
                self.currency = "USD"
                with conn:
                    cursor.execute(
                        "UPDATE account SET currency = 'USD' WHERE user_id = :user_id",
                        {'user_id': self.user_id})
            elif opt == 2:
                self.currency = "EUR"
                with conn:
                    cursor.execute(
                        "UPDATE account SET currency = 'EUR' WHERE user_id = :user_id",
                        {'user_id': self.user_id})
            elif opt == 3:
                self.currency = "MXN"
                with conn:
                    cursor.execute(
                        "UPDATE account SET currency = 'MXN' WHERE user_id = :user_id",
                        {'user_id': self.user_id})
            elif opt == 0:
                pass
            else:
                print("Invalid Option\n")

    def info(self, user):
        print(f"""
===========================================================
                                    Currency: {self.currency}
            *Welcome {user.first_name} {user.last_name}!*

        Total Balance: {self.balance}
        Savings: {self.savings}

===========================================================
    """)


# Movements Class
class Movement:
    def __init__(self, movement_type):
        self.movement_type = movement_type

    def movements_menu(self, account):
        while True:
            print()
            print("Select Movement Type:\n"
                  "1. Income\n"
                  "2. Expense\n"
                  "3. Add to Savings from Balance\n"
                  "4. Withdraw from Savings to Balance\n"
                  "0. Cancel\n")
            try:
                opt = int(input("Option: "))
            except:
                print("Invalid Option\n")
            else:
                if opt == 1:
                    self.movement_type = 'Income'
                    self.register_movement(account)
                    break
                elif opt == 2:
                    if account.balance == 0:
                        print("Error. Can't register expense if balance is 0")
                        break
                    else:
                        self.movement_type = 'Expense'
                        self.register_movement(account)
                        break
                elif opt == 3:
                    account.add_savings()
                    break
                elif opt == 4:
                    account.withdraw_savings()
                    break
                elif opt == 0:
                    break
                else:
                    print("Invalid Option\n")

    def register_movement(self, account):
        print()
        print(f"You're making a {self.movement_type}")
        try:
            amount = float(input(f"Specify amount of {self.movement_type}: "))
        except:
            print("Invalid Value\n")
        else:
            if self.movement_type == 'Expense' and amount > account.balance:
                print("Error. Can't register expense greater than total balance")
            else:
                description = input("Specify a short description (optional): ")
                cursor.execute("SELECT account_id FROM account WHERE account_id = :account_id",
                               {'account_id': account.account_id})
                account_id = cursor.fetchone()[0]
                with conn:
                    check_transact = cursor.execute("INSERT INTO transact(type, amount, description, account_id)"
                                                    "VALUES(:type, :amount, :description, :account_id)",
                                                    {'type': self.movement_type, 'amount': amount,
                                                     'description': description, 'account_id': account_id})
                    if check_transact:
                        print("*Transaction Successful*")
                        if self.movement_type == 'Income':
                            new_balance = account.balance + amount
                        elif self.movement_type == 'Expense':
                            new_balance = account.balance - amount
                    else:
                        print("Something went wrong. Please try again later.")
                with conn:
                    cursor.execute("""UPDATE account SET balance = :balance
                                   WHERE account_id = :account_id""",
                                   {'balance': new_balance, 'account_id': account_id})

                account.balance = new_balance
                transaction_id = cursor.lastrowid  # Get most recent autoincrement id inserted

                cursor.execute("SELECT transaction_date FROM transact WHERE transaction_id = :transaction_id",
                               {'transaction_id': transaction_id})
                transaction_date = cursor.fetchone()[0]
                transact = Transaction(transaction_id, self.movement_type, transaction_date, amount, description)
                transact.get_transaction_info(account)

    def modify_movement(self):
        pass


# Transaction Class
class Transaction:
    def __init__(self, transaction_id, transaction_type, date_time, amount, description):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.date_time = date_time
        self.amount = amount
        self.description = description

    def get_transaction_info(self, account):
        print(f"""
===========================================================
                                    Currency: {account.currency}
            *Transaction Information*

        Transaction Number: {self.transaction_id}
        Date: {self.date_time}
        Amount: {self.amount}
        Description: {self.description}
        
===========================================================
    """)

    def set_amount(self, amount):
        self.amount = amount

    def set_description(self):
        self.description = input("Description: ")

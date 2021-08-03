import mask_password
import sqlite3

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
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            check_mail = cursor.execute("SELECT email FROM user WHERE email = :email", {'email': email})
            if check_mail:
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
                                "UPDATE user SET first_name = :first_name, last_name = :last_name, email = :email, "
                                "password = :password "
                                "WHERE email = :current_email",
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
    def __init__(self, balance, savings, currency, user_id):
        self.balance = balance
        self.savings = savings
        self.currency = currency
        self.user_id = user_id

    def __str__(self):
        return f'Balance: {self.balance}\n' \
               f'Savings: {self.savings}\n' \
               f'Currency: {self.currency}'

    def balance_report(self):
        print("===== Balance Report =====")

    def add_savings(self):
        pass

    def withdraw_savings(self):
        pass

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

    def movements_menu(self):
        pass

    def register_movement(self):
        pass

    def modify_movement(self):
        pass


# Transaction Class
class Transaction:
    def __init__(self, transaction_id, transaction_type, date_time, description):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.date_time = date_time
        self.amount = 0
        self.description = description

    def set_date(self):
        pass

    def set_amount(self, amount):
        self.amount = amount

    def set_description(self):
        pass


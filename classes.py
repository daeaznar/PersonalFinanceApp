import mask_password


# User Class
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self._email = email
        self._password = password

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\n' \
               f'Email: {self._email}'

    def register(self):
        pass

    def login(self):
        pass

    def update_info(self):
        print(f"---Current Information---"
              f"First Name: {self.first_name}"
              f"Last Name: {self.last_name}"
              f"Email: {self._email}\n")
        while True:
            print("---Update Information---")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            while True:
                temp_password = mask_password.hide_pass(
                    prompt='Current Password:')  # Prevent password from showing input
                password = mask_password.hide_pass(prompt='New Password: ')
                if password == temp_password:
                    break
                else:
                    print("Error. Password doesn't match")

            while True:
                confirm = input("Update information? (y/n)>>")
                if confirm == 'y':
                    user = User(first_name, last_name, email, password)
                    # TODO: Add function to update to DB

                    break
                elif confirm == 'n':
                    print()
                    break
                else:
                    print("Invalid Option\n")
            if confirm == 'y':
                break


# Account Class
class Account:
    def __init__(self, balance, savings, currency):
        self.balance = balance
        self._savings = savings
        self._currency = currency

    def __str__(self):
        return f'Balance: {self.balance}\n' \
               f'Savings: {self._savings}\n' \
               f'Currency: {self._currency}'

    def balance_report(self):
        print("===== Balance Report =====")

    def add_savings(self):
        pass

    def withdraw_savings(self):
        pass

    def change_currency(self):
        pass


# Movements Class
class Movement:
    def __init__(self, movement_type):
        self.movement_type = movement_type

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

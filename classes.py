# User Class-
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
        pass


# Account Class
class Account:
    def __init__(self, balance, savings, currency):
        self.balance = balance
        self._saving = savings
        self._currency = currency

    def balance_report(self):
        pass

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
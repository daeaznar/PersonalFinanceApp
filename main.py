from sys import exit
import sqlite3
import mask_password

from classes import User, Account, Movement, Transaction

# Define connection and cursor2
conn = sqlite3.connect('finance_app.db')
cursor = conn.cursor()


def main():
    while True:
        print("""
========== Personal Finance App ==========\n
    Please select an option to continue\n
    1. Login
    2. Register
    0. Exit
        """)
        try:
            opt = int(input("Option: "))
        except:
            print("Invalid Option\n")
        else:
            if opt == 1:
                login()
                break
            elif opt == 2:
                register()
            elif opt == 0:
                while True:
                    confirm = input("Are you sure you want to exit? (y/n)>>")
                    if confirm == 'y':
                        print("See you later ;)\n\n"
                              "Exiting System...")
                        exit()
                    elif confirm == 'n':
                        print()
                        break
                    else:
                        print("Invalid Option\n")
            else:
                print("Invalid Option\n")


# noinspection PyProtectedMember
def home(user, account):
    transacts = []
    print()
    while True:
        account.info(user)
        print("""
        Please select an option to continue\n
        1. Movements Registry
        2. Balance Report
        3. Update Account Information
        4. Change Currency
        0. Log Out
        """)
        try:
            opt = int(input("Option: "))
        except:
            print("Invalid Option\n")
        else:
            if opt == 1:
                while True:
                    print("Select Movement Type:\n"
                          "1. Deposit\n"
                          "2. Withdrawal")
                    try:
                        opt = int(input("Option: "))
                    except:
                        print("Invalid Option\n")
                    else:
                        if opt == 1:
                            transacts.append(Movement('Deposit'))
                            break
                        elif opt == 2:
                            transacts.append(Movement('Withdrawal'))
                        else:
                            print("Invalid Option\n")
            elif opt == 2:
                account.balance_report()
            elif opt == 3:
                user.update_info()
            elif opt == 4:
                account.change_currency()
            elif opt == 0:
                while True:
                    confirm = input("Are you sure you want to log out? (y/n)>>")
                    if confirm == 'y':
                        print(f"See you soon {user.first_name}\n\n"
                              "Logging out...")
                        break
                    elif confirm == 'n':
                        print()
                        break
                    else:
                        print("Invalid Option\n")
                if confirm == 'y':
                    break
            else:
                print("Invalid Option\n")


def login():
    print()
    print("*Login*")
    while True:
        print("Enter your credentials\n")
        email = input("Email: ")
        password = mask_password.hide_pass()
        try:
            # region Get User
            query = cursor.execute("SELECT user_id FROM user WHERE email = :email AND password = :password",
                                   {'email': email, 'password': password})
            if query:
                user_id = cursor.fetchone()[0]

                cursor.execute("SELECT first_name FROM user WHERE user_id = :user_id", {'user_id': user_id})
                first_name = cursor.fetchone()[0]

                cursor.execute("SELECT last_name FROM user WHERE user_id = :user_id", {'user_id': user_id})
                last_name = cursor.fetchone()[0]

                cursor.execute("SELECT email FROM user WHERE user_id = :user_id", {'user_id': user_id})
                email = cursor.fetchone()[0]

                cursor.execute("SELECT password FROM user WHERE user_id = :user_id", {'user_id': user_id})
                password = cursor.fetchone()[0]

                user = User(first_name, last_name, email, password)
                # endregion

                # region Get Account
                cursor.execute("SELECT balance FROM account WHERE user_id = :user_id", {'user_id': user_id})
                balance = cursor.fetchone()[0]

                cursor.execute("SELECT savings FROM account WHERE user_id = :user_id", {'user_id': user_id})
                savings = cursor.fetchone()[0]

                cursor.execute("SELECT currency FROM account WHERE user_id = :user_id", {'user_id': user_id})
                currency = cursor.fetchone()[0]

                account = Account(balance, savings, currency, user_id)
                # endregion
            else:
                print('Something went wrong, please try again later')
        except:
            print("Incorrect email or password\n")
        else:
            home(user, account)
            break


def register():
    print()
    print("*Register*")
    while True:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        check_mail = cursor.execute("SELECT email FROM user WHERE email = :email", {'email': email})
        if check_mail:
            print("Email is already taken\n")
        else:
            print()
            while True:
                temp_password = mask_password.hide_pass()  # Prevent password from showing input
                password = mask_password.hide_pass(prompt='Confirm Password: ')
                if password == temp_password:
                    break
                else:
                    print("Error. Password doesn't match")
            while True:
                confirm = input("Is your information correct? (y/n)>>")
                if confirm == 'y':
                    user = User(first_name, last_name, email, password)

                    with conn:
                        cursor.execute("INSERT INTO user (first_name, last_name, email, password)"
                                       "VALUES(:first_name, :last_name, :email, :password)",
                                       {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email,
                                        'password': user.password})

                        cursor.execute("SELECT user_id FROM user WHERE email = :email", {'email': user.email})
                        user_id = cursor.fetchone()[0]

                        account = Account(0, 0, 'MXN', user_id)

                        cursor.execute("INSERT INTO account (currency, user_id)"
                                       "VALUES(:currency, :user_id)",
                                       {'currency': account.currency, 'user_id': user_id})

                    home(user, account)
                    break
                elif confirm == 'n':
                    print()
                    break
                else:
                    print("Invalid Option\n")
            if confirm == 'y':
                break
        break


if __name__ == '__main__':
    main()
    conn.close()

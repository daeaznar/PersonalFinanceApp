from sys import exit
import getpass
import mask_password

from classes import User, Account, Movement, Transaction


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
def home(user):
    print()
    # TODO: change default account parameters for DB data
    account = Account(0, 0, 'MXN')
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
                pass
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
        temp_email = input("Email: ")
        temp_pass = input("Password: ")
        # TODO: Add search function from DB


def register():
    print()
    print("*Register*")
    while True:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        while True:
            temp_password = mask_password.hide_pass()   # Prevent password from showing input
            password = mask_password.hide_pass(prompt='Confirm Password: ')
            if password == temp_password:
                break
            else:
                print("Error. Password doesn't match")
        while True:
            confirm = input("Is your information correct? (y/n)>>")
            if confirm == 'y':
                user = User(first_name, last_name, email, password)
                home(user)
                # TODO: Add function to save to DB

                break
            elif confirm == 'n':
                print()
                break
            else:
                print("Invalid Option\n")
        if confirm == 'y': break


if __name__ == '__main__':
    main()

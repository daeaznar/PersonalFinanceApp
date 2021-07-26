from sys import exit

from classes import User, Account, Movement, Transaction

def main():
    print("====== Welcome to the Personal Finance App ======\n")
    while True:
        print("""
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
                break
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


    
def home(user):
    print()
    # TODO: change default parameters for DB data
    account = Account(0, 0, 'mxn')
    print(f"""
===========================================================
                                    Currency: {account._currency}
            Welcome {user.first_name} {user.last_name}!
                            
        Total Balance: {account.balance}                      
        Savings: {account._savings}
    
===========================================================
    """)
    while True:
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
            pass


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
        password = input("Password: ")

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

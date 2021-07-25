from sys import exit

from classes import User, Account, Movement, Transaction


def home(user):
    print()
    print(f"Welcome {user.first_name}!\n")
    print(user)


def login():
    print()
    print("*Login*")


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


if __name__ == '__main__':
    print("***Welcome to the Personal Finance App***\n")
    while True:
        print("Please select an option to continue (0 for exit)\n"
              "1. Login\n"
              "2. Register")
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

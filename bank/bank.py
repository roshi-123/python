from user import User
from manager import Manager
from operations import Operations

class Bank:
    def __init__(self):
        self.user_list = []
        self.activate_list = []

    def banking(self):
        m = Manager()
        while True:
            print("Select options from the list below:")
            print("1 -> Management")
            print("2 -> User")
            print("3 -> Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                user = input("Enter manager name: ")
                pswd = input("Enter password: ")
                login_status = m.verify(user, pswd)
                print(login_status)
                if login_status == "Successfully logged in":
                    print("Do you want to check activation records? (y/n)")
                    y_n = input()
                    if y_n.lower() == "y":
                        if self.activate_list:
                            for user in self.activate_list:
                                print(m.user_activation_status(user, self.activate_list))
                        else:
                            print("No activation requests available.")

            elif choice == "2":
                print("Select options from the list below:")
                print("1 -> User Registration")
                print("2 -> User Login")
                print("3 -> Account Activation")
                option = input("Enter choice: ")

                if option == "1":
                    user = User()
                    self.user_list.append(user)
                    name = input("Enter username: ")
                    password = input("Enter password: ")
                    user.set_name(name)
                    user.set_password(password)
                    print("Registration successful!")

                elif option == "2":
                    name = input("Enter username: ")
                    password = input("Enter password: ")
                    for user in self.user_list:
                        if user.get_name() == name and user.get_password() == password:
                            if user.get_status() == "active":
                                print("Login successful!")
                                op = Operations()
                                while True:
                                    print("Select options from the list below:")
                                    print("1 -> Deposit")
                                    print("2 -> Withdrawal")
                                    print("3 -> Bank Balance")
                                    print("4 -> Exit")
                                    no = input("Enter choice: ")

                                    if no == "1":
                                        depo = int(input("Enter deposit amount: "))
                                        print(op.deposit(user.get_amount(), depo, user))
                                    elif no == "2":
                                        withdraw = int(input("Enter withdrawal amount: "))
                                        print(op.withdrawal(user.get_amount(), withdraw, user))
                                    elif no == "3":
                                        print(op.balance(user))
                                    elif no == "4":
                                        break
                                    else:
                                        print("Invalid option. Try again.")
                            else:
                                print("Account is not activated. Please request activation.")
                            break
                    else:
                        print("Invalid username or password.")

                elif option == "3":
                    name = input("Enter username for activation: ")
                    for user in self.user_list:
                        if user.get_name() == name:
                            self.activate_list.append(user)
                            print("Activation request submitted.")
                            break
                    else:
                        print("User not found.")

                else:
                    print("Invalid option. Please enter a valid one.")

            elif choice == "3":
                print("Thank you for visiting!")
                exit(0)

            else:
                print("Invalid choice. Please try again.")
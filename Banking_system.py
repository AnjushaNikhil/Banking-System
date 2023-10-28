class Bank_Account:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password, balance):
        if username in self.accounts:
            print("This username is already in use.")
        else:
            self.accounts[username] = {
                'password': password,
                'balance': balance
            }
            return username
    def login(self, username, password):
        if username in self.accounts and self.accounts[username]['password'] == password:
            return self.accounts[username]
        else:
            return None

    def deposit(self, username, amount):
        if username in self.accounts:
            if amount > 0:
                self.accounts[username]['balance'] += amount
                print(f"Deposited Rs. {amount}. New balance: Rs. {self.accounts[username]['balance']}")
                return "Deposit Successful"
            else:
                print("Invalid deposit amount.")
        else:
            return "Invalid Username"

    def withdraw(self, username, amount):
        if username in self.accounts:
            if 0 < amount <= self.accounts[username]['balance']:
                self.accounts[username]['balance'] -= amount
                print(f"Withdrew Rs. {amount}. New balance: Rs. {self.accounts[username]['balance']}")
                return "Withdrawal Successful"
            else:
                print("Invalid withdrawal amount.")
        else:
            return "Invalid Username"

    def check_balance(self, username):
        if username in self.accounts:
            print(f"Current balance: Rs. {self.accounts[username]['balance']}")


def main():
    bank = Bank_Account()
    customer_list = [
        {"username": "Anjusha", "password": "Anju0605", "balance": 10000.00},
        {"username": "Arwin Rudra", "password": "Arw0611", "balance": 1000.00},
        {"username": "Nikhil", "password": "nikz123", "balance": 20000.00},
        {"username": "Greeshma", "password": "chippy456", "balance": 500.00},
        {"username": "Fathima Parwin", "password": "pathz123", "balance": 600.00}
    ]

    for customer in customer_list:
        bank.create_account(customer["username"], customer["password"], customer["balance"])

    while True:
        print("Welcome to the Banking System")
        print("***********")
        print("1. Log in")
        print("2. Create a new account")
        print("3. Exit")
        opt = input("Choose an option: ")

        if opt == '1':
            username = input("Enter Your Username: ")
            password = input("Enter your password: ")
            account = bank.login(username, password)

            if account:
                print(f"Welcome, {username}!")
                while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    opt = input("Choose an option: ")

                    if opt == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        deposit_amnt = bank.deposit(username, amount)
                        print(deposit_amnt)
                    elif opt == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        print(bank.withdraw(username, amount))
                    elif opt == '3':
                        bank.check_balance(username)
                    elif opt == '4':
                        print("Logged out")
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("Invalid username or password. Try again.")
        elif opt == '2':
            username = input("Enter your name: ")
            password = input("Enter a password: ")
            balance = float(input("Enter balance: "))
            created_username = bank.create_account(username, password, balance)
            if created_username:
                print(f"Your account has been created successfully with the username {created_username}")
        elif opt == '3':
            print("Logged out")
            break
        else:
            print("Invalid choice. Try again.")



main()
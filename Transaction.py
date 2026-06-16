
class account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def credit(self):
        print("Available balance is", self.bal)
        c = int(input("Enter amount to credit: "))
        self.bal += c
        print("Updated balance is", self.bal)

    def debit(self):
        print("Available balance is", self.bal)
        d = int(input("Enter amount to debit: "))

        if d > self.bal:
            print("Insufficient balance")
        else:
            self.bal -= d
            print("Updated balance is", self.bal)

    def balance(self):
        return self.bal


accounts = {}
account_count = 0

while True:
    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Show All Accounts")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        bal = int(input("Enter initial balance: "))

        account_count += 1
        acc_no = "ACC" + str(account_count)

        accounts[acc_no] = account(bal, acc_no)

        print("Account created successfully!")
        print("Your Account Number is:", acc_no)

    elif choice == 2:
        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:
            current_user = accounts[acc_no]

            while True:
                print("\n--- ACCOUNT MENU ---")
                print("1. Credit")
                print("2. Debit")
                print("3. Check Balance")
                print("4. Logout")

                op = int(input("Enter choice: "))

                if op == 1:
                    current_user.credit()

                elif op == 2:
                    current_user.debit()

                elif op == 3:
                    print("Available Balance =", current_user.balance())

                elif op == 4:
                    print("Logged out successfully!")
                    break

                else:
                    print("Invalid choice")

        else:
            print("Account not found!")

    elif choice == 3:
        if len(accounts) == 0:
            print("No accounts available")
        else:
            print("\nAll Accounts:")
            for acc_no in accounts:
                print(acc_no)

    elif choice == 4:
        print("Thank you for using the bank system!")
        break

    else:
        print("Invalid choice")
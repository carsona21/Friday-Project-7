class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


def main():
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number)

    while True:
        print("\nOptions:")
        print("(a) Deposit Money")
        print("(b) Withdraw Money")
        print("(c) Check Balance")
        print("(d) Exit")

        choice = input("Choose an option (a/b/c/d): ").strip().lower()

        if choice == 'a':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 'b':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 'c':
            account.check_balance()
        elif choice == 'd':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the program
if __name__ == "__main__":
    main()

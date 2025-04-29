

class BankAccount:
    def __init__(self, initial_balance, account_number):
        self.__account_balance = initial_balance
        self.__account_number = account_number

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            #print(f"Deposited ${amount:.2f}. New Balance: ${self.__account_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            #print(f"Withdrew ${amount:.2f}. New Balance: ${self.__account_balance:.2f}")
        else:
            print("Error: Insufficient balance for withdrawal.")

    def get_balance(self):
        return self.__account_balance


# Create an instance of BankAccount
account1 = BankAccount(initial_balance=1000.0, account_number="123456789")

# Perform transactions
account1.deposit(500.0)
account1.withdraw(200.0)

# Print final account balance
print("Final Account Balance:", account1.get_balance())
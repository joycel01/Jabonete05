class BankAccount:
    def __init__(self,account_number,owner,balance):
        self.account_number=account_number
        self.owner=owner
        self.balance=balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited: Php.{amount} \nNew Balance Php.{self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw: Php.{amount}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account balance: Php.{self.balance}")
        
my_account = BankAccount(1018737, "Beabadoobee", 5000)

my_account.deposit(4500)
my_account.withdraw(2500)
my_account.display_balance()
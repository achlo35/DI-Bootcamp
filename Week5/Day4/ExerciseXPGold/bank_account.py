class BankAccount():
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        else:
            raise ValueError('Invalid username or password')

    def deposit(self, amount):
        if amount  < 0:
            raise ValueError('Invalid Deposit amount')
        elif self.authenticated == False:
            raise Exception('Authentication required for Deposit')        
        elif amount > 0 and self.authenticated == True:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Invalid Withdraw amount')
        elif self.balance < amount:
            raise ValueError('Insufficient funds')
        elif amount > 0 and self.authenticated == True and self.balance >= amount:
            self.balance -= amount
            return self.balance
        
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise ValueError('Insufficient funds, Minimum balance not met')
        else:
            return super().withdraw(amount)
        
    

# Test code
acct = MinimumBalanceAccount(100, "user1", "pass1", minimum_balance=50)
try:
    acct.deposit(50)  # Should raise authentication error
except Exception as e:
    print(e)

acct.authenticate("user1", "pass1")
print("Authenticated:", acct.authenticated)
print("Deposit:", acct.deposit(50))  # Should work
try:
    print("Withdraw:", acct.withdraw(120))  # Should raise minimum balance error
except Exception as e:
    print(e)
print("Withdraw:", acct.withdraw(50))  # Should work
print("Final balance:", acct.balance)
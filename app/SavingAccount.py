

class SavingAccount:
    current_amount: int

    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def deposit(self, amount):
        self.current_amount += amount 

    def withdraw(self, amount):
        if self.current_amount - amount < 0:
            return "Insufficient balance"
        else:            
            self.current_amount -= amount
            return "Successful withdrawal"
    
    @staticmethod
    def isOneYearWithoutWithdrawal(amount):
        return amount + (amount * 0.4)

    @staticmethod
    def isOneYearWithWithdrawal(amount):
        return amount + (amount * 0.02)

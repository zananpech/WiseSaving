from _typeshed import Self


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
     
    def isOneYearWithoutWithdrawal(self):
        #TODO
        #we want to check if user keeps their money for one year without withdrawal, 
        #if this is true, amount in the account will multiple 4% of interest after one year.
        return

    def isOneYearWithWithdrawal(self):
        #TODO
        # if user cannot keep for one year, they make transfer or withdraw, then user lose 4% interest after
        # that interest for them is 0.20%
        return 

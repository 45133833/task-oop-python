# bank system project oop

class accont:
    def __init__(self, number_account ,balance):
        self.number_account =number_account 
        self.balance=balance
        
    def Deposit(self , amount):
        if amount < 0:
            print("there is no money")
        else:
            amount += self.balance

    def Withdraw(self , amount):
        if amount>0 and amount<self.balance:
            self.balance -= amount
        else:
            print("there is no money")
    
    def Transfer(self, amount, ontherAccount):
        if self.Withdraw(amount):
            ontherAccount.Deposit(amount)
        else:
            print("there is no money")

class SavingsAccount(accont):
    pass




            
            
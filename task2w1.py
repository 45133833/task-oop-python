# bank system project oop

class accont:
    def __init__(self, number_account ,balance):
        self.number_account =number_account 
        self.balance=balance
        self.transactins=[]
        print(self.transactins)
        
    def Deposit(self , amount):
        if amount < 0:
            print("there is no money")
        else:
            self.balance += amount
            self.transactins.append( self.balance)
            print(self.transactins)



    def Withdraw(self , amount):
        if amount>0 and amount<self.balance:
            self.balance -= amount
            self.transactins.append( self.balance)
            print(self.transactins)
        else:
            print("there is no money")
    
    def Transfer(self, amount, ontherAccount):
        if self.Withdraw(amount):
            ontherAccount.Deposit(amount)
            self.transactins.append( self.balance)
            print(self.transactins)
        

class SavingsAccount(accont):
    
    pass



myacc_savings = SavingsAccount("Someone1", 1000)

myacc_savings.Deposit(500)
myacc_savings.Withdraw(400)
myacc_savings. Transfer(200, "Someone2")


            
            
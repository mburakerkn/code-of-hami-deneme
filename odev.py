class BankAcc :
    def __init__(self,name):
        self.name = "Adana merkez"
        self.__balance = 0

    def deposit(self,amount):
        self.__balance += amount
    
a = BankAcc("anan")
a.deposit(100)
print(a.__balance)
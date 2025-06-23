class bankaccount():
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def withdrwa(self,amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
cc = bankaccount("Vicky", 1000)

cc.deposit(500)             # balance = 1500
cc.withdrwa(400)            # balance = 1100
cc.withdrwa(2000)           # Should print: Insufficient funds
print(cc.get_balance())   
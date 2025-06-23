class bankaccount():
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposits(self,amount):
        if amount>0:
            self.__balance += amount
            print("amount deposited")
        else:
            ("invalid deposit")
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("withdrawl is completed")
        else:
            print("invalid withdrawal")
d=bankaccount("dharu",1000)
print("intial balance:",d.get_balance())
d.deposits(500)
print("after deposit:",d.get_balance())
d.withdraw(200)
print("after withdraw:", d.get_balance())
    
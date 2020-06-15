class Bank:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def get_balance(self):
        print("Get balance")
        return self._balance

    def set_balance(self, value):
        print("Get balance")
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self._balance = value

    def delete_balance(self):
        print("delete balance")
        del self._balance

    # balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    my_balance = property()
    my_balance = my_balance.getter


bank = Bank("Alfa", 2000)
bank.set_balance(2222)
bank.get_balance()
print(bank.name)




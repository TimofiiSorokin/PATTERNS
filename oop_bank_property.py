# PROPERTY


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def my_balance(self):
        print("Get balance")
        return self._balance

    @my_balance.setter
    def my_balance(self, value):
        print("Set balance")
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        self._balance = value

    @my_balance.deleter
    def my_balance(self):
        print("delete balance")
        del self._balance


bank = Bank("Alfa", 2000)
bank.my_balance = 2100
print(bank.my_balance)
del bank.my_balance
bank.my_balance = 2600
print(bank.my_balance)



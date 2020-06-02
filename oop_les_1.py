class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name, age)

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


d = Dog("Tim", 14)
d2 = Dog("Tim", 14)
d.set_name("RED")
print(f"This is a sting { d.get_name() } { d.age }")
# d2 = Dog("BigTim")
# print(type(d))


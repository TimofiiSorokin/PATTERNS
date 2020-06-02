# Animals =)))


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"This animal has a name {self.name} and he is {self.age} years old")

    def speak(self):
        print("I dont know what to say")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age,)
        self.color = color

    def show(self):
        print(f"This animal has a name {self.name} and he is {self.age} years old and have {self.color} color")


d1 = Pet("PetName", 9)
d1.show()
d1.speak()
d2 = Cat("CatName", 8)
d2.show()
d3 = Pet("DogName", 8)
d3.show()

d4 = Fish("FishName", 8, "red")
d4.show()

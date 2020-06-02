# @classmethod example


class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Bil")
p3 = Person("Anna")
print(Person.number_of_people)
p4 = Person("Artur")
print(Person.number_of_people)
print(Person.number_of_people_())

# class Person:
#     number_of_people = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.number_of_people += 1
#
#
# p1 = Person("Tim")
# print(p1.number_of_people)
# p2 = Person("Bill")
# print(p2.number_of_people)
# p3 = Person("Anna")
# print(p1.number_of_people)
# print(p3.number_of_people)
#
# print(Person.number_of_people)

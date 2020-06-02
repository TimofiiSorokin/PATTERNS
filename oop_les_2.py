# Get get average grade from the student
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


d1 = Student("Tim", 21, 89)
d2 = Student("Bill", 33, 93)
d3 = Student("Anna", 23, 77)

course = Course("Geometry", 2)
course.add_student(d1)
course.add_student(d2)
print(course.get_average_grade())


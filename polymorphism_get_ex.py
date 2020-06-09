# request to polymorphism_class_ex.py

from polymorphism_class_ex import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(7, 12)
# print(rect1.get_rect_area(), rect2.get_rect_area())

sq1 = Square(3)
sq2 = Square(9)
# print(sq1.get_sq_area(), sq2.get_sq_area())

r1 = Circle(5)
r2 = Circle(7)
# print(r1.get_circle_area(), r2.get_circle_area())

figures = [rect1, rect2, sq1, sq2, r1, r2]
for figure in figures:
    # if isinstance(figure, Rectangle):
    #     print(figure.get_rect_area())
    # elif isinstance(figure, Square):
    #     print(figure.get_sq_area())
    # else:
    #
    print(figure.get_area())

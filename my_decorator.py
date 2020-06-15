# Decorator
def funk(new_funk):
    def red_funk():
        print("WWWWWWWWWWWWWWW")
        new_funk()
        print("AAAAAAAAAAa")
        return ""

    return red_funk


# def for_new_funk():
#     print("Привет!!!")
#
#
# new_bank = funk(for_new_funk)
# print(new_bank())

@funk
def for_new_funk():
    print("Привет!!!")

print(for_new_funk())


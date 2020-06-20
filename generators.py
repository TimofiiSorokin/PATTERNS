def function():
    print("Let me go get that number for you.")
    yield 4


num = function()
num2 = next(num)
print(num2)


# def gimme4_please():
#     print("Let me go get that number for you.")
#     return 4
#
#
# num = gimme4_please()
# print(num)

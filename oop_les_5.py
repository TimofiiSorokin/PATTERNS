class Math:

    @staticmethod
    def add(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")


print(Math.add10(2))
Math.pr()
print(Math.add(2))

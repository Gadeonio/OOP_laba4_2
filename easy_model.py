class EModel:
    def __init__(self, a, b):
        self.__a = 0
        self.__b = 0
        self.set_a(a)
        self.set_b(b)


    def set_a(self, a):
        self.__a = a
        self.is_incorrect(self.__a)
        self.check_b_for_a()

    def set_b(self, b):
        self.__b = b
        self.is_incorrect(self.__b)
        self.check_b_for_a()

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def is_incorrect(self, num):
        if num < 0:
            num = 0
        elif num > 100:
            num = 100

    def check_b_for_a(self):
        if self.__b < self.__a:
            self.__b = self.__a
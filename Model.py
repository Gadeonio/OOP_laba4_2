class Model:

    def __init__(self, a=0, b=0, c=0):
        self.__a = 0
        self.__b = 0
        self.__c = 0

        self.set_c(c)
        self.set_b(b)
        self.set_a(a)

    def set_a(self, a):
        self.__a = a
        self.is_incorrect(self.__a)
        self.check_b_for_a()

    def set_b(self, b):
        self.__b = b
        self.check_b_for_a()
        self.check_b_for_c()

    def set_c(self, c):
        self.__c = c
        self.is_incorrect(self.__c)
        self.check_b_for_c()

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def is_incorrect(self, num):
        if num < 0:
            num = 0
        elif num > 100:
            num = 100

    def check_b_for_a(self):
        if self.__b < self.__a:
            save_b = self.__b
            self.__b = self.__a
            if self.__b >= self.__c:
                self.__b = self.__c
                self.__a = self.__b

    def check_b_for_c(self):
        if self.__b > self.__c:
            save_b = self.__b
            self.__b = self.__c
            if self.__b < self.__a:
                self.__b = self.__a
                self.__c = self.__b







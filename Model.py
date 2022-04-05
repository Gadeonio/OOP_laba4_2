class Model:
#a, b, c должны быть property

    def __init__(self, a=0, b=0, c=0):
        self.__a = 0
        self.__b = 0
        self.__c = 0

        self.c = c
        self.b = b
        self.a = a

    @property
    def a(self) -> int:
        return self.__a

    @property
    def b(self) -> int:
        return self.__b

    @property
    def c(self) -> int:
        return self.__c

    @a.setter
    def a(self, a: int):
        self.__a = a
        self.is_incorrect(self.__a)
        self.check_b_for_a()

    @b.setter
    def b(self, b: int):
        self.__b = b
        self.check_b_for_a()
        self.check_b_for_c()

    @c.setter
    def c(self, c: int):
        self.__c = c
        self.is_incorrect(self.__c)
        self.check_b_for_c()

    def is_incorrect(self, num: int):
        if num < 0:
            num = 0
        elif num > 100:
            num = 100

    def check_b_for_a(self):
        if self.__b < self.__a:
            self.__b = self.__a
            if self.__b >= self.__c:
                self.__b = self.__c
                self.__a = self.__b

    def check_b_for_c(self):
        if self.__b > self.__c:
            self.__b = self.__c
            if self.__b < self.__a:
                self.__b = self.__a
                self.__c = self.__b

    def parse_file(self, name: str):
        with open(name, 'r') as f:
            stroka = f.read()
            a = int(stroka[:stroka.index(" ")])
            stroka = stroka[stroka.index(" ") + 1:]
            b = int(stroka[:stroka.index(" ")])
            stroka = stroka[stroka.index(" ") + 1:]
            c = int(stroka)
            self.c = c
            self.b = b
            self.a = a


    def save_file(self, name: str):
        with open(name, 'w') as f:
            f.write(str(self.a) + " " + str(self.b) + " " + str(self.c))









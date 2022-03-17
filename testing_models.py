from Model import Model
from easy_model import EModel

if __name__=="__main__":
    #emodel = EModel(0, 0)
    emodel = Model(30, 20, 50)
    print(emodel.get_a())
    print(emodel.get_b())
    print(emodel.get_c())
    print()
    while True:
        string = input()
        num = int(input())
        if string == "a":
            emodel.set_a(num)
        elif string == "b":
            emodel.set_b(num)
        else:
            emodel.set_c(num)
        print(emodel.get_a())
        print(emodel.get_b())
        print(emodel.get_c())
        print()



class Shundarban:
    def __init__(self):
        print("__init__of Shundarban")
    def fun1(self):
        print("from Shundarban")

class Sa:
    def __init__(self):
        print("__init__of Sa")

    def fun1(self):
        print("from Sa")

class curiar(Shundarban, Sa):
    print("__init__of curiar")
    def fun2(self):
        print("from curiar")

c1 = curiar()
c1.fun1()
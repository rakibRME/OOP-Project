class Data:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __ne__(self, other):
        if(self.a != other.a):
            return ( "not equal")
        else:
            return ( "equal")

    # def view(self):
    #     print("Number of door ", self.a, " and window ",self.b)

d1 = Data(100, 100)
d2 = Data(1000, 2)
print(d1 != d2)
#new.view()


class mull:
    def multiplication(self, *numbers):
        result = 1
        for i in numbers:
            result = result * i
        print(result)

obj = mull()
obj.multiplication(13,4)


# class mull:
#     def multiplication(self, a, b = None, c = None):
#         if a != None and b != None and c!= None:
#             print(a * b * c)
#         elif (a != None and b != None):
#             print(a * b)
#         else:
#             print(a)
#
# obj = mull()
# obj.multiplication(1)
# obj.multiplication(1,2)
# obj.multiplication(1,2,3)

class student:
    def __init__(self, **data):
        if len(data) == 3:
            self.name = data['name']
            self.roll = data['roll']
            self.cg = data['cg']

        elif len(data) == 2:
            self.name = data['name']
            self.roll = data['roll']

        else:
            self.name = data['name']

        print("HA")

s1 = student(roll = 22, cg = 3.22,name = "rakib")
s2 = student(name = "raki",roll = 2)
s3 = student(name = "rak")


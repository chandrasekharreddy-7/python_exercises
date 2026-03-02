class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def details(self):
           return f"x : {self.x} and y : {self.y}"
    def scale(self, value):
        self.x *= value
        self.y *= value
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    def add_complex(self, other_object):            # other_object carries the reference of c2 
        c4 = complex(0, 0)                          # c4 is a new object of class complex               
        c4.x = self.x + other_object.x              # self carries the reference of c1
        c4.y = self.y + other_object.y
        return c4
    def sub_complex(self, other_object):
        c4 = complex(0, 0)
        c4.x = self.x - other_object.x
        c4.y = self.y - other_object.y
        return c4
    def mult_complex(self, other_object):
        c4 = complex(0, 0)
        c4.x = self.x * other_object.x - self.y * other_object.y
        c4.y = self.x * other_object.y + self.y * other_object.x
        return c4
# c1 = complex(2, 3)
# c2 = complex(4, 5)
# print(c1.details())
# print(c2.details())
# print("magnitude of c1 = ", f"{c1.magnitude():.4f}")
# c3 = c1.add_complex(c2)
# print(c3.details())
# print(c2.details())
# c3 = c1.sub_complex(c2)
# print(c3.details())
# c3 = c1.mult_complex(c2)
# print(c3.details())
# print(type(c1))
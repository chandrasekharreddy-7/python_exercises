# list
class my_list():
    def __init__(self):
        self.l = [0,0,0,0,0,0,0,0,0,0]
        self.count = 0
    def my_append(self, value):
        self.l[self.count] = value
        self.count += 1
    def print_list(self):
        print("[",end = "")
        for i in range(self.count):
            if i != self.count - 1:
                print(self.l[i], end = ",")
            else:
                print(f"{self.l[i]}]",end = " ")
    def insert(self, value, index):
        i = self.count
        while i > index:
            self.l[i] = self.l[i - 1]
            i -= 1
        self.count += 1
        self.l[index] = value
l1 = my_list()
l1.my_append(4)
l1.my_append(64)
l1.my_append(24)
l1.my_append("CHANDRA")
l1.my_append("SIVA")
l1.print_list()
i1 = l1.insert(2,5)
print(l1.print_list())
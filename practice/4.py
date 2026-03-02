class Termmarks:
    def __init__(self, term1 = 0, term2 = 0, term3 = 0):
        self.__Term1 = term1
        self.__Term2 = term2
        self.__Term3 = term3
        if self.__Term1 < 0:
            self.__Term1 = 0
        else:
            self.__Term1 = term1
        if self.__Term2 < 0:
            self.__Term2 = 0
        else:
            self.__Term2 = term2
        if self.__Term3 < 0:
            self.__Term3 = 0
        else:
            self.__Term3 = term3
    def __str__(self):
        return f"Term 1 = {self.__Term1}\nTerm 2 = {self.__Term2}\nTerm3 = {self.__Term3}"
    def average(self):
        avg = (self.__Term1 + self.__Term2 + self.__Term3) / 3
        return f"average of term1, term2, term3 marks = {avg}"
    def maximum(self):
        if self.__Term1 >= self.__Term2 and self.__Term1 >= self.__Term3:
            return f"maximum of {self.__Term1}, {self.__Term2} and {self.__Term3} = {self.__Term1}"
        elif self.__Term2 >= self.__Term1 and self.__Term2 >= self.__Term3:
            return f"maximum of {self.__Term1}, {self.__Term2} and {self.__Term3} = {self.__Term2}"
        elif self.__Term3 >= self.__Term1 and self.__Term3 >= self.__Term2:
            return f"maximum of {self.__Term1}, {self.__Term2} and {self.__Term3} = {self.__Term3}"
        else:
            return None
s1 = Termmarks(50,-20,30)
print(s1)
a1 = s1.average()
print(a1)
max1 = s1.maximum()
print(max1)
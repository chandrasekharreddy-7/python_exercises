class Termmarks:
    def __init__(self, term1 = 0, term2 = 0, term3 = 0):
        self.__Term1 = term1
        self.__Term2 = term2
        self.__Term3 = term3
        if self.__Term1 < 0:
            self.__Term1 = 0
        else:
            self.__Term1 = term1
        if self.term2 < 0:
            self.__Term2 = 0
        else:
            self.__Term2 = term2
        if self.term3 < 0:
            self.__Term3 = 0
        else:
            self.__Term3 = term3
    def __str__(self):
        return f"Term 1 = {self.__Term1}\nTerm 2 = {self.__Term2}\nTerm3 = {self.__Term3}"
s1 = Termmarks(50,-20,30)
print(s1)
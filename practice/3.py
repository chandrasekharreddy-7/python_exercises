class person:
    def __init__(self, name, age, gender, height):
        self.__name = name            # private attributes.
        self.__age = age              # private attributes.
        self.__gender = gender        # private attributes.
        self.__height = height        # private attributes.
        self.__count = 0              # private attributes.
    def __str__(self):
            return f"name : {self.__name}\nage : {self.__age}\ngender : {self.__gender}\nheight : {self.__height}"
    def details(self):
        return f"name : {self.__name}, age : {self.__age}, gender : {self.__gender}, height : {self.__height}"
    def update_height_and_age(self,age = None, height = None):
        if age is not None:
            self.__age = age
        if height is not None:
            self.__height = height
s1 = person("abc",19,"male",160)
print(s1)
print("\n")      # we want the details from class only, main has no right to change the details.
s1.update_height_and_age(age = 30)
print(s1)
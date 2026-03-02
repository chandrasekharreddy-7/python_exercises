class person:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.count = 0
    def __str__(self):
            return f"name : {self.name}\nage : {self.age}\ngender : {self.gender}\nheight : {self.height}"
    def details(self):
        return f"name : {self.name}, age : {self.age}, gender : {self.gender}, height : {self.height}"
    def update_height_and_age(self):
        choice = int(input("enter 1 to update height and 0 to exit :"))
        if choice == 1:
            height = int(input("enter new height :"))
            self.height = height
            print("height updated successfully")
        print("enter 1 to update age and 0 to exit :")
        choice = int(input())       
        if choice == 1:
            age = int(input("enter new age :"))
            self.age = age
            print("age updated successfully")
        else:
            return
s1 = person("abc",19,"male",160)
print(s1)
print("\n")
s1.update_height_and_age()
print(s1)
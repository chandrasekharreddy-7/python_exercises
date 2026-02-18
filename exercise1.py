''' Write a program that takes the radius of a circle as input and computes its area.
Note: If the radius is non-negative, display an appropriate message. '''
# r = float(input("enter radius of circle :"))
# if r >= 0:
#     pi = 3.14
#     area = pi * r * r
#     print(f"area of circle = {area}")
# else:
#     print("radius is in non - negative.")


''' Write a program that takes two integers a and b as input and prints their sum, difference,
product, quotient, and remainder. '''
# a = int(input("enter 1st integer :"))
# b = int(input("enter 2nd integer :"))
# sum = a + b
# diff = a - b
# pro = a * b
# print(f"sum of {a} and {b} = {sum}")
# print(f"difference of {a} and {b} = {diff}")
# print(f"product of {a} and {b} = {pro}")
# if b == 0:
#     print("0 is in denominator., quotient undefined.")
# else:
#     print(f"quotient of {a} and {b} = {a/b}")
# if b == 0:
#     print("0 is in denominator., remainder undefined.")
# else:
#     print(f"remainder of {a} and {b} = {a%b}")


''' Write a simple calculator program. It should be able to add, subtract, multiply, and divide
any two numbers input by the user.
Note: The user will also specify the operation to perform. '''
''' PROCESS - 1 '''
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# print("you can perform below operations on entered two numbers.")
# print("1. ADDITION")
# print("2. DIFFERENCE")
# print("3. PRODUCT")
# print("4. DIVISION")
# c = int(input("enter your choice from above options :"))
# if c == 1:
#     sum = a + b
#     print(f"sum of {a} and {b} = {sum}")
# elif c == 2:
#     difference = a - b
#     print(f"difference of {a} and {b} = {difference}")
# elif c == 3:
#     product = a * b
#     print(f"product of {a} and {b} = {product}")
# elif c == 4:
#     division = a / b
#     print(f"division of {a} and {b} = {division}")
# else:
#     print("please enter correct choice.")

''' PROCESS - 2 '''
# num1 = int(input("enter 1st integer :"))
# num2 = int(input("enter 2nd integer :"))
# print("you can perform below operations on entered two numbers.")
# print("1. ADDITION")
# print("2. DIFFERENCE")
# print("3. PRODUCT")
# print("4. DIVISION")
# c = int(input("enter your choice from above options :"))
# match(c):
#     case 1:
#         sum = num1 + num2
#         print(f"sum of num1 and num2 = {sum}")
#     case 2:
#         difference = num1 - num2
#         print(f"difference of num1 and num2 = {difference}")
#     case 3:
#         product = num1 * num2
#         print(f"product of num1 and num2 = {product}")
#     case 4:
#         try:
#             division = num1 / num2
#             division1 = num1 // num2
#             print(f"division of num1 and num2 = {division}")
#             print(f"division(int) of num1 and num2 = {division1}")
#         except :
#             print("division by zero is undefined.")
#     case _:
#         print("please enter correct choice.")


''' Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter.
Note: If the inputs are invalid, display an appropriate message. '''
''' PROCESS - 1 '''
# length = int(input("enter the length of rectangle (non - negative) :"))
# breadth = int(input("enter the breadth of rectangle (non - negative) :"))
# if length < 0 or breadth < 0:
#     print("please check length or breadth is in negative integer")
# else :
#     area = length * breadth
#     perimeter = 2 * (length + breadth)
#     print(f"area of rectangle with dimensions [{length}][{breadth}] = {area}")
#     print(f"perimeter of rectangle with dimensions [{length}][{breadth}] = {perimeter}")


''' PROCESS - 2 '''
# def areaofrectangle(length,breadth):
#     area = length * breadth
#     return area
# def perimeterofrectangle(length,breadth):
#     perimeter = 2 * (length + breadth)
#     return perimeter
# length = int(input("enter the length of rectangle (non - negative) :"))
# breadth = int(input("enter the breadth of rectangle (non - negative) :"))
# if length < 0 or breadth < 0:
#     print("please check length or breadth is in negative integer")
# else:
#     print(f"area of rectangle with dimensions [{length}][{breadth}] = {areaofrectangle(length,breadth)}")
#     print(f"perimeter of rectangle with dimensions [{length}][{breadth}] = {perimeterofrectangle(length,breadth)}")


''' Write a program that takes an integer as input, and displays whether this integer is negative,
positive, or zero. '''
''' PROCESS - 1 '''
# integer = int(input("enter an integer(to check negative, positive, or zero ) :"))
# if integer == 0:
#     print("entered number is 0.")
# elif integer < 0:
#     print(f"entered integer {integer} is negative.")
# elif integer > 0:
#     print(f"entered integer {integer} is positive.")
# else :
#     print("please enter an integer.")


''' PROCESS - 2 '''
# def integercheck(number):
#     if number == 0:
#         print("entered integer is 0.")
#     elif number < 0:
#         print(f"entered integer {number} is negative")
#     elif number > 0:
#         print(f"entered integer {number} is positive.")
#     else :
#         print("please enter an integer.")
# number = int(input("enter an integer (to check negative, positive, or zero) :"))
# integercheck(number)


''' Write a program that takes two integers a and b as input and displays whether a < b, a = b,
or a > b. '''
''' PROCESS - 1 '''
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# print(f"relation between {a} and {b} is :")
# if a > b:
#     print(f"result : {a} > {b}")
# elif a < b:
#     print(f"result : {a} < {b}")
# elif a == b:
#     print(f"result : {a} = {b}")
# else :
#     print("please enter number in both a and b")

''' PROCESS - 2 '''
# def equitycheck(a,b):
#     if a > b:
#         print(f"relation : {a} > {b}.")
#     elif a < b:
#         print(f"result : {a} < {b}")
#     elif a == b:
#         print(f"result : {a} = {b}")
#     else :
#         print("please enter number in both a and b")
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# equitycheck(a,b)


''' Write a program that takes three integers as input and prints their maximum value. '''
''' PROCESS - 1 '''
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# c = int(input("enter the 3rd number :"))
# if a >= b and a >= c:
#     print(f"{a} is maximum in {a},{b} and {c}")
# elif b >= a and b >= c:
#     print(f"{b} is maximum in {a},{b} and {c}")
# elif c >= a and c >= b:
#     print(f"{c} is maximum in {a},{b} and {c}")
# else :
#     print("enter three integers only.")


''' PROCESS - 2 '''
# def maxofthree(a,b,c):
#     if a >= b and a >= c:
#         print(f"{a} is maximum in {a},{b} and {c}")
#     elif b >= a and b >= c:
#         print(f"{b} is maximum in {a},{b} and {c}")
#     elif c >= a and c >= b:
#         print(f"{c} is maximum in {a},{b} and {c}")
#     else :
#         print("enter three integers only.")
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# c = int(input("enter the 3rd number :"))
# maxofthree(a,b,c)


''' Q8 : Write a program that takes a three-digit integer as input and prints the sum of its digits. '''
''' PROCESS - 1 '''
# num = int(input("enter any integer number :"))
# org_num = num
# sum = 0
# while num > 0:
#     remainder = num % 10
#     sum = sum + remainder
#     num = num // 10
# print(f"sum of digits in {org_num} = {sum}")


''' PROCESS - 2 '''
# def sumofdigits(num):
#     org_num = num
#     sum = 0
#     while num > 0:
#         remainder = num % 10
#         sum = sum + remainder
#         num = num // 10
#     return sum
# num = int(input("enter any integer number :"))
# print(f"sum of digits in {num} = {sumofdigits(num)}")


''' Q9 : Write a program that takes the marks for 5 subjects as input and calculates the total and
average marks. '''
# c = int(input("enter the marks in C programming :"))
# calculus = int(input("enter the marks in calculus :"))
# python = int(input("enter the marks in python :"))
# maths = int(input("enter marks in maths :"))
# ct = int(input("enter marks obtained in ct :"))
# totalmarks = c + calculus + python + maths + ct
# averagemarks = totalmarks / 5
# print(f"total no of marks obtained = {totalmarks}")
# print(f"average marks obtained = {averagemarks}")


''' Q10 : Write a program that takes three integers as input and prints the minimum (of the three
values). '''
''' PROCESS - 1 '''
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# c = int(input("enter the 3rd number :"))
# if a <= b and a <= c:
#     print(f"{a} is minimum in {a},{b} and {c}")
# elif b <= a and b <= c:
#     print(f"{b} is minimum in {a},{b} and {c}")
# elif c <= a and c <= b:
#     print(f"{c} is minimum in {a},{b} and {c}")
# else :
#     print("enter three integers only.")


''' PROCESS - 2 '''
# def minofthree(a,b,c):
#     if a <= b and a <= c:
#         print(f"{a} is minimum in {a},{b} and {c}")
#     elif b <= a and b <= c:
#         print(f"{b} is minimum in {a},{b} and {c}")
#     elif c <= a and c <= b:
#         print(f"{c} is minimum in {a},{b} and {c}")
#     else :
#         print("enter three integers only.")
# a = int(input("enter the 1st number :"))
# b = int(input("enter the 2nd number :"))
# c = int(input("enter the 3rd number :"))
# minofthree(a,b,c)


''' Q11 : Write a program that takes an integer as input and displays if it is odd or even. '''
''' PROCESS - 1 '''
# number = int(input("enter a number (to check even or odd or zero) :"))
# if number == 0:
#     print("0 is neither even nor odd.")
# elif number % 2 == 0:
#     print(f"{number} is even")
# else :
#     print(f"{number} is odd.")


''' PROCESS - 2 '''
# def evenorodd(number):
#     if number == 0:
#         print("0 is neither even nor odd.")
#     elif number % 2 == 0:
#         print(f"{number} is even")
#     else :
#         print(f"{number} is odd.")
# number = int(input("enter a number (to check even or odd or zero) :"))
# evenorodd(number)


''' Q13 : Write a program that takes an integer as input and checks if it is divisible by 17. '''
''' PROCESS - 1 '''
# number = int(input("enter a number :"))
# divisible = int(input("enter a number to check divisble or not :"))
# if number % divisible == 0:
#     print(f"entered number {number} is divisible with {divisible}")
# else:
#     print(f"entered number {number} is not divisible with {divisible}")


''' PROCESS - 2 '''
# def divisibilitycheck(number,divisor):
#     if number % divisor == 0:
#         print(f"entered number {number} is divisible with {divisor}")
#     else:
#         print(f"entered number {number} is not divisible with {divisor}")
# number = int(input("enter a number :"))
# divisor = int(input(f"enter a divisor to check divisble or not {number} :"))
# divisibilitycheck(number,divisor)


''' Q14 : Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints its
respective grade point (10/9/8/7/6/4). 
Note: If an invalid letter grade is entered, the program should display an appropriate message. '''
# lettergrade = input("enter the letter grede (S/A/B/C/D/E) {to print grade point} : ")
# if lettergrade == 'S':
#     print("For lettergrade 'S', grade point is '10'.")
# elif lettergrade == 'A':
#     print("For lettergrade 'A', grade point is '9'.")
# elif lettergrade == 'B':
#     print("For lettergrade 'B', grade point is '8'.")
# elif lettergrade == 'C':
#     print("For lettergrade 'C', grade point is '7'.")
# elif lettergrade == 'D':
#     print("For lettergrade 'D', grade point is '6'.")
# elif lettergrade == 'E':
#     print("For lettergrade 'E', grade point is '4'.")
# else :
#     print("please enter correct letter grade.")


''' Q15 : Write a program to select one option from the list and display output accordingly.
Example:
Please enter your choice:
1. Check Balance
2. View Offers
3. Special Recharge
Enter 0 to exit
(Display some arbitrary message for each option, e.g., “Your balance is Rs. 500”.) '''
''' *****   ATM PROGRAM   ***** '''
# balance = int(input("enter your balance :"))
# print("Please enter your choice:")
# print("1. Check Balance")
# print("2. credit money")
# print("3. debit money")
# print("4. View offers")
# print("5. Special Recharge")
# print("PRESS '0' TO EXIT")
# c = int(input("enter your choice from above options :"))
# if c == 1:
#     print(f"your current balance = {balance}.")
# elif c == 2:
#     newbalance = 0
#     credit = int(input("enter money you want to credit :"))
#     newbalance = balance + credit
#     print(f"new balance after credit of {credit} rupees = {newbalance}")
# elif c == 3:
#     newbalance = 0
#     debit = int(input("enter money you want to debit :"))
#     if debit > balance:
#         print("your current balance is less than your debiting ammount.")
#     else:
#         newbalance = balance - debit
#         print(f"new balance after debit of {debit} rupees = {newbalance}")
# elif c == 4:
#     print("YOU CAN VIEW OUR RESPECTIVE BANK OFFERS.")
# elif c == 5:
#     print("steps to SPECIAL RECHARGE.")
# elif c == 0:
#     print("YOU LOGGED OUT FROM ATM.")
# else :
#     print("please enter correct choice.")


''' Q16 : Write a program that takes as input the coefficients of the quadratic equation
" ax2 + bx + c = 0 " and prints whether the roots are real or complex. '''
# a = int(input("give coeffecient of x square:"))     
# b = int(input("give coeffecient of x:"))
# c = int(input("give constant value:"))
# root1 = 0
# root2 = 0
# d = b*b - 4 * a * c
# if d > 0:
#     print("the quadratic equation has real and distinct roots.")
# elif d == 0:
#     print("the quadratic equation has real and equal roots.")
# else :
#     print("the quadratic equation has complex (imaginary) roots.")
# if d > 0 or d == 0:
#     root1 = (-b + (d**(0.5))) / 2 * a
#     root2 = (-b - (d**(0.5))) / 2 * a
#     print(f"Roots of the given equation is: {root1,root2}")


''' Q17 : Write a program that takes two 5-letter words as input and finds the sum of the distance
between the respective characters of these words. '''
''' process - 1 '''
# def worddistance(word1,word2):
#     if len(word1) == 5 and len(word2) == 5 and word1.isalpha() and word2.isalpha():
#         sum = 0
#         for i in range(len(word1)):
#             distance = abs(ord(word1[i]) - ord(word2[i]))
#             sum = sum + distance
#         print(sum)
#     else:
#         print("please enter a 5 letter words with upper case or lower case letter.")
# word1 = input("enter a 5 letter word :")
# word2 = input("enter a five letter word :")
# worddistance(word1,word2)


''' process - 2 '''
# word1 = input("enter a 5 - letter word :")
# word2 = input("enter another 5 - letter word :")
# if len(word1) == 5 and len(word2) == 5 and word1.isalpha() and word2.isalpha():
#     sum = 0
#     distance = abs(ord(word1[0]) - ord(word2[0])) + abs(ord(word1[1]) - ord(word2[1])) + abs(ord(word1[2]) - ord(word2[2])) + abs(ord(word1[3]) - ord(word2[3])) + abs(ord(word1[4]) - ord(word2[4]))
#     sum = sum + distance
#     print(f"sum of distance between respective words = {sum}")
# else:
#     print("enter a 5 - letter word")


''' Q18 : Write a program that takes a 2-letter word as input and prints it in capital letters.
Note: Each letter of the input word can be in capital or small letters. '''
''' PROCESS - 1 (only for two letter word.) '''
# word = input("enter a two letter word :")
# length = len(word)
# if length > 2 and length < 2:
#     print("please enter a two - letter word.")
# else:
#     capword = ""
#     for i in word:
#         if i >= 'A' and i <= 'Z':
#             continue
#         else:
#             i = ord(i)
#             i = i - 32
#             i = chr(i)
#             capword = capword + i
#     print(capword)

''' PROCESS - 2(using in built functions.) '''
# word = input("enter a two letter word (to converet into upper case.)")
# length = len(word)
# if length == 2 and word.isalpha():
#     capital = word.upper()
#     print(capital)
# else:
#     print("please enter a two letter word.")


''' Q19 : Write a program that takes a 2-letter word as input and prints it in small letters.
Note: Each letter of the input word can be in capital or small letters. '''
# word = input("enter a two letter word :")
# length = len(word)
# if length > 2:
#     print("please enter a two - letter word.")
# else:
#     smallword = ""
#     for i in word:
#         if i >= 'a' and i <= 'z':
#             smallword = smallword + i
#         else:
#             i = ord(i)
#             i = i + 32
#             i = chr(i)
#             smallword = smallword + i
#     print(smallword)

''' process - 2(using in built functions.) '''
# word = input("enter a two letter word (to converet into lower case.)")
# length = len(word)
# if length == 2 and word.isalpha():
#     small = word.lower()
#     print(small)
# else:
#     print("please enter a two letter word.")



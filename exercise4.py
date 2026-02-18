''' Write and test a function named check leap year that takes as parameter a year between 1600
and 9999. It should return True if the year is a leap year and False otherwise. '''
# def leapyearcheck(year):
#     if year > 1600 and year < 9999:
#         if year % 4 == 0 and year % 100 != 0:
#             return True
#         elif year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         print("please enter correct year between 1600 and 9999.")
#         return None
# year = int(input("enter a year (1600 - 9999) to check leap year or not :"))
# print(f"{leapyearcheck(year)}")


''' Write and test a function that takes a word as input and prints the number of vowels and
consonants in it. '''
# def vowelandconsonantcount(word):
#     vowels = "AEIOUaeiou"
#     vowel = 0
#     consonant = 0
#     for i in word:
#         if i in vowels:
#             vowel+=1
#         elif ("a" <= i <= "z") or ("A" < i <= "Z"):
#             consonant+=1
#         else:
#             continue
#     return vowel, consonant
# word = input("enter a word :")
# print(f"(vowels, consonants) = {vowelandconsonantcount(word)}")


''' Write and test a function that takes a number as parameter and prints the multiplication table
of that number. '''
# def multiplicationtable(n):
#     print(f"*****   MULTIPLICATION TABLE OF {n}   *****")
#     for i in range(1,11):
#         mult = 0
#         mult = n * i
#         print(f"{n} x {i} = {mult}")
# n = int(input("enter the number to print its multiplication table :"))
# multiplicationtable(n)


''' Write a function that takes three numbers as parameters and returns the median value of those
parameters. '''
# def medianof(x, y, z):
#     if (y < x and x < z) or (z < x and x < y):
#         median = x
#         return median
#     elif (x < y and y < z) or (z < y and y < x):
#         median = y
#         return median
#     else:
#         median = z
#     return median
# x = int(input("enter 1st integer :"))
# y = int(input("enter 2nd integer :"))
# z = int(input("enter 3rd integer :"))
# print(f"median = {medianof(x, y, z)}")


''' Write and test a function add square that returns the square of its parameter. '''
# def add_square(n):
#     if n == 0:
#         return 0
#     else:
#         return n * n
# a = int(input("enter an integer to print its square :"))
# print(f"square of {a} = {add_square(a)}")


''' Write a function called calcSeconds() which takes three arguments for hours, minutes, and
seconds and returns the total time in seconds. Example: calcSeconds(1, 3, 20) should
return 3800. '''
# def calcseconds(hours, minutes, seconds):
#     total_seconds = 0
#     hour_seconds = hours * 60 * 60
#     minute_seconds = minutes * 60
#     total_seconds = hour_seconds + minute_seconds + seconds
#     return total_seconds
# hours = int(input("enter no of hours :"))
# minutes = int(input("enter no of minutes :"))
# seconds = int(input("enter no of seconds :"))
# print(f"total no of seconds = {calcseconds(hours, minutes, seconds)}")


''' Write a function named IIT() that takes a character as an argument and prints IIT in that
character. Example:
Input: '.'
Output:
.
.
.
.
.
.
.
.
. . . . .
.
.
. '''
# def IIT(ch):
#     for i in range(5):
#         print(ch, end="   ")
#         print(ch, end="   ")
#         if i == 0:
#             print(ch * 5, end="")
#         else:
#             print("  " + ch + "  ", end="")
#         print()
# IIT('.')


''' Write a function add square() that takes a 3-digit integer as its argument and finds the sum
of the squares of digits in the number. '''
# def add_square(num):
    # count = 0
    # o_num = num
    # x_num = num
    # while o_num > 0:
    #     rem = o_num % 10 
    #     count+=1
    #     o_num //= 10
    # if count == 3:
    #     sum = 0
    #     while num > 0:
    #         r = num % 10
    #         sum += r ** 2
    #         num //= 10
    #     print(f"sum of squares of digits in {x_num} = {sum}")
    # else:
    #     print("please enter a three digit - integer")
    # pass
# num = int(input("enter a three digit integer :"))
# add_square(num)


''' Write a function that takes a 3-digit positive integer as its argument and reverses it. Example:
Input: 123, Output: 321 Input: 120, Output: 21 '''
# def reverse(num):
#     count = 0
#     o_num = num
#     x_num = num
#     while o_num > 0:
#         rem = o_num % 10 
#         count+=1
#         o_num //= 10
#     if count == 3:
#         rev = 0
#         while num > 0:
#             r = num % 10
#             rev = rev * 10 + r
#             num //= 10
#         print(f"reverse of {x_num} = {rev}")
#     else:
#         print("please enter a three digit - integer")
#     pass
# num = int(input("enter a three digit integer :"))
# reverse(num)


'''  '''
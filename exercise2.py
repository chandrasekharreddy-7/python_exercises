''' Q1 . Write a program to swap the contents of two variables using only bitwise operations. '''
# a = int(input("enter 1st integer (to swap) :"))
# b = int(input("enter 2nd integer (to swap) :"))
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a,b)
# a , b = b , a
# print(a,b)


''' Q2 . Write a program to check whether a number has 0 as its last digit. '''
# a = input("enter an integer(to check last digit is 0) :")
# if a.isdigit():
#     a = int(a)
#     remainder = a % 10
#     if remainder == 0:
#         print(f"the number {a} has last digit 0")
#     else:
#         print(f"the number {a} had not 0 as last digit.")
# else:
#     print("please enter a number.")


''' Q3 . Write a program that takes an integer as input and checks, using bitwise operations, if it is
         divisible by 4. '''
# a = input("enter an integer :")
# if a.isdigit():
#     a = int(a)
#     if a & 3 == 0:
#         print(f"the number {a} is divisible by 4")
#     else:
#         print(f"the number {a} is not divisible by 4")
# else:
#     print("please enter a number.")


''' Q4 . Write a program that takes a natural number as input and prints the remainder when it is
         divided by 3. '''
# a = input("enter a natural number :")
# if a.isdigit():
#     a = int(a)
#     if a > 0:
#         x = a % 3
#         print(f"remainder when divided by 3 = {x}")
# else:
#     print("enter a number")


''' Q5. Write a program that takes as input n1 o1 n2 o2 n3, where n1, n2, n3 are natural numbers
        and o1, o2 ∈ {+, -, *}. Use nested if--else--if statements to evaluate the expression. '''
# def evaluate_expression(n1, op1, n2, op2, n3):
#     result = None
#     if op1 == '+':
#         if op2 == '+':
#             result = n1 + n2 + n3
#         elif op2 == '-':
#             result = n1 + n2 - n3
#         elif op2 == '*':
#             result = n1 + n2 * n3
#     elif op1 == '-':
#         if op2 == '+':
#             result = n1 - n2 + n3
#         elif op2 == '-':
#             result = n1 - n2 - n3
#         elif op2 == '*':
#             result = n1 - n2 * n3
#     elif op1 == '*':
#         if op2 == '+':
#             result = n1 * n2 + n3
#         elif op2 == '-':
#             result = n1 * n2 - n3
#         elif op2 == '*':
#             result = n1 * n2 * n3
#     return result
# n1 = input("enter a natural number :")
# n2 = input("enter a natural number :")
# n3 = input("enter a natural number :")
# op1 = input("enter your choice for operation 1 (+ / - / *) :")
# op2 = input("enter your choice for operation 2 (+ / - / *) :")
# if n1.isdigit() and float(n1) > 0:
#     n1 = float(n1)
#     if n2.isdigit() and float(n2) > 0:
#         n2 = float(n2)
#         if n3.isdigit() and float(n3) > 0:
#             n3 = float(n3)
#             if op1 == "+" or op1 == "-" or op1 == "*":
#                 if op2 == "+" or op2 == "-" or op2 == "*":
#                     print(f"result = {evaluate_expression(n1, op1, n2, op2, n3)}")
#                 else:
#                     print("please enter correct option from (+ / - / *) for o2.")
#             else:
#                 print("please enter correct option from (+ / - / *) for o1.")
#         else:
#             print("please enter a natural number for n3.")
#     else:
#         print("please enter a natural number for n2.")
# else:
#     print("please enter a natural number for n1.")


''' Q6 . Write a program that takes as input two integers and prints appropriate messages if at least
        one or both are positive, negative, or zero. '''
# a = input("enter 1st integer :")
# b = input("enter 2nd integer :")
# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)
#     if a > 0 and b > 0:
#         print(f"In {a} and {b}, both are positive.")
#     elif a > 0 and b < 0:
#         print(f"In {a} and {b}, {a} is positive and {b} is negative.")
#     elif a < 0 and b < 0:
#         print(f"In {a} and {b}, both are negative.")
#     elif a < 0 and b == 0:
#         print("a is negative, b is zero.")
#     elif a > 0 and b == 0:
#         print("a is positive, b is zero.")
#     elif a == 0 and b > 0:
#         print("a is zero, b is positive.")
#     else:
#         print("a is zero, b is negative.")
# else:
#     print("please enter a number.")


''' Q7 . Write a program that takes as input two integers and checks if their LCM is equal to at least
        one of the given integers. '''
# import math
# def check_lcm_equality(a, b):
#     calculated_lcm = math.lcm(a, b)
#     if calculated_lcm == a or calculated_lcm == b:
#         return True
#     else:
#         return False
# num1 = int(input("Enter first integer: "))
# num2 = int(input("Enter second integer: "))
# if check_lcm_equality(num1, num2):
#     print(f"The LCM of {num1} and {num2} is equal to one of the given integers.")
# else:
#     print(f"The LCM of {num1} and {num2} is not equal to either of the given integers.")


''' Q9 . Write a program that takes as input the cost price and selling price of an item, prints whether
        the sale resulted in a profit or a loss, and prints the amount. '''
# def amountcalculator(costprice, sellprice):
#     profit = 0
#     loss = 0
#     if costprice.isdigit() and int(costprice) >= 0:
#         costprice = int(costprice)
#         if sellprice.isdigit() and int(sellprice) >= 0:
#             sellprice = int(sellprice)
#             if costprice > sellprice:
#                 loss = abs(costprice - sellprice)
#                 print(f"you got a loss of {loss}.rupees")
#             elif costprice < sellprice:
#                 profit = abs(costprice - sellprice)
#                 print(f"you got a profit of {profit}.rupees")
#             else:
#                 print("you doesn't make any profit or loss on the item.")
#         else:
#             print("please enter a correct selling price.")
#     else:
#         print("please enter a correct cost price")
# costprice = input("enter cost price of the item :")
# sellprice = input("enter sell price of the item :")
# amountcalculator(costprice, sellprice)


''' Q10 . Write a program that takes a year as input and prints whether it is a leap year or not.
        Note: The year can be any year in the past or up to 100 years into the future. '''
# def leapyearcheck(year):
#     if year.isdigit():
#         year = int(year)
#         if year % 4 == 0 and year % 100 != 0:
#             print(f"{year} is a leap year.")
#         elif year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print("please enter a valid year.")
# year = input("enter a year (to check leap year or not) :")
# leapyearcheck(year)


''' Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter. Also print whether the area is greater than the perimeter. '''
# length = float(input("enter length of rectangle :"))
# breadth = float(input("enter breadth of rectangle :"))
# if length > 0 and breadth > 0:
#     area = length * breadth
#     perimeter = 2 * (length + breadth)
#     if area > perimeter:
#         print("area is greater than the perimter.")
#     else:
#         print("perimeter is greater than the area.")
# else:
#     print("please enter correct length or breadth.")
    
    
''' Write a program that takes three points (x1, y1), (x2, y2), and (x3, y3) and checks if they lie
# on a straight line. '''
# x1 = int(input("enter 1st point X - coordinate :"))
# y1 = int(input("enter 1st point y - coordinate :"))
# x2 = int(input("enter 2nd point X - coordinate :"))
# y2 = int(input("enter 2nd point y - coordinate :"))
# x3 = int(input("enter 3rd point X - coordinate :"))
# y3 = int(input("enter 3rd point y - coordinate :"))
# collinear = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
# if collinear == 0:
#     print(f"the points ({x1}, {y1}), ({x2}, {y2}) and ({x3}, {y3}) are collinear")
# else:
#     print(f"the points ({x1}, {y1}), ({x2}, {y2}) and ({x3}, {y3}) are not collinear")


''' Write a program that takes as input:
• center of a circle (cx, cy),
• radius r,
• a point P(px, py),
and determines whether the point lies inside the circle, on the circle, or outside the circle. '''
# x1 , y1 = float(input("enter x coordinate of centre of circle :")), float(input("enter y coordinate of centre of circle :"))
# r = float(input("enter radius of circle :"))
# x2 , y2 = float(input("enter x coordinate of the point :")), float(input("enter y coordinate of the point :"))
# distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# if r == distance:
#     print(f"the point {x2, y2} lies on the circle.")
# elif r > distance:
#     print(f"the point {x2, y2} lies inside the circle.")
# else:
#     print(f"the point {x2, y2} lies outside the circle.")


''' Write a program that takes a point P(px, py) and determines the quadrant it lies in. Explicitly
handle the cases when the point lies on the axes or at the origin. '''
# x, y = float(input("enter x coordinate of the point :")), float(input("enter y coordinate of the point :"))
# if x == 0 and y == 0:
#     print(f"{x, y} lies at the origin.")
# elif x == 0 and (y > 0 or y < 0):
#     print(f"{x, y} lies on y axis")
# elif y == 0 and (x > 0 or x < 0):
#     print(f"{x, y} lies on x axis")
# elif x > 0 and y > 0:
#     print(f"{x, y} lies in Quadrant 1")
# elif x > 0 and y < 0:
#     print(f"{x, y} lies in Quadrant 4")
# elif x < 0 and y > 0:
#     print(f"{x, y} lies in Quadrant 2")
# else:
#     print(f"{x, y} lies in Quadrant 3")


''' Insurance Premium Calculation
A (hypothetical) insurance company wishes to automate its premium calculation and policy
restrictions. The rules are as follows:
(a) If a person's health is excellent, the person is between 25 and 35 years of age, lives
in a city, and is a male, then the premium is Rs. 4000 per month and the policy
amount cannot exceed Rs. 2 lakhs.
(b) If all the above conditions are satisfied except that the person is female, then the
premium is Rs. 3000 per month and the policy amount cannot exceed Rs. 1.5
lakhs.
(c) If a person's health is poor, the person is between 25 and 35 years of age, lives in
a village, and is a male, then the premium is Rs. 6000 per month and the policy
amount cannot exceed Rs. 1 lakh.
(d) In all other eligible cases, the premium is Rs. 5000 per month and the policy amount
cannot exceed Rs. 1.25 lakhs.
(e) A person below 25 years of age or above 65 years of age will not be insured.
(f) If the policy value requested is less than the maximum allowed, the monthly premium
amount is proportional to the policy value.
Write a program that takes necessary inputs from the user and determines whether the
person can be insured or not, and if eligible, calculates the premium amount to be paid. '''
# age = int(input("Enter age: "))
# if age < 25 or age > 65:
#     print("\nPerson is NOT eligible for insurance.")
# else:
#     gender = input("Enter gender (male/female): ").lower()
#     health = input("Enter health condition (excellent/poor): ").lower()
#     location = input("Enter location (city/village): ").lower()
#     policy_requested = float(input("Enter policy amount requested (in lakhs): "))
#     premium = 0
#     max_policy = 0

#     if health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "male":
#         premium = 4000
#         max_policy = 2.0

#     elif health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "female":
#         premium = 3000
#         max_policy = 1.5

#     elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
#         premium = 6000
#         max_policy = 1.0

#     else:
#         premium = 5000
#         max_policy = 1.25

#     if policy_requested > max_policy:
#         print("\nRequested policy exceeds maximum allowed.")
#         print("Maximum policy allowed:", max_policy, "lakhs")
#     else:
#         final_premium = premium * (policy_requested / max_policy)
#         print("\nPerson is eligible for insurance.")
#         print("Policy Amount:", policy_requested, "lakhs")
#         print("Monthly Premium to be paid: Rs.",final_premium)


''' Grading of Steel
A certain grade of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are assigned as follows:
• Grade 10: All three conditions are satisfied
• Grade 9: Conditions (i) and (ii) are satisfied
2

• Grade 8: Conditions (ii) and (iii) are satisfied
• Grade 7: Conditions (i) and (iii) are satisfied
• Grade 6: Only one condition is satisfied
• Grade 5: None of the conditions are satisfied
Write a program that takes as input the hardness, carbon content, and tensile strength of
the steel and prints the grade of the steel. '''
# hardness = float(input("Enter hardness: "))
# carbon = float(input("Enter carbon content: "))
# tensile = float(input("Enter tensile strength: "))

# c1 = hardness > 50
# c2 = carbon < 0.7
# c3 = tensile > 5600

# if c1 and c2 and c3:
#     grade = 10
# elif c1 and c2:
#     grade = 9
# elif c2 and c3:
#     grade = 8
# elif c1 and c3:
#     grade = 7
# elif c1 or c2 or c3:
#     grade = 6
# else:
#     grade = 5

# print("Grade of steel:", grade)


''' A library charges a fine for late returns:
• First 5 days: 50 paise
• 6-10 days: 1 rupee
• Above 10 days: 5 rupees
If returned after 30 days, membership is canceled. Write a program to display the fine or
the appropriate message. '''
# days = int(input("Enter number of days late: "))

# if days <= 5:
#     fine = days * 0.50
#     print("Fine to be paid: Rs.", fine)

# elif days <= 10:
#     fine = 5 * 0.50 + (days - 5) * 1
#     print("Fine to be paid: Rs.", fine)

# elif days <= 30:
#     fine = 5 * 0.50 + 5 * 1 + (days - 10) * 5
#     print("Fine to be paid: Rs.", fine)

# else:
#     print("Membership cancelled.")


''' Write a program that takes a 4-character binary number and prints its decimal equivalent.
Note: Do not use hex, bin, or int functions. '''
# binary = int(input("enter 4 - character binary number :"))
# org_binary = binary
# count = 0
# sum = 0
# while binary > 0:
#     l = binary % 10
#     if l == 0 or l == 1:
#         sum += (l*(2**count))
#         count+=1
#         binary//=10
#     else:
#         print("please enter correct binary number(0 and 1).")
#         break
# if sum >= 0:
#     print(f"binary to decimal of {org_binary} = {sum}")
# else:
#     print("please make sure to have correct code.")


''' Write a program that takes a number between 0 and 31 and prints its binary representation.
Note: Do not use the bin function. '''
# i = int(input("enter a number :"))
# string = ""
# reverse = ""
# if i == 0:
#     n = 0
#     print(f"binary equivalent = {n}")
# else: 
#     while i > 0:
#             n = i % 2
#             string += str(n)
#             i = i // 2
# for i in range(len(string)+1):
#     reverse = string[::-1]
# print(f"binary equivalent = {reverse}")


''' Write a program to swap two integers without using a third variable. '''
# a = int(input("enter 1st integer to swap :"))
# b = int(input("enter 2nd integer to swap :"))
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a ,b)



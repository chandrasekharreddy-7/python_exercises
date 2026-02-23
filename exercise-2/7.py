''' Q7 . Write a program that takes as input two integers and checks if their LCM is equal to at least
        one of the given integers. '''
import math
def check_lcm_equality(a, b):
    calculated_lcm = math.lcm(a, b)
    if calculated_lcm == a or calculated_lcm == b:
        return True
    else:
        return False
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
if check_lcm_equality(num1, num2):
    print(f"The LCM of {num1} and {num2} is equal to one of the given integers.")
else:
    print(f"The LCM of {num1} and {num2} is not equal to either of the given integers.")
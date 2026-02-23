''' Q4 . Write a program that takes a natural number as input and prints the remainder when it is
         divided by 3. '''
a = input("enter a natural number :")
if a.isdigit():
    a = int(a)
    if a > 0:
        x = a % 3
        print(f"remainder when divided by 3 = {x}")
else:
    print("enter a number")
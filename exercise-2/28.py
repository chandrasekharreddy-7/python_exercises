''' Q28 : Write a program that takes a 4-character binary number and prints its decimal equivalent.
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
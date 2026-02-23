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
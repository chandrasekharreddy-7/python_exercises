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
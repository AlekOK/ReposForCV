# # 7 Print every elements of the list with #-symbol on the end
# new_list = ["addf", "bdff", "cret", "dfdjk"]
# for i in new_list:
#     for j in i:
#         print(j, end='# ')
##################################################################

# # 8 the number is simple or complex?
# num = int(input("enter your number: "))
# for x in  range(2,num):
#     if num % x == 0:
#         print("Your number is complex")
#         break
#     else:    
#         print("Your number is simple")
       
############################################################    
# # 9. max digit of your number
# import random
# random_num= random.randint(0, 1000)
# random_list = [random_num for j in range(int(input("enter  how must be numbers of the list: "))) ]
# print(max(random_list))

############################################################
# # 10. it's palindrom or no?
# word = input("enter your word: ")
# word.upper()
# poli = list(word)
# ilop = poli[::-1]
# if ilop == poli:
#     print("yes! your word is the polindrom")
# else:
#     print("no! it's not the polindrom")


# # 11. create list and print max and min elements
# a = [input("enter your value") for f in range(int(input("enter  how must be numbers of the list: "))) ]
# g = max(a)
# w = min(a)
# print("Max number is = {} and min number is = {}".format(g , w))
#####################################################################################
# 12.1 print even numbers from 1 to 11
#  odd_numbers = [x for x in range(1,11) if x % 2 == 0]
# print(odd_numbers)
#######################################
# 12.2 print odd numbers that are divided into 3
#  even_numbers = [x for x in range(1,11) if x % 2 ==1 and  x % 3  ==0 ]
# print(even_numbers)
######################################
# 12.3 print numbers that aren't divided into 2 and 3
# not_divide_numbers = [ x for x in range(1,11) if x % 2 == 1 and  x % 3  == 1 ]
# print(not_divide_numbers)
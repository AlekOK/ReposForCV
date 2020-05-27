# # 1.1 Calculete greater number
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# if a > b :
#     print("First number is greater")
# elif a < b :
#     print("Second number is greater")
# else:
#     print("These numbers are equal")        
 
###################################################################### 
#  # 1.2 The number is even or odd???
# try: 
#     a = int(input("enter number: "))  
#     if a % 2 == 0: 
#         print("Your number is even")
#     else:
#         print("Your number is odd")
# except:
#     print("not correct input")     
########################################################################
# 1.3 calculete factorial 
# try:
#     number = int(input("enter natural number: "))  
#     i=1
#     factorial = 1
#     while i <= number:
#         factorial *= i
#         i += 1
#     print("factorial {}!=".format(number),factorial)
# except:
#     print("Please input NATURAL number")
##############################################################################    
# # 2.1 Print all ODD numbers from 0 to 100 without continue
# new_list = list(range(100))
# for i in new_list:
#     if i % 2 == 0:
#         print(i) 
##############################################
# #2.2 calculete all ODD numbers from 0 to 100 with continue
# new_list = list(range(100))
# for i in new_list:
#     if i % 2 ==0:
#         continue
#     print(i) 
################################################################################
# # 1.1 Print all EVEN numbers from 0 to 100 with for
# for i in range(1,100,2):
#     print(i)    

####################################################
# # 1.2 Print all EVEN numbers from 0 to 100 with while
# i = 0 
# while i < 100 :
#     if i%2 == 1:
#         print(i)
#     i+=1
   
#################################################################################
# # 3 check odd number in the list
# for i in list(range(10)):
#     if i % 2 == 1:
#         break
# print("yes. Not less one odd number in the list")
############################################################################
# #4 create list and change type of elements
# new_list = list(range(10))
# list_index = 0
# for j in new_list:
#     new_list[list_index] = j/1
#     list_index = list_index + 1
# print(new_list)
############################################################################    
# # 5 fibonacci
# number = int(input("enter natural number: ")) 
# first_num_order = 0
# second_num_order = 1
# while second_num_order <= number:
#     print(second_num_order)
#     next_num_order = first_num_order + second_num_order
#     first_num_order = second_num_order
#     second_num_order = next_num_order    
######################################################################

# # 6 Print every elements of the list
# new_list = ["a", "b", "c", "d"]
# for i in new_list:
#     print(i)
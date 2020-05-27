# #13. find sum of digits of the number
# num=input("enter number: ")
# def count_sum(num):
#     '''This function calculete amount of all digits of the number'''
#     i = 0
#     result = 0
#     for j in range(len(num)):
#         result += int(num[i])
#         i+=1
#     print(result)      
      
# count_sum(num)        

###########################################
# # 14. function for calculete numbers of Fibonacci 
# num=int(input("enter number: "))
# def count_fibo(num):
#     '''this function calculete numbers of Fibonacci and print whiz entered number '''
#     a=0
#     b=1
#     while b <=num:
#         print(b)
#         sum=a+b
#         a=b
#         b=sum
#     print(num)    
# count_fibo(num)        

##########################################

# # 15 find discriminant   
# def calc_discrim(a,b,c):
#     '''It function calculate discriminant of the quadratic equation'''
#     disc = b**2-4*a*c
#     # if disc > 0:
#     #     root1 = (-4+disc**0.5)/2
#     #     root2 = (-4-disc**0.5)/2
#     #     print(root1, root2)
#     # elif disc == 0:
#     #     root= -b/2*a
#     #     print(root)    
#     # else:
#     #     print("root isn't existe")    
#     print(disc)
# calc_discrim(1,4,-21) # 
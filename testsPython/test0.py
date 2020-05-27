# def arithmetic_mean(*args):
#     '''Functoin that calculates the arithmetic mean'''
#     r = sum(args)/len(args)
#     print(r)
# arithmetic_mean(6,5,7)  

#  

# #################################
# def absolute(num):
#     '''Function that returns absolutr value of the number'''    
#     i = abs(num)
#     print(i)
# absolute(-67)        

###################################

# def func(a,b):
#     '''This function determines which number is greater'''   
#     if a > b:
#         print(a, " is greater than ",b )
#     elif b > a:
#         print(b, " is greater then ",a)
#     else: 
#         print(a, "is equels ",b)                      
# func(6,6)  

########################################
# def calculete_square_rect(a,b):
#     '''Function for square of rectangle'''
#     s_r = a * b
#     s_r = float(s_r)
#     print(s_r)   
      
# def calculete_square_tri(a,b,c):
#     '''Function for square of triangle'''    
#     p = (a+b+c)/2
#     s_t = (p*(p-a)*(p-b)*(p-c))**0.5
#     s_t = float(s_t)
#     print(s_t)
   
# def calculete_square_cir(e):
#     '''Function for square of circle'''        
#     c_s = 3.14*e**2
#     float(c_s)
#     print(c_s)
      
# figura = str(input("What is your figura for calculete square? ('rectangle'  'triangle'  'circle': "))
# if figura=="rectangle":
#     a=float(input("enter first side:  "))
#     b=float(input("enter second side: "))
#     calculete_square_rect(a,b)
# elif figura=="triangle":
#     a=float(input("enter first side:  "))
#     b=float(input("enter second side: "))
#     c=float(input("enter third side: ")) 
#     calculete_square_tri(a,b,c)
# elif figura == "circle":
#     r = float(input("enter first side:  "))
#     calculete_square_cir(r)
# else:
#     print("sorry, select between of rectangle or triangle or circle") 
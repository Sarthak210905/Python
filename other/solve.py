
# # read 2 value from keyboard and find minimum value
# # read 2 value from keyboard and swap them with out using 3 variable

# value1 = float(input("Enter the first value: "))
# value2 = float(input("Enter the second value: "))

# x = value1 if value1 < value2 else value2


# print("The minimum value is:",x)\

# print("_______________________________________________")

# a = float(input("Enter the first number (a): "))
# b = float(input("Enter the second number (b): "))
# a,b = b,a 
# print("After swapping:")
# print("a =", a)
# print("b =", b)

# print("_______________________________________________")
# a=10
# b=10
# print(a is not b)

# print("_______________________________________________")

# a='sumit'
# b='sumit'
# print(a is b)
# print("_______________________________________________")

# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# print("_______________________________________________")


# a=(1,2,3)
# b=(1,2,3)
# print(a is b)
# print(id(a) )
# print(id(b) )
# print("_______________________________________________")

# a=[1,2,3]
# b=[1,2,3]
# print(a == b)
# print("_______________________________________________")

# a=[1,2,3]
# print(2 in a)
# print(2 not in a)
# print("_______________________________________________")

# s = 'learning python is very simple'
# print('E'in s) 
# print('e'in s) 

# print("_______________________________________________")

# a = 10
# a = 'sumit'
# b = 10
# c = 10
# print(id(a))
# print(id(b))
# print(id(c))

# print("_______________________________________________")

# l=[1,2,3,4,5,6,7,8,]
# print(type(l))

# l=[]
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# print(l)

# l=[1,1,23,'sarthak',32.5]
# l.reverse()
# l.insert(0,'hello world')
# l.clear()
# l=(1,2,4,4,5,6,7)
# x = l.count(4)
# print(x)
# l=(1,2,4,4,5,6,7)
# x = l.count(4)

# print(x)

# r =range(1,51,3)
# for i in r :
#      print(i)


# p= float(input('enter the principle : '))
# r= float(input('enter the rate : '))
# t= float(input('enter the time in months : '))

# Total=p*r*t/100
# print("The simple intrest is",Total)
# print("_______________________________________________")


# age = int(input('Enter the age '))

# if age >0 :
#  print('positive') 

# elif age ==0:
#  print("zero")
# else :
#  print('negative')
 
 
# company = input('Enter the age ')

# if company == 'bugatti':
#  print('car brand') 

# elif company == 'hayabusa':
#  print('')
# else :
#  print('negative')


#  write a program to check wethear the given is between 1-100 or not

# num = int(input('enter the number'))

# if num >= 1 or num <= 100:
#      print('valid number')

# else:
#      print(' number is out of range')

# name = input('enter the name ')
# count=0
# for i in name :
#     print('char at index',count, 'is',i)
#     count = count+1
 
# def fun(name,*args):
#     result=0
#     for i in args:
#         result = result + i
#     print(name,"is",result)
   
# fun(name='sarthak')
# fun(10,30,name='sarth')
# fun(10,30,name='pranjal')
# ***********************************************
# Keyword variable length arguments:
# def display(**n):
#  print('record of info')
#  for k,v in n.items(): 
#     print(k,'........',n)
# display(name='gattu',age=13,marks=10)
# display(age=20,name='sarthak',marks=100,address='nanda nagar')
# ***************************************************
# Types of variables
# 1.Local variables
# 2.Global variables
# ***************************************************
# example of 1.
# def f1():
    # a=10
    # print('f1=',a)
# def f2():
    # print('f2=',a)  //it cannot access a in f2 because it is the local variable of f1
# f1()
# f2()
# ********************************
# a=10
# def f1():
#     a=10
#     print('f1=',a)
# def f2():
#     print('f2=',a)  
# f1()
# f2()
# *****************************************
# a=10
# def f1():
#    global a
#    a=20
#    print('f1=',a)
# def f2():
#     print('f2=',a)  
# f2()
# f1()
# **************************************************
# Recursive function->
def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print(fact(5))


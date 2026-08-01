##
##
##
####a = input("enter the staring")
####
####print(type(a))
####print(a)
##
##
##
##
####a = int(input("enter the first number"))
####
####b = int(input("enter the second number"))
##
##
####print("addition",a+b)
####print("multiplication",a*b)
####print("division",a/b)
####print(a>b)
##
##
####a = float(input("enter the number"))
####
####b = int(a)
####
####print(a)
####print(b)
##
##
##a = int(input("enter the number"))
##
##
##b = float(a)
##
##
##print(b)
##
##c = str(a)
##
####print(c)



##a = input("enter the number")
##
##b = int(a)
##
##c = float(a)
##
##print(b+c)
##

##a = int(input("enter the number"))
##
##b = int(input("enter the second no"))
##
##c = a+b/2
##
##print("avrange is a=",c)



##a = bool(input("enter the bool value"))
##
##print(a)
##

##
##a = int(input("enter the number"))
##
##b = int(input("enter the second"))
##
##
##print(f"formating is a:-{a+b}")
##print("the subtraction is a:{}".format(a-b))



##p = int(input("principal amount"))
##
##r = int(input("rate of the interest"))
##
##t = int(input("the time o fthe loan"))
##
##
##si = (p*r*t) /100
##
##print("simple interest is a",si)

##from math import *
##r = int(input("enter the radius"))
##
##
##s = pi * r * r
##
##print("area of the circle is a:-",s)
##
##


##a = int(input("enter 1:-"))
##
##b = int(input("enter 2:-"))
##
##c = int(input("enter 3:-"))
##
##total = 100
##
##obtained = a + b + c
##
##
##per = obtained / total * 100



##income = int(input("enter the income"))
##
##expenses = int(input("enter the expenses"))
##
##
##saving = income - expenses
##
##
##print(saving)



##a = int(input("enter 1:-"))
##
##b = int(input("enter 2:-"))
##
##c = int(input("enter 3:-"))
##
##d = int(input("enter 4:-"))
##
##e = int(input("enter 5:-"))
##
##
##total = a+b+c+d+e
##
##print("sum is a:-",total)
##
##
##avg = total / 5
##
##print("avrange is a:-",avg)

import math as m

##r = int(input("enter :-"))
##
##
##area = m.pi*r*r
##
##print(area)


##name = input("enter the name")
##
##
##print(name.rjust(20))


##l = int(input("enter the length"))
##
##w = int(input("enter the width"))
##
##
##d = l * w
##
##print(d)

##a = int(input("enter the a value"))
##
##b = int(input("enter the b value"))
##
##
##temp = b
##
##b = a
##
##a = temp
##
##
##print("after swap",a)
##print("after swap",b)



##a = int(input("enter the a number"))
##
##b = int(input("emter the a second number"))
##
##a = a+b
##
##b = a-b
##
##a = a-b
##
##
##
##print(a)
##print(b)


##a = int(input("enter"))
##
##b = float(input("enter float"))
##
##c = input("enter string")
##
##d = bool(input("enter true/false"))
##
##
##print(type(a),"the b",b,"the value of c",c,"the value of the a bool",d)



##l = int(input("enter the length"))
##
##w = int(input("enter the width"))
##
##s = l * w
##
##
##print(s)


##salary = int(input("enter your salary"))
##
##
##s = salary + (salary * 10)/100
##
##
##print(s)


##name = input("enter your name")
##
##age = int(input("enter your age"))
##
##print(f"welcome {name} your {age} age is a perfact fit for this role ")

##a = int(input("enter 1:-"))
##
##b = int(input("enter 2:-"))
##
##c = int(input("enter 3:-"))
##
##d = a+b+c
##
##e = d/3
##
##print("the sum of the a number is a",d)
##
##print("the avrange of the number is a:-",e)


##l = 10
##w = 20
##
##d = 2*(l+w)
##
##print(d)


##h = 20
##
##c = h * h
##
##w = 34
##
##print(w/h)


def  welcome():
    print("welcome in python")


##welcome()

##def college_name():
##    print("gangamai college of the engineering") 
##
##
##college_name()



def add(a,b):

    print(a+b)


##add(20,30)




##def rect(l,w):
##
##    print(l*w)
##
##
##rect(3,4)


def pei_rect(l,w):

    d = 2*(l+w)

    print("the a peiremeter of rectriangle is a:-",d)


##pei_rect(20,34)


from math import *

def area(radius):

    d = pi * radius * radius

    print(d)


##area(23)

##def per(total_marks,obtained_m):
##
##    d = obtained_m / total_marks  * 100
##
##    print(d)
##
##
##per(720,650)


def largest(a,b):

    if a>b:
        print("a is greater no")

    else:
        print("b is grater number")


largest(12,34)











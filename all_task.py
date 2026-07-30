####
####
####a = input("enter the string")
####
####print("the name is a:-",a)
####
####print(type(a))
##
##      
####a = int(input("enter the first number "))
####
####b = int(input("enter the second number"))
####
####s = int(a)
####
####f = int(b)
####
####
####print("sum is a:-",a+b)
####
####print("multiplication is a:-",a*b)
####
####print("subtraction is a:-",a-b)
####
####print("divison is a:-",a/b)
##
##
####a = float(input("enter the number:-"))
####
####print("number is a:-",a)
####print(type(a))
####
####r = int(a)
####
####print(type(r))
##
##
####a = int(input("enter the number"))
####
####
####print("thenumber is a",a)
####print(type(a))
####
####s = float(a)
####f = str(a)
####print(type(s))
####print(type(f))
##
##
####a = input("enter the string:-")
####b = int(a)
####
####c = float(a)
####
####print(type(a))
####print(type(b))
####print(type(c))
##
##
##
####a = int(input("enter the number:-"))
####b = int(input("enter the second number:-"))
####
####c = a+b/2
####
####print("average:---",c)
##
##
####a = bool(input("enter the True / False :--"))
####
####print(type(a))
##
##
##
####a = int(input("enter the first number:-"))
####b = int(input("enter the second number:-"))
####
####print("addition is a:-",a+b)
####
####print("subtraction is a:-",a-b)
####
####print("multiplication is a :-",a*b)
####
####print("division is a:-",a/b)
####
####print("fuler is a:-",a//b)
####
####print("power is a:-",a**b)
##
##
##
####a = int(input("enter the principal amount"))
####b = int(input("enter the rate of interest:"))
####c = int(input("enter the time "))
####
####
####si = (a*b*c)/100
####
####print("simple interest is a:-",si)
##
##
####from math import pi
####
####radius = int(input("enter the radius:-"))
####
####circle = pi * radius * radius
####
####print("area of a circle is a",circle)
##
####m1 = float(input("enter the first subject marks:-"))
####
####m2 = float(input("enter the second subject marks:-"))
####
####m3 = float(input("enter the third subject marks:-"))
####
####
####total = 100
####
####d = m1+m2+m3
####
####s = d/total*100
####
####
####
####print("percentage is a:-",s)
##
##
####income = int(input("enter the first number:-"))
####
####expenses = int(input("enter the expenses of the employee:-"))
####
####
####saving = income - expenses
####
####print("his saving is a:-",saving)
####
##
##
####m1 = int(input("enter the first:-"))
####m2 = int(input("enter the second:-"))
####m3 = int(input("enter the third"))
####m4 = int(input("enter the four"))
####m5 = int(input("enter the fivr"))
####
####total = m1 + m2 + m3 + m4 + m5
####
####total_avg = total / 5
####
####print("sum of the number is a:-",total)
####print("averrage of the number is a:-",total_avg)
##
##
##
##
####a = int(input("enter the first number:-"))
####
####b = int(input("enter the second number:-"))
####
####temp = b
####b = a
####a = temp
####
####print("after swap:--",a)
####print("after swap:--",b)
##
####a = int(input("enter the first number:--"))
####
####b = int(input("enter the second number:--"))
####
####a = a+b
####b = a-b
####a = a-b
####
####print("after swaping a is a :--",a)
####print("after swaping b is a :--",b)
##
##
##
####l = int(input("enter the length :-"))
####
####w = int(input("enter the width :--"))
####
####area = l * w
####
####print("area of the rectriangle is a:-",area)
##
####salary = int(input("enter your salary :--"))
####
####total_increase_salary = salary + (salary * 18) / 100
####
####print("after increment salary is a:=",total_increase_salary)
####
##
##
####a = int(input("enter the length:--"))
####b = int(input("enter the width:--"))
####
####s = 2*a + b
####
####print("area of peimenter is a :-",s)
##
##
####l = int(input("enter the legth:--"))
####
####w = int(input("enter the width:--"))
####
####a = l * l
####
####b = w/a
####
####print("body Mass index is a:-",b)
##
##
##
##
##
##
##
##
##def welcome():
##    print("welcome to the python")
##
####welcome()
##
##
##def college_name():
##    print("gangamai college of the engineering")
##
####college_name()
##
##def info():
##    name = input("enter the name")
##    city = input("city name ")
##    course = input("enter the course:-")
##
##    print(name)
##    print(city)
##    print(course)
##
####info()
##
##
##def five():
##    print(5*1)
##    print(5*2)
##    print(5*3)
##    print(5*4)
##    print(5*5)
##    print(5*6)
##    print(5*7)
##    print(5*8)
##    print(5*9)
##    print(5*10)
##
####five()
##
##
##def pattern():
##    print("****")
##    print("****")
##    print("****")
##
####pattern()
##
##def current_year():
##    print("the current year is a:-2026")
##
####current_year()
##
##
##def even():
##    for i in range(20):
##        if i % 2==0:
##            print(i)
##
##
####even()
##
##
##
##def company():
##    print("my dream company is a:- TCS")
##
####company()
##
##
##def add(a,b):
##    print(a+b)
##
##def sub(a,b):
##    print(a-b)
##
##def mul(a,b):
##    print(a*b)
##
##
##def div(a,b):
##    print(a/b)
##
##
####add(20,34)
####sub(34,45)
####mul(23,4)
####div(23,45)
##
##
##def square(num):
##    d = num * num
##    print("sqaure is a",d)
##
####square(5)
##
##
##def cube(num):
##    d = num * num * num
##
##    print("the cube of the number:-",d)
##
####cube(5)
##
##def five(num):
##    for i in range(11):
##        print(num*i)
##
####five(5)
##
##def student(name,age):
##    print("the name of studnet is a:-",name)
##
##    print("the age of the student",age)
##
####student('roshan',23)
##
##
##from math import pi
##
##def circle(radius):
##    d = pi * radius * radius
##    print("area of circle",d)
##
####circle(13)
##
##
##
##def rect(l,w):
##    p = l * w
##    print("the area of the rectriangle is a:-",p)
##
##
####rect(12,43)
##
##
##def per(total_m,obtained_m):
##    a = obtained_m / total_m * 100
##    print(a)
##
##
####per(720,650)
##
##
##
##def largest(a,b):
##    if a>b:
##        print("a is a largest number:-",a)
##    else:
##        print("b is largest number :- ",b)
##
##
####largest(20,45)
##
##def salary(basic):
##    total_s = basic + (basic * 18)/100
##    print("the total salary after increment:-",total_s)
##
####salary(1000)
##              
##
##
##class m1:
##    def m2(a,b):
##        print("addition is a:-",a+b)
##
##        def m3(a,b):
##            print("subtraction is a",a-b)
##
##        def m4(a,b):
##            print("multiplication is a",a*b)
##
##        def m5(a,b):
##            print("the multiplication is :-",a/b)
##
##        return m3,m4,m5
##
##
####a = m1
####ab,ac,ad= a.m2(20,30)
####ab(10,2)
####ac(23,3)
####ad(23,45)
####aa(22,45)
##
##
##
##
##class main:
##    def inner_main(self):
##        def add(a,b):
##            print("addition is:-",a+b)
##
##        def sub(a,b):
##            print("subtraction is a:-",a-b)
##
##        def mul(a,b):
##            print("multiplication is a:-",a*b)
##
##        def div(a,b):
##            print("division is a:-",a/b)
##
##        return add,sub,mul,div
##
##
##    def second_inner(self):
##        def add1(a,b):
##            print("second inner are excuted addition is a:-",a+b)
##    
##        return add1
##
##
##a = main()
##
##ab,ac,ad,sd = a.inner_main()
##ab(10,20)
##ac(20,23)
##ad(34,5)
##ad(20,45)
##
##av = a.second_inner()
##av(20,23)




##def add(a,b):
##    z = a+b
##    print("addition is a",z)
##    return z
##
##
##
##c = add(20,34)


##def sub(a,b):
##    print("subtraction is a:-",a+b)
##
##sub(20,34)

##def mul(a,b):
##    print("multiplication is a :- ",a*b)
##
####mul(23,33)
##
##def square(num):
##    squ = num * num
##    print("square is a :-",squ)
##
##square(7)


def cube(num):
    d = num * num * num
    print("cube is a:-",d)

##cube(17)



##def largest(a,b):
##    if a>b:
##        print("a is a greter number",a)
##
##    else:
##        print("b is a greter number",b)
##
##largest(23,34)


##def small(a,b):
##    if a<b:
##        print("a is small number")
##
##    else:
##        print("b is small number")
##
##small(20,34)


def area_rectriangle(l,w):
    s = l * w
    print("area of the rectriangle",s)

##area_rectriangle(200,34)

##from math import *
##
##def area(radius):
##    r = pi * radius * radius
##    print("area of the circle is a:",r)
##
##area(200)
##    


def percentage(total_marks,obtained_marks):
    per = obtained_marks / total_marks * 100
    print("percentage of the student is :-",per)


##percentage(720,560)

def simple_interset(p,r,t):
    s = p*r*t/100
    print("simple interset is a:-",s)

##simple_interset(100,20,1)

from math import factorial

def fact(num):
    print("factorial of the number:-",factorial(num))


##fact(5)

def even_odd(num):
    if num % 2==0:
        print("True")
    else:
        print("False")

##even_odd(7)


def addition(a,b):
    print("hi")
    def calculate():
        print("addition is a:-",a+b)

    return calculate

##v = addition(20,23)
##
##v()

def rect(l,w):
    def area():
        print("area of the rectriangle:-")
        u = l * w
        print(u)

    return area


##a = rect(200,23)
##
##a()
from math import *
def circle(radius):
    def area():
        d = pi * radius * radius
        print("area of the circle",d)

    return area

##w = circle(200)
##w()

def square_cube(num):
    def square():
        s = num * num
        print("sqaure is a:-",s)

    def cube():
        d = num * num * num
        print("the cube of the number is a:-",d)

    return square,cube
        
##g,e = square_cube(7)
##g()
##e()


def student(obtained_marks,total_marks):
    def percentage():
        print("----------student percentage------------")
        d = obtained_marks / total_marks * 100
        print("percentage is --",d)

    return percentage

##a = student(677,720)
##
##a()


def salary(basic):
    def gross_salary():
        HRA =  (basic * 20) / 100
        DA = (basic * 10) / 100

        total_salary = basic + HRA + DA

        print("total salary is :-",total_salary)

    return gross_salary

##a = salary(159)
##
##a()

def largest_tree(a,b,c):
    def find_largest():
        if (a > b and a > c):
                print("A is a largest number")

        elif(b>a and b>c):
            print("B is a largeset number")

        else:
            print("c is largest number")

    return find_largest

##s = largest_tree(20,30,10)
##s()

def discount(price):
    def calculate():
        d = price  - (price * 15) /100
        print("after discount price is a:-",d)

    return calculate
##
##a = discount(100)
##
##a()



def bank(balance):
    def deposit(amount):
        d = balance + amount
        print("after deposit your balance is a:-",d)

    def withdraw(amount):
        f = balance - amount
        print("after withdraw the a balance is a:-",f)

    return deposit,withdraw


##a,b = bank(10000)
##a(100)
##b(200)





class main:
    def bank(self,balance):
        print("hii")
        def deposit(amount):
            d = balance + amount
            print("after the deposit balance is a:--",d)

        def withdraw(amount):
            w = balance - amount
            print("after the withdraw balance is a:--",w)

        return deposit,withdraw



##a = main()
####a.bank(100)
##b,e = a.bank(100)
##
##b(200)
##e(10)

from math import *
class all_op:
    def arithmatic(self):
        print("******all opration*****")
        def add(t,g):
            print("addition is a:-",t+g)

        def sub(tt,bb):
            print("subtraction is a:-",tt-bb)

        def cube(num):
            d = num * num * num
            print("cube of the number is a:-",d)

        def square(num):
            f = num * num
            print("the a sqauare of the number is a",f)

        def area_circle(radius):
            t = pi * radius * radius
            print("the area of circle is a",t)

        def rect(l,w):
            e = l * w
            print("area of the rectriangle is a:-",e)

        def salary(basic):
            def gross_salary():
                gross = basic + (basic * 10)/100
                print("gross salary is a",gross)
            return gross_salary

        def temp(ceivn):
            e = (9/5) * ceivn + 32
            print("the tempercuture to the ceivn is a:-",e)

        def simple_interest(p,r,t):
            si = p*r*t/100
            print("simple interest is a:-",si)

        return add,sub,cube,square,area_circle,rect,salary,temp,simple_interest

            


##s = all_op()
##a,b,c,d,e,f,g,h,i= s.arithmatic()

##a(12,34)
##b(23,34)
##c(5)
##d(5)
##e(100)
##f(20,23)
##y = g(100)
##y()
##h(51)
##i(100,10,1)




import keyword as k


##print(k.kwlist)

import math as m

print(print.__module__)





















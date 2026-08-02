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


##def largest(a,b):
##
##    if a>b:
##        print("a is greater no")
##
##    else:
##        print("b is grater number")
##
##
##largest(12,34)
##
##
##



##for i in range(1,6):
##    print(i)
##
##
##
##
##a = 80
##b= 89
##
##print(pow(a,b))
##
##
##





##class A:
##
##    name = "roshan"
##
##    def self():
##        print("the name is a :-",A.name)
##        print("the name is a:-",a.name)
##
##
##
##    def self2(self):
##        print("non static method",self.name)
##        print("static name is a",A.name)
##
##
##a = A()
##a.name = "sonu"
##
##A.self()
##
##a.self2()
##
##



class A :

    def non(self):
        print("non static function")


    def statics():
        print("static method")
        a = A()
        a.non()


##A.statics()


class A:


    def  st():

        print("helloo.....")


    def std():
        print("hii........")

        A.st()


##A.std()


##class A:
##
##
##    def non(self):
##
##        print("helloo....")
##
##    def no1(self):
##
##        print("hiii...")
##        a.non()
##
##
##a = A()
##
##a.no1()


##for i in range(1,11):
##
##    print(i,f"table of [[ 2 to {i} ]] is a:--\t ",i**2,"cube is a:--\t",i**3)

    



##name = "roshan"
##
##print(name[0:6])
##
##for i in range(0,6):
##    print(name[i])
##
##



def display_name(name):
    print("the name is a:-",name)


##display_name("roshan")


def add(a,b):
    print("addition is a:-",a+b)


##add(20,200)


##for i in range(1,6):
##    print(str(i) * i)
    
def square(num):
    num1 = num * num 
    print("the square is a:-",num1)


##square(5)


##def per(total_marks,obtained_m):
##    f = obtained_m / total_marks * 100
##
##    print("percentage is A:-",f)
##
##per(720,710)



##def sum1(a,b):
##    c = a+b
##    return c
##
##e = sum1(12,34)
##e()

##def add():
##    a = 10
##    b = 20
##    c = a+b
##    return c
##
##
##a1 = add()
##
##print(a1)
##
##


##def sub(a,b):
##
##    c = a+b
##
##    return c
##
##a = sub(20,34)
##
##print(a)



##def square(num):
##
##    return num * num
##
##
##s = square(5)
##
##print(s)


def bmi(w,l):
    f = l*l
    
    return w * f


##b = bmi(10,20)
##print((b))



##def avg(num,num1,num2):
##    return num + num1 + num2 /3
##
##
##a = avg(12,34,55)
##
##print(a)



def per(total_m,obtained_m):
    return obtained_m / total_m * 100


##a = per(720,710)
##print(a)


##def func(m1,m2,m3,m4,m5):
##    return m1+m2+m3+m4+m5
##
##
##d = func(20,30,34,45,65)
##
##
##print(d)

def func(m1,m2,m3,m4,m5):
    return m1+m2+m3+m4+m5 / 5


##s = func(30,40,50,65,65)
##
##print(s)


def basic_salary(salary,hra,da):

    total = salary + hra + da

    return total


##a = basic_salary(10000,234,43)
##
##print(a)


def gst(salary):

    s = salary + (salary * 18) / 100

    return s


##a = gst(100)
##print(a)


def circumfrance(r):

    return 2 * (pi * r)


##s = circumfrance(20)
##print(s)


def greeting():
    def message():
        print("welcome in python")

    return message


##a = greeting()
##a()


def college():
    def depart():
        print("computer department")

    return depart

##a = college()
##
##a()


def add(a,b):
    def addition():
        print(a+b)
    return addition


##a = add(23,34)
##
##a()

def details():
    def python():
        print("hello python")

    def java():
        print("hello java")

    return python,java

##a,b = details()
##
##a()
##b()


def all_a():

    def add(a,b):
        print(a+b)

    def sub(a,b):
        print(a-b)

    def mul(a,b):
        print(a*b)

    def div(a,b):
        print(a/b)

    return add,sub,mul,div


##a,b,c,d = all_a()
##a(2,3)
##b(23,34)
##c(234,444)
##d(123,321)
##e(123,23)




class A:

    def B():
        print("hello")

        def E():
            print("hello guyss")

        return E

    def C(self):
        print("sonu pardeshi")

##a = A()
##
##A.C(a)
##
##s=A.B()
##s()














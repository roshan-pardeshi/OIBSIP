##
##
##
####print("roshan")
##
##
####a = 10
####
####print(a)
##
##
##a = 10
##
##b = "roshan"
##
##c = 23.5
##
####
####print(type(a))
####print(type(b))
####print(type(c))
##
####a = input("enter your name")
##
####print("name is a:-",a)
##
####
####a = 2
####print(type(a))
####
####b = float(a)
####
####print(type(b))
##
####a = int(input("enter the number"))
####
####b = int(input("enter the number 2:-"))
####
####c = a*a
##
####print("square is a:-",a)
####
####cube = b*b*b
####
####print("cube of the number is a:-",cube)
##
##
####import math as m
####
####
####a =  int(input("enter the number"))
####
####
####print(m.sqrt(a))
####
####print(m.factorial(a))
##
####from math import sqrt,factorial
####
####
####a = int(input("enter the number"))
####
####
####print(sqrt(a))
####
####print(factorial(a))
##
####from math import pi
####
####a = int(input("enter the radius"))
####
####
####area = pi * a * a
####
####print("area of a circle is a:-",area)
####
##
##
####a = int(input("enter the celius"))
####
####r = (9/5) * a + 32
####
####print("tempercuture is a",r)
##
####salary = int(input("his salary is increase by 18%"))
####
####
####s = salary + (salary * 18)/100
####
####print(f"increase by 18% :- {s}")
##
####a = int(input("enter the number 1:="))
####
####b = int(input("enter the second number"))
####
####
####print("first number {} second number is a {}".format(a,b))
##
##
##
####def a():
####    print("roshan")
####
####a()
##
####
####def b():
####    print("hello")
####
####a = b
####a()
##
####def m1():
####    print("--hi--")
####
####    def m2():
####        print("--hello--")
####
####    return m2
####
####
####a = m1()
####a()
##
##
####def m1():
####    print("roshan")
####
####def m2():
####    m1()
####
####m2()
##
######def m1():
######
######    def m2():
######        print("roshan")
######
######  
######
######        print("hi")
######
######    return m2
######
######
######a = m1()
####a()
####
##
##
####print(print.__module__)
##
##
##
####def m1():
####    def m2():
####        print("m2 is call")
####        m3()
####
####    def m3():
####        print("m3 function is a call")
####
####    return m2
####
####m = m1()
####
####m()
##
##
####from math import factorial,pi
####
####def math_operation(a,b):
####    print("using this function we perfrom multiple math operation")
####    
####    def add():
####        print("addition",a+b)
######        sub()
####        
####        
####    def sub():
####        print(f"substraction:-{a-b}")
######        mul()
####    
####
####    def mul():
####        print("multiplication",a*b)
######        div()
####
####    def div():
####        print("division",a/b)
######        square()
####
####    def square():
####        print("square of the number :-",a*a)
######        factorial2()
####    
####
####    def factorial2():
####        print(factorial(b))
######        cube()
####
####    def cube():
####        print("cube is a:--",a*a*a)
######        area_of_circle()
####
####    def area_of_circle():
####        q = pi * a * a
####        print("area of a circle is a:--",q)
######        area_of_rectriangle()
####
####    def area_of_rectriangle():
####        d = a * b
####        print("area of rectriangle:-",d)
####
####    return add,sub,mul,div,square,factorial2,cube,area_of_circle,area_of_rectriangle
####
####
####
####c,v,g,h,o,j,i,y,t= math_operation(12,34)
####c()
####v()
####g()
####h()
####o()
####j()
####i()
####y()
####t()
##
##
##
##
##
####def add(a,b):
####    print(a+b)
####
####add(12,34)
##    
##
####def sub(a,b):
####    print(a+b)
####
####
####sub(20,45)
##
##
####def mul(a,b):
####    print(a*b)
####
####
####mul(10,30)
####
####def div(a,b):
####    print(a/b)
####
####div(2,6)
##
####def simple(p,r,t):
####    a = (p*r*t)/100
####    print(a)
####
####simple(1000,4,23)
##
##
##
####def power(base,exponent):
####    a = base**exponent
####    print("power",a)
####
####power(20,45)
##
##
##
##
####def addition(a,b):
####    def calculate():
####        print("addition",a+b)
####
####    return calculate 
####
####v = addition(20,45)
####v()
##
##
####def rectriangle(l,b):
####    def area():
####        area1 = l * b
####        print("area of rectriangle",area1)
####
####    return area
####
####r = rectriangle(20,34)
####r()
##
##
##
####from math import *
####
####def circle(radius):
####    def area():
####        a = pi * radius * radius
####        print(a)
####
####    return area
####
####e = area(309)
####
####e()
##
##
####def square_cube(num):
####    def square():
####        a = num * num
####        print("square is a:-",a)
####        
####    def cube():
####        b = num * num * num
####        print("cube:-",b)
####
####    return square,cube
####
####
####s,v= square_cube(7)
####s()
####v()
##
##    
####def student(total_marks,obtained_marks):
####    def percentage():
####        a = obtained_marks / total_marks * 100
####        print("percentage of the function is a:-",a)
####
####    return percentage
####
####s = student(720,450)
####s()
####
##
####def salary(basic_salary):
####    def gross_salary():
####        HRA = (basic_salary * 20)/100
####        DA=(basic_salary * 10)/ 100
####
####        c = basic_salary + HRA + DA
####        print("gross salary is a:-",c)
####
####    return gross_salary
####
####
####t = salary(1000)
####t()
####
##
##
####def largest_of_three(a,b,c):
####    def find_largest():
####        if a>=b:
####            print("a is a greater number")
####        elif (b>c):
####            print("b is grater number")
####        elif (c>a):
####            print("c is greater number")
####        else:
####            print("c ")
####
####    return find_largest
####
####s = largest_of_three(45,67,88)
####s()
##
##
####def discount(price):
####    def calculate():
####        a = price - (price * 15) / 100
####        print("after applying 15% discount",a)
####
####    return calculate
####
####
####s = discount(1000)
####s()
##
##
####def eletricity(unit):
####    def bill():
####        if unit<100:
####            print("$ 5 per unit")
####        elif (unit>=100):
####            print("$ 7 per unit")
####        else:
####            print("your bill is remaining")
####
####
####    return bill
####
####s=eletricity(157)
####s()
####
####
####def bank_acc(balance,amount,withdraw_amount):
####    def deposit():
####        a = balance + amount
####        print("after deposit",a)
####
####    def withdraw():
####        c = balance - withdraw_amount
####        print(f"after withdraw the amount is a:--{c}")
####
####
####    return deposit,withdraw
####
####
####a,v = bank_acc(10000,2000,3000)
####
####a()
####v()
####
####
####
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##    
##        
####def smallest(a,b):
####    def small():
####        if a>b:
####            print("b is smallest number")
####        else:
####            print("a is a smallest number")
####
####    return small
####
####s = smallest(20,45)
####s()
##
####def even(num):
####    def even1():
####        if num % 2 == 0:
####            print("even")
####        else:
####            print("odd")
####
####
####
####    return even1
####
####a= even(7)
####a()
##
##
##
##
##
##
##
##def add(a,b):
##    z = a+b
##    return z
##
##add(10,30)












##a = 10
##b = 20
##
##print(a+b)
##print(a-b)
##print(a*b)
##print(a/b)
##print(a**b)
##print(a//b)



##name = input("enter your name:-")
##mob = int(input("enter your home mobile number"))
##add = input("enter the address")
##
##print("the name is a:-",name)
##print("the mobile number is a:-",mob)
##print("the address is a:-",add)
##
##print(type(name))
##print(type(mob))
##print(type(add))
##
##print("using formating")
##
##print("the name is a :-{} the mobile number is a:-{} the address is a:{}".format(name,mob,add))
##
##print(f"the name is a:-{name} the number is a:- {mob} the address is a:-{add}")



##
##from math import *
##
##print(factorial(5))
##
##print(sqrt(6))
##
##print(pi)
##
##a = remainder(5,4)
##
##print(a)




##def add():
##    a = int(input("enter the a value"))
##    b = int(input("enter the b value"))
##    c = a+b
##    print("addition of the number is a:-",c)
##
##add()


##def sub(a,b):
##    print("subtraction is a:-",a-b)
##
##sub(40,34)


##def add(a,b):
##    z = a+b
####    print(z)
##    return z
##
##
##def add1():
##    a = add(12,34)
##    print(a)
##
##
##add1()


##def salary(basic):
##    a = basic + (basic * 18) /100
##
##    print("after increasing the a salary",a)
##
##salary(10000)

##from math import pi
##def circle(radius):
##    def area():
##        a = pi * radius * radius
##
##        print("the area of circle is a:-",a)
##
##    return area
##
##s = circle(10)
##s()


##def rectriangle(l,w):
##    def area():
##        a = l * w
##        print("area of a rectriangle is a:-",a)
##
##    return area
##
##s = rectriangle(100,30)


##from math import *
##def circum(r):
##    print("hello")
##    def area_cir():
##        s = 2*(pi*r)
##
##        print("the circumfrance of the circle is a:-",s)
##
##    return area_cir
##
##a = circum(30)
a()
    





##def cei(celi):
##    def temp():
##        a = (9/5) * celi + 32
##        print("the celivn to the tempercuture is a:-",a)
##
##    return temp
##
##
####s = cei(20)
####s()














































##
##
####def add(a,b):
####    print(a+b)
####
####
######add(10,20)
####
####
####
####def add2():
####    a=10
####    b=30
####    print(a+b)
####
####
####def addition(a,b):
####    z = a+b
####    return z
####
####
######addition(200,300)
##
##
##
######----------------------------task1 ----------------------
####
####
####def display_name(name):
####    print(name)
####
####display_name("roshan")
####
####
######-----------------------task2---------------------------
####
####
####def add(a,b):
####    print("addition is:-",a+b)
####
####add(100,300)
####
####
######------------------task 3
####
####
####def find_square(num):
####    a = num*num
####    print("the square is:-",a)
####
####find_square(7)
####
####
######--------------task 4
####
####
####def rectriangle(length,width):
####    c = length * width
####    print("area of rectriangle",c)
####
####rectriangle(20,35)
####
##       task 5
##
##
##from math import pi
##def circle_area(radius):
##    c = pi*radius*radius
##    print("circle area is :-",c)
##
##circle_area(29)


####task 6
##def student_info(name,age,course):
##    print("student name:-",name)
##    print("student age:-",age)
##    print("student course name:-",course)
##
##student_info("roshan",45,"data science")
##
##
##


##def calculate_percentage(total_marks,obtained_marks):
##    percentages = obtained_marks / total_marks * 100
##    print("the percentage of the student:-",percentages)
##
##calculate_percentage(100,67)
##



##task  8


##def convert_celsius_to_fahrenheit(celsius):
##    c=(9/5)*celsius +32
##    print(c)
##
##
##convert_celsius_to_fahrenheit(20)
##


##def even_odd(num):
##    if num % 2 == 0:
##        print("even")
##    else:
##        print("odd")
##
##even_odd(6)
##

##
##def display_emp(emp_id,emp_name,emp_salary):
##    print("the emp id is a:-",emp_id)
##    print("the emp name is a:-",emp_name)
##    print("the emp salary:-",emp_salary)
##
##display_emp(1,'roshan',20000)
##



##def add(a,b):
##    v = a+b
##    return v


##def sub(a,b):
##    r = a-b
##    return r


##def mul(a,b):
##    d = a*b
##    return d
##
##
##
##def div(a,b):
##    f = a/b
##    return f



##def square(num):
##    a = num*num
##    return a
##
##def cube(num):
##    b = num*num*num
##    return b
##
##def simple_interest(p,r,t):
##    f = (p*r*t)/100
##    return f 


##def largest(a,b):
##    print(a>b)
##    print(a<b)
    
def bmi(weigth,height):
    f = height * height
    d = (weigth / f) 
    return d


##def average(num1,num2,num3):
##    d = num1 + num2 + num3/3
##    return d



##def subject(m1,m2,m3,m4,m5):
##    d = m1+m2+m3+m4+m5
##    return d

##def subject(m1,m2,m3,m4,m5):
##    d = m1+m2+m3+m4+m5 / 5
##    return d





##def basic(salary,hra,da):
##    f = salary + hra + da
##    return f


##def gst(bil):
##    d = bil -(bil*18)/100
##    return d


##from math import pi
##
##def circumfrance(radius):
##    f = 2*pi*radius
##    return f
##    



#############################################################################################










def display_name(name):
    print("name is a:",name)

##display_name("roshan")


def add(a,b):
    print(a+b)

##add(20,30)


def find_square(num):
    d = num * num
    print(d)

##find_square(6)


def rectriangle(a,b):
    print("area of rectriangle")
    d = a*b
    print("the area of a rectriangle is a:-",d)

##rectriangle(20,47)

from math import pi
def circle(radius):
    d = pi * radius * radius
    print("the circle area is a:-",d)

##circle(20)
    
def student_info(name,age,course):
    print("the name of student :-",name)
    print("the age of student is a:-",age)
    print("the course is student choice is a:-",course)

##student_info("roshan",34,"data science")


def calculate(total_marks,obtained_marks):
    d = obtained_marks / total_marks * 100
    print("the total marks of the student percentage is a",d)

##calculate(720,500)


def celsius_convert(celsius):
    d = (9/5) * celsius +32
    print("the tempercuture is a:-",d)

##celsius_convert(45)

def even_odd(num):
    d = num % 2==0
    print(d)

##even_odd(7)


def display_employee(emp_id,emp_name,emp_salary):
    print("the employee salary is a:-",emp_salary)
    print("the employee id is a:-",emp_id)
    print("the employee name is a:-",emp_name)

##display_employee(1,'roshan',500000)

def add(a,b):
    z = a+b
    return z



def sub(a,b):
    z = a-b
    return z


def mul(a,b):
    s = a*b
    return s

def div(a,b):
    d = a/b
    return d


def find_square(num):
    d = num * num
    return d

def cube(num):
    d = num * num * num
    return d


def largest(a,b):
    d = a>b
    print("a is largest number",a) 
    c = a<b
    print("b is largest number",b)


def simple(p,r,t):
    simple_interest = (p * r * t)/100
    print("the simple interest is a:-",simple_interest)
    return simple_interest

def bmi(lenght,width):
    bmi1 = lenght * lenght
    bmi2 =  width * bmi1
    return bmi2


def average(num1,num2,num3):
    total = num1+num2+num3 / 3
    return total


def subject(math1,math2,math3,SE,OS,DBMS):
    total_marks = math1+math2+math3+SE+OS+DBMS
    return total_marks

def basic(salary,HRA,DA):
    d = salary + HRA + DA
    return d


def GST(bill):
    d = bill - (bill * 18) /100
    return d


def accepts(radius):
    d = 2 * pi *radius
    return d



def welcome():
    print("welcome to python programming")


##welcome()


def  college_name():
    print("Gangamai College of Engineering")

##college_name()
    
def display_info():
    name  = "roshan"
    address = "kusumba gali no 4 tal dist dhule"
    roll_no = '12'
    pincode = '424302'

    print("the name is a:-",name)
    print("the address is a:-",address)
    print("the roll_no is a:-",roll_no)
    print("the pincode is a:-",pincode)


    print(f"name:{name} address{address} roll_no:-{roll_no} pincode {pincode}")

##display_info()


def five():
    a = 5
    print(a*1)
    print(a*2)
    print(a*3)
    print(a*4)
    print(a*5)
    print(a*6)
    print(a*7)
    print(a*8)
    print(a*9)
    print(a*10)

##five()


def star():
    print("*****")
    print("*****")
    print("*****")
    print("*****")


##star()


def current_year():
    year = '2026'
    print("the current year is a:-",year)

##current_year()

def even_odd():
    a = 7
    d = a%2==0
    print("even",d)

##even_odd()


def python_topic():
    print("python basic")
    print("python variables")
    print("python data types")
    print("python import module")
    print("python input fucation()")

##python_topic()



def company():
    print("TCS is my dream company")

##company()


def motivation():
    print("belive in your self")

##motivation()

def add(a,b):
    print(a+b)

##add(30,56)


def sub(a,b):
    print(a-b)

##sub(23,20)

def mul(a,b):
    print(a*b)


##mul(23,12)


def square(num):
    d = num * num
    print(d)

##square(7)

def cube(num):
    d = num * num * num
    print(d)

##cube(7)



def table(num):
    print(num*1)
    print(num*2)
    print(num*3)
    print(num*4)
    print(num*5)
    print(num*6)
    print(num*7)
    print(num*8)
    print(num*9)
    print(num*10)

##table(7)

def student(name,age):
    print("student name is a:-",name)
    print("student age is a",age)

##student("roshan",20)

import math as m
def circle(radius):
    d = m.pi*radius*radius
    print(d)

##circle(10)


def rectriangle(length,width):
    s = length * width
    print(s)

##rectriangle(200,45)


def percentage(total_marks,obtained_marks):
    a = obtained_marks / total_marks *100
    print(a)

##percentage(720,620)

def largest(a,b):
    print(a<b)

##largest(10,30)
















l 








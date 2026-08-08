




def greeting():
    def message():
        print("welcome to python")
##
##    message()
##
##greeting()


def college():
    def department():
        print("computer science")

    department()

##college()


def student():
    def details():
        student_name = input("enter the student name:-")
        roll_number = int(input("enter the number"))
        course = input("enter the course")

        print("student name:-",student_name)
        print("student roll_number:-",roll_number)
        print("student course name:-",course)

    details()

##student()



def company():
    def employee():
        emp = int(input("enter the employee id:-"))
        emp_name = input("enter the emp name:-")

        emp_address = input("enter address of the emp:-")

        print(f"emp id is a {emp} emp_name :-{emp_name} emp_address :- {emp_address}")

        print("emp id {} emp_name {} emp_address {}".format(emp,emp_name,emp_address))


    employee()

##company()


def show():
    def python():
        print("the python function is run")

    def java():
        print("the java function is run")

    python()
    return java


##a = show()
##a()


def addition(a,b):
    def calculate():
        print("addition is a:-",a+b)

    return calculate

##a = addition(20,45)
##a()


def rect(l,w):
    def area():
        a = l * w
        print("area of rectriangle:-",a)

    return area


##c = rect(23,45)
##c()


from math import pi,sqrt,factorial

def circle(radius):
    def area():
        print("area of circle")
        s  = pi * radius * radius
        print(s)

    return area


####s = circle(35)
##s()

def student(name,marks):
    def result():
        if marks >= 35:
            print(f"{name} == pass")
        else:
            print("fail")


    return result


##a = student("roshan",67)
##a()    


def salary(basic,HRA,DA):
    def gross_salary():
        s = basic + HRA + DA
        print("gross salary is a:-",s)

    return gross_salary

##a = salary(10000,345,3452)
##a()


def square(num):
    def calculate():
        num1 = num * num
        print("square of the function is a:-",num1)


    return calculate

##a = square(7)
##a()


def cube(num):
    def cube1():
        a = num * num *num

        print("the cube of the number",a)

    return cube1
##
##h = cube(6)
##h()

def largest(a,b):
    def find():
        if a>b:
            print("A is a greater number")

        else:
            print("B is a greater")

    find()


##largest(25,25.7)


def percentage(total_marks,obtained_marks):
    def calculate():
        d = obtained_marks / total_marks * 100
        print("percentage of the student is a:-",d)

    return calculate


##d = percentage(600,500)
##d()


def calculate(a,b):
    def add():
        print("addition is a:-",a+b)

    def sub():
        print("substraction is a-",a-b)

    def mul():
        print("multiplication is a:-",a*b)

    def div():
        print("division is a:-",a/b)

    add()
    sub()
    mul()
    div()
    return add,sub,mul,div

##
##a,b,c,d = calculate(45,56)
##
##a()
##b()
##c()
##d()


def number(num):
    def even():
        if num % 2 == 0:
            print("even :- ",num)

    def odd():
        if num % 2 == 1:
            print("odd:-",num)



    even()
    return odd

##a = number(3)
##a()
        
from math import factorial,pi
def math_operation(num):
    print("math opertion")

    def square():
        a = num * num
        print("square is a",a)

    def cube():
        a = num * num * num
        print("cube of the number is a:-{}".format(a))

    def factorial1():
        print(f"factorial is a:---{factorial(num)}")


    square()
    return cube,factorial1


##a,b = math_operation(5)
##a()
##b()


def student(name,marks):
    def display_details():
        print("the name of the student",name)
        print("hi")
        display_result()

    def display_result():
        print("student obtained marks",marks)

    return display_details


##a = student("roshan",34)
##
##a()

def bank_account(balance):
    def deposit(amount):
        c = balance + amount
        print("after deposit balance is a:-",c)
        withdraw(200)

    def withdraw(amount):
        d = amount - balance
        print(d)


    deposit(2000)
    withdraw(320)
    return deposit

##a = bank_account(20000)
##a()

    
def m1():
    print("hello")


    def m2():
        print("hello1")

    return m2

##
##a = m1()
##a()
##m1()
##del m1
##m1()
##          
##
##
##



##def  m1():
##    print("hello")
##
##def m2(a):
##    print("roshan")
##
##
##
##a = m1()
##a()



##print("1.deposit\n2.withdraw \n3.check balacnce")
##
####choice = int(input("enter your choice"))
##
##balance = int(input("enter your account balance"))
##
##while balance>0:
##    choice = int(input("enter your choice"))
##
##
##    match(choice):
##        case 1:
##            deposit=int(input("depost amount"))
##            balance+=deposit
##
##            print(balance)
##
##        case 2:
##            withdraw = int(input("enter your withdraw amount"))
##            balance-=withdraw
##            print(balance)
##
##        case 3:
##            print(balance)
##
##        case _:
##            print("invalid choice")









print("1.creadit card \n2.debit card\n3.upi \n4.cash")


choice=int(input("enter your choice:--"))

rm = input("select your payment mode cc.dt.upi.cash")

price = int(input("enter your shopping price"))

match(choice):
    case 1:
        if rm == 'cc':
            total_bill = price - (price * 15)/100
            print("the total discount use by cc paymnet is a:=",total_bill)
        else:
            print("no discount1")

    case 2:
        if rm == 'dt':
            total_bill = price - (price * 10)/100
            print("the total discount use by dt paymnet is a:=",total_bill)
        else:
            print("no discount2")

    case 3:
        if rm == 'upi':
            total_bill = price - (price * 5)/100
            print("the total discount use by upi paymnet is a:=",total_bill)
        else:
            print("no discount3")

    case 4:
        if rm == 'cash':
            total_bill = price - (price * 1)/100
            print("the total discount use by cash paymnet is a:=",total_bill)
        else:
            print("no discount")

    case _:
        print("not valid choice")

        



    

            
        














































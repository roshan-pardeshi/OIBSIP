##
##
##
##
####def m1():
####    print("hello")
####
####c = m1
####c()
##
##def m1():
##    print("m1---")
##
##    def m2():
##        print("h1")
##
##    m2()
##
####m1()
##
##def m1():
##    print("roshan")
##
##    def m2():
##        print("roshan1")
##
##    return m2

##a = m1()
##a()


##def m1():
##    x = int(input("enter the number 1:-"))
##    y = int(input("enter the number 2:-"))
##    z = x+y
##    print(z)
##
##    def m2():
##        print("hello")
##
##    return m2



##a = m1()
##a()
        

def m1():
    def m2():
        print("enter the number")

    return m2


##a = m1()
##a()
        
##def m1():
##    print("hello")
##
##    def m2():
##        print("hi")
##
##    return m2
####    print("roshan")


##a = m1()
##a()




def greeting():
    def message():
        print("welcome to python")


    return message


##a = greeting()

##a()



def college():
    def dept():
        print("computer department")

    return dept


##a = college()

##a()


def student():
    print("student detail")

    def details():
        name = "roshan"
        print("name of student is a",name)
        roll_number = '10'
        print("roll number of student",roll_number)
        course = "python"
        print("course od student is a:-",course)

    return details


##a = student()
##a()


def m1():
    print("hello")

    def m2():
        print("hi")

    m2()

##a = m1
##a()

##def company():
##    print("company employee detail")
##
##    def emp():
##        name = input("enter the employee name:-")
##        print("employee name:-",name)
##
##        emp_id = int(input("enter the emp_id:-"))
##        print("employee id is a:-",emp_id)
##
##    return emp
##
##
##a = company()
##a()



def show():
    def python():
        print("python function")

    def java():
         print("java function")

##    java()
    return python



##a = show()
##a()


def addition(a,b):
    def calculate():
        print("addition of the number is a:-",a+b)

    return calculate


##a = addition(10,20)
##a()

##def rectriangle(l,w):
##    def area():
##        rect = l*w
##        print("area of rectriangle is a:-",rect)
##
##    return area
##
##a = rectriangle(200,57)
##a()


from math import pi
def circle(radius):
    def area():
        a = pi * radius * radius
        print("area of the circle",a)

    return area


##c = circle(200)
##c()


def student(basic):
    def gross_salary():
        hra = 400
        da = 4000
        gross_salary = basic+hra + da
        print("gross_salary is a",gross_salary)

    return gross_salary


##a = student(20000)
##a()
        


def student(name,marks):
    def result():
        if marks >= 35:
            print(f"{name} pass")
        else:
            print(f"{name} fali")

    return result

a=student("roshan",77)
a()










































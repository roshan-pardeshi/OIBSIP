
##class roshan:
##    def details(name,address,course,age,self):
##        print("detail")
##        
##        print("name :-",name)
##        print("address :-",address)
##        print("course:-",course)
##        print("age",age)
##
##
##
##a = roshan()
##
##a.details("roshan","kusumba","python",20)

##class roshan:
##    def details(self):
##        print("name :- roshan")
##        print("address :- kusumba")
##        print("course python")
##        print("age :- 20")
##
##a = roshan()
##a.details()
    
##class emp:
##    def emp_detail(self):
##        emp_name = input("employee name:-")
##        emp_id = int(input("employee id:-"))
##        emp_company_name = input("enter company name:-")
##        emp_salary = int(input("enter the emp salary"))
##
##
##        print(f"name of emp [{emp_name}] \n emp_id :- [{emp_id}] \t emp_company_name :- [{emp_company_name}] \n emp_salary :- [{emp_salary}]")
##
##    def gross(self,name_emp):
##        print("name 0f emp is a:-",name_emp)
##
##                    
##
##a = emp()
##a.emp_detail()
##a.gross('roshan')



##class maths:
##    def add(self,a,b):
##        print("addition is a:-",a+b)
##
##
##    def sub(self,a,b):
##        print("subtraction is a:-",a-b)
##
##
##    def mul(self,a,b):
##        print("multiplication is a:-",a*b)
##
##
##    def div(self,a,b):
##        print("division is a:-",a/b)
##
##
##
##f = maths()
##f.add(10,30)
##
##r = maths()
##r.sub(20,15)
##
##e = maths()
##e.mul(23,5)
##
##t = maths()
##t.div(23,45)





##class a:
##    def add(self,a,b):
##        print(a+b)
##
##    def sub(self,a,b):
##        print("subtraction is a:-",a-b)
##
##    def mul(self,a,b):
##        print("multipliation is a:-",a*b)
##
##    def div(self,a,b):
##        print("division is a:-",a/b)
##
##
##ab = a()
##ab.add(20,34)
##ab.sub(45,67
##ab.mul(34,67)
##ab.div(23,45)





##class a:
##    def m1(a):
##        print("hi",a)
##
##        def m2():
##            print("roshan")
##
##        m2()
##
##aw = a()
##aw.m1()
        
        





##def m1(name):
##    def m2():
##        print("hello roshan")
##
##    def m3():
##        print("roshan address is a:",name)
##
##    return m2,m3
##
##
##
##d,s = m1("roshan")
##d()
##s()




##
##def add(a,b):
##    print("addition is a:-",a+b)
##
##
##def sub(a,b):
##    print("subtraction is a",a-b)
##
##def mul(a,b):
##    print("multipliation is a:-",a*b)
##
##def div(a,b):
##    print("division:-",a/b)
##
##
##add(20,45)
##sub(23,45)
##mul(45,56)
##div(34,56)


def square(num):
    p = num * num
    print("square is a:-",p)


square(7)


def cube(num):
    n = num * num * num
    print("the cube of the number is a:-",n)


cube(8)


def largest(a,b):
    if a>b:
        print("a is a largest number")
    else:
        print("b is largest number")

largest(34,56)


def smallest(a,b):
    if a>b:
        print("b is smallest number")

    else:
        print("a is smallest number")


smallest(3,6)




def rect(l,w):
    s = l * w
    print("area of the rectriangle is a:-",s)

rect(20,34)




from math import pi 
def area(radius):
    s = pi * radius * radius

    print("area of the circle",s)

area(200)


def per(total_m,obtained_m):
    s = obtained_m / total_m * 100
    print("percentage is a",s)

per(720,618)
    


def simple(p,r,t):
    s = (p * r * t)/100
    print("simple interest is a",s)


simple(10000,30,4)


from math import factorial


def fact(num):
    print(factorial(num))


fact(5)











    













































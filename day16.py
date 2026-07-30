
##class a:
##    a = 10
##    b = 20
##
##    def add(self):
##        c = self.a + self.b
##        print("addition is a:-",c)
##
##    def sub(self):
##        c = self.a + self.b
##        print("subtraction is a:-",c)
##
##    def mul(self):
##        c = self.a * self.b
##        print("multiplication is a",c)
##
##
####obj = a()
####obj.add()
####obj.sub()
####obj.mul()
##
##
##class a:
##    b = 10
##    c = 20
##
##    def rect(self):
##        res = self.b*self.c
##        print("area of the rectrinangle is a:--",res)
##        
##    def square(self):
##        res = self.b * self.b
##        print("square of the number is a:--",res)
##
##    def cube(self):
##        res = self.b * self.b * self.b
##        print("the cube of the number is a:-",res)
##
####obj = a()
##obj.rect()
##obj.square()
##obj.cube()



##from math import *
####class main:
##    a = 10
##    b = 20
##
##    def rect(self):
##        return self.a * self.b
##
##    def area_of_circle(self):
##        res = pi * self.a * self.a
##        return res
##
##    def triangle(self):
##        res = 0.5 * self.a * self.b
##        return res
##
##
####obj = main()
##print(obj.rect())
##print(obj.area_of_circle())
##print(obj.triangle())
####        



##class main:
##    def all(self):
##        def add(a,b):
##            print(a + b)
####            return a+b
##
##        def sub(a,b):
##            print("sub:-",a-b)
##
##        def mul(a,b):
##            print("multi:-",a*b)
##
##        return add,sub,mul
##
##
##
##c = main()
##
##d , f , e = c.all()
##
##d(20,10)
##f(30,23)
##e(2,4)
##


##class student:
##    def details(self,name,roll_number,course):
##        print("name is a",name)
##        print("roll number is a",roll_number)
##        print("course is a",course)
##
##
##a = student()
##a.details("roshan",1,"data")


class emp:
    emp_id = 1
    emp_name = "roshan"
    emp_salary = 10

    def emp_details(self):
        print("emp id is a:-",self.emp_id)
        print("emp name is a:-",self.emp_name)
        print("emp salary is a:-",self.emp_salary)


##e = emp()
##
##e.emp_details()


class car:
    car = "tata"
    model = 2014
    price = "4 lakh"

    def car_d(self):
        print("car name is a:-",self.car)
        print(f"car model is a{self.model}")
        print("car price is a",self.price)


##s = car()
##s.car_d()



class book:
    book_name = "python & data science book"
    author = "Ravi sir"
    price = 200

    def book_d(self):
        print("book name is a:-",self.book_name)
        print("book author name is a",self.author)
        print("book price is a:-",self.price)


##d = book()
##d.book_d()

class mobile:
    brand = "vivo"
    ram = "4 gb"
    price = 1000
    def mobile_d(self):
        print("mobile brand name is a:-",self.brand)
        print("mobile ram is a:-",self.ram)
        print("mobile price is a:-",self.price)


e = mobile()
e.mobile_d()












        
    







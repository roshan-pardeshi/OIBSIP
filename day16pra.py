

class student:
    name = "roshan"
    student_id = 1
    student_address = "ajintha height kasba peth pune"
    def details(self):
        print("the studnet name is :-",self.name)
        print("the student id is :-{}".format(self.student_id))
        print(f"student address is a:{self.student_address}")

##a = student()
##a.details()
##
##        
        
        
class employee:
        emp_id = 1
        emp_name = "roshan"
        emp_work = "data anaylsis"
        def emp_details(self):
            print(f"the emp_id :-{self.emp_id} emp_name:-{self.emp_name} emp_work:-{self.emp_work}")
    
##a = employee()
##a.emp_details()


class car:
    book_name = "python & data science"
    author = "roshan"
    price = "100 rs"

    def books(self):
        print(self.book_name)
        print(self.author)
        print(self.price)


##c = car()
##c.books()



class mobile:
    brand = "vivo"
    ram = "4 GB"
    price = "12k"
    
    def object(self):
        print("the brand of the mobile is a",self.brand)
        print(f"the ram of the mobile is a",self.ram)
        print("the price of the money:-{self.price}")
    

##s = mobile()
##s.object()

class student:
    name = "roshan"
    marks = "100"
    
    def display(self):
        print("the student name is a:-",self.name)
        print("the student marks",self.marks)


##a = student()
##a.display()



class laptop:
    brand = "hp"
    processor = "gaming processor"
    price = "50k"

    def  details(self):
        print(self.brand)
        print(self.processor)
        print(self.price)


##a = laptop()
##a.details()

class teacher:
    teacher_n = "ravi sir"
    subject = "python and data science"
    experience = "2 year"

    def info(self):
        print("the teacher name is a:-",self.teacher_n)
        print("the subject to teacher are teach:-",self.subject)
        print("the experience of the sir is a",self.experience)


##a = teacher()
##a.info()

class h:
    hospital_name = "universal hospital"
    location = "pune"
    
    def ho(self):
        print("the hospital name is a:-",self.hospital_name)
        print("the location of the hospital",self.location)



##a = h()
##a.ho()
        
class movie:
    def details_m(self,mov_name,hero_name,rating):
        print("the movie name is a",mov_name)
        print("the horo name is a:-",hero_name)
        print("the rating of the a movie is a:",rating)


##a = movie()
##a.details_m("kakan","randam hero","5 star")

class calculator:
    def add(self,a,b):
        print("addition is a:-",a+b)


    def sub(self,a,b):
        print("suntraction is a:-",a-b)

    def mul(self,a,b):
        print("the multiplication is a:-",a*b)


    def div(self,a,b):
        print("the division:-",a/b)



##a = calculator()
##a.add(10,23)
##a.sub(20,34)
##a.mul(2,4)
##a.div(23,45)


from math import *
class rect:
    def area(self,l,w):
        print("area of a rectriangle is a:-")
        r = l * w
        print(r)


        def circle(radius):
            print("area of the circle is a")
            d = pi * radius * radius
            print("area of the circle:-",d)

        return circle


##a = rect()
##s = a.area(200,300)
##
##s(100)



class square:
    side = 120
    def area(self):
        r = self.side * self.side
        return r


##a = square()
##print(a.area())
    
class multiplication_table:
    def table(self,num):
        for i in range (10):
            print(num*i)
            print(num)



##a = multiplication_table()
##a.table(5)
##


class bank:
    account_number = "123455"
    account_holder_name = "roshan vijay pardeshi"
    balance = "10000 RS"
    def display_d(self):
        print("the a account number is a:-",self.account_number)
        print("the account_holder_name is a:-",self.account_holder_name)
        print("the account balance is a:-",self.balance)


##a = bank()
##a.display_d()


class college:
    college_name = "Gangamai college of the engineering"
    college_location = "dhule maharastra"
    college_university = "north maharastra"


    def details(self):
        print("the college name is a:-",self.college_name)
        print("the college location is a:-",self.college_location)
        print("the college university name is a:-",self.college_university)

##a = college()
##a.details()

class bike:
    def details(self,bike_name,bike_brand,bike_price):
        print(f"the bike name is a----------",bike_name)
        print(f"brand name of the bike is:-",bike_brand)
        print(f"the bike price is a:-------",bike_price)


##a = bike()
##a.details("palsur","BAJAJ","125000rs")



class product:
    def product_d(self,product_id,product_name,product_price):
        print(f"the product id is {product_id} the product_name is a{product_name} the produc_price is {product_price}")


a = product()
a.product_d(1,"onion",30)


class customer:
    def info_cust(self,customer_id,customer_name,customer_city):
        print(customer_id)
        print("customer name is a:-",customer_name)
        print("customer home town:-",customer_city)


a = customer()

a.info_cust(1,"roshan","dhule")
        









        






              
































































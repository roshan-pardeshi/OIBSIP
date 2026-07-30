##
##
##class A:
##
##    def m1():
##        print("m1 is call by m2")
##
##    def m2(self):
##        print("m2 is non static method")
##        A.m1()
##
####a = A()
####a.m2()
##
##
##
##class A:
##
##    def m1():
##        print("static method")
##
##    def m2():
##        print("static method second")
##        A.m1()
##
####A.m2()
##
##
##class A:
##
##    print("hellow")
##

##a=A()
####a()


##class A:
##
##    def m1(self):
##        print("m1 method is a call")
##        A.m2()
##
##    def m2():
##        print("m2 method is a call")
##a = A()
##
##a.m1()



##class A:
##
##
##    x = 10
##    
##    def m1(self):
##        print("m1--a")
##        print("roshan",self.x)
##
##    def m2():
##        print("m2--a")
##        print("")
##
##
##a = A()
##
####a.m1()
##A.m1(a)
##a.name = "roshan"
##print(a.name)
##A.m2()


##class student:
##
##
##    pass
##
##
##a = student()
##a.name = "roshan"
##a.roll_no = 1
##a.address = "pune"
##
##
##print("name",a.name)
##print("roll_no",a.roll_no)
##print("address",a.address)




##class A:
##    def m1(self):
##        print(self.name)
##
##
##a = A()
####a.m1()
##a.name = "roshan"
##a.m1()
##





class A:
    borad_name = "mscb"

    def info():
        print(a.bord_name)


    def details(self):
        s = self.perivious_bill - self.current_bill
        print("the total unit is a:-",s)


##a = A()
##a.perivious_bill = 10
##a.current_bill = 20
##a.details()
##
##



class movie:
    def movie_info(self):
        print(self.movie_name)
        print(self.movie_hero)
        print(self.movie_director)


##a = movie()
##
##a.movie_name = "ved"
##a.movie_hero = "ritesh deshmukh"
##a.movie_director = "ritesh "
##
##movie.movie_info(a)





class animal:
    def display(self):
        print(self.animal_name)
        print(self.animal_color)
        print(self.animal_age)


##a=animal()
##
##
##a.animal_name = "lion"
##a.animal_color = "golden"
##a.animal_age = 23
##
##animal.display(a)


class flight:
    def flight_info(self):
        print(self.flight_name)
        print(self.flight_source)
        print(self.flight_destination)



##a = flight()
##a.flight_name = "D10"
##a.flight_source = "pune"
##a.flight_destination = "mumbai"
##
##
##a.flight_info()


class restaurant:
    def restaurant_info(self):
        print(f"the restaurant name is a {self.restaurant_name}")
        print("the restaurant type :--{}",self.restaurant_type)
        print(self.restaurant_rating)

##a = restaurant()
##a.restaurant_name = "roshan res"
##a.restaurant_type = "veg & non veg"
##a.restaurant_rating = "5 star"
##
##a.restaurant_info()


class bus:
    def bus_details(self):
        print("the bus number is a:-",self.bus_number)
        print("the bus route is a",self.bus_route)
        print("the bus time is a",self.bus_time)


##a = bus()
##a.bus_number = "12"
##a.bus_route = "pune to mumbai"
##a.bus_time = "10 to 12 pm"
##a.bus_details()


class university:
    university_name = "north maharastra unversity"

    def info(self):
        print("the name of the university is a:-",a.university_name)

        print("the student name is a:-",self.student_name)
        print("the student department name",self.student_depart)


##a = university()
##
##a.student_name ="roshan"
##a.student_depart = "computer science"
##
##
##a.info()

class library:
    library_name = "roshan collection"
    def library_info(self):
        print("the library name is a:-",a.library_name)
        print("the book name is a:-",self.book_name)
        print("the author of book is a :-",self.author_book)

##a = library()
##a.book_name = "python & data sciencs"
##a.author_book = "roshan pardeshi"
##
##a.library_info()
##            




class airline:
    airline_name = "TATA Airline"
    def airline_info(self):
        print(a.airline_name)
        print(self.airline_passenger_name)
        print(self.ticket_number)


##a = airline()
##
##
##a.airline_passenger_name = "roshan pardeshi"
##a.ticket_number = "D11"
##
##a.airline_info()



class mall:
    mall_name = "roshan mall"
    def mall_details(self):
        print(a.mall_name)

        print("the name of the a:",self.shop_name)
        print("the name of the floor",self.shop_floor)

##a = mall()
##a.shop_name="roshan ltd"
##a.shop_floor = "4--th"
##
##a.mall_details()


class hotel:
    hotel_name = "roshan kaa hotel"
    def hotel_details(self):
        print(a.hotel_name)
        print(self.customer_name)
        print(self.room_number)

##a = hotel()
##
##a.customer_name = "roshan pardeshi"
##a.room_number = "10se"
##
##a.hotel_details()
##        


class converter:
    def meter_to_centimeter(meter):
        s = meter * 100
        print("the meter to ceintimeter:-",s)


##converter.meter_to_centimeter(20)      


class converter:
    def kilometer_to_meter(kilometer):
        d = kilometer * 1000

        print("the kilometer to the meter is :-",d)

##converter.kilometer_to_meter(20)


class discount:
    def calculate(price):
        s = price - (price *10) / 100
        print(s)


##discount.calculate(100)

class vote:
    def eligiable(age):
        if age >=18:
            print("eligiable the candidate")

        else :
            print("the candidate is a eligiable")


##vote.eligiable(30)
  

class check_no:
    def number(num):
        if num > 0:
            print("the number is a positive")
        else:
            print("the number is a negetive")

##check_no.number(12)

class cinema:
    cinema_name = "joti cinema"
    def show_static():
        print("the a cinema name is a:-",a.cinema_name)

    def show_no_static(self):
        print(self.movie_name)
        print(self.movie_ticket)


##a = cinema()
##
##cinema.show_static()
##
##a.movie_name = "ved"
##a.movie_ticket = "200 RS"
##
##a.show_no_static()



class gym:
    gym_name = "RP--fitness"

    def gym_info():
        print(a.gym_name)

    def gym_details(self):
        print(self.member_name)
        print(self.membership_fees)

##a = gym()
##a.member_name = "roshan"
##a.membership_fees = "2000 RS"
##
##a.gym_details()
##
##
##gym.gym_info()


class courier:
    company_name = "infosys"

    def company_info():
        print(a.company_name)

    def company_details(self):
        print("the parcel is a:-",self.parcel_id)
        print("customer_name is a:-",self.customer_name)


##a = courier()
##a.parcel_id = "12@2420"
##a.customer_name = "roshan"
##a.company_details()
##courier.company_info()

class train:
    railway_zone = "high risk zone & safe zone"

    def zone_info():
        print("the zone details is a:-",a.railway_zone)

    def train_info(self):
        print("the train name is a:--",self.train_name)
        print("the train number is a:--",self.train_number)

##a = train()
##a.train_name = "indraying exprees"
##a.train_number = "D1234"
##train.zone_info()
##a.train_info()
##    
##



class exam:
    exam_name = "JEE & NEET"
    def exam_details():
        print("the details of the a exam is a:-",a.exam_name)

    def result_info(self):
        print("the name of the student is a:--",self.student_name)
        print("the marks of the student is a:-",self.marks_student)

##a = exam()
##a.student_name = "roshan"
##a.marks_student = "85%"
##a.result_info()
##exam.exam_details()


class bill:
    board_name = " mscb dhule "

    def board_details():
        print("the a borad name is a:-",a.board_name)

    def calculate(self):
        c = self.perivious_bill - self.current_bill

        print("the unit of the bill is A:-",c)


##a = bill()
##
##bill.board_details()
##
##a.perivious_bill = 20
##a.current_bill = 12.3
##
##a.calculate()
##    


class waterbill:
    department_name = "MSCB DHULE MAHARASTRA"

    def dep_details():
        print(a.department_name)

    def bill_amount(self,water_bill):
        print("the total water bill is a",water_bill)

##a = waterbill()
##waterbill.dep_details()
##a.bill_amount(12)
##



class emp_att:
    company_name = "TCS"
    position_package = " 4LPA "

    def company_details():
        print(a.company_name)
        print(a.position_package.rjust(20))

    def att_percentage(self,emp_name,emp_working_days):
        print("the employee name is a:-",emp_name)
        print("the empployee working days",emp_working_days)


##a = emp_att()
##emp_att.company_details()
##
##a.att_percentage("roshan","7 days working".rjust(200))
##


class online_course:
    platfrom_name = "corsera"

    def platform_name():
        print(f"the platfrom name is a:--{a.platfrom_name}")


    def course_info(self):
        print("the course name is :-",self.course_name)
        print("the course duration is a:-",self.duration)
        print("the course fees is a:-",self.fees_course)

##a = online_course()
##
##online_course.platform_name()
##
##a.course_name = "python and data science"
##a.duration = "6 mounth"
##a.fees_course = "60 k "
##
##a.course_info()


class vehicle_r:
    RTO_name = "Ravi kaka"

    def rto_info():
        print(a.RTO_name)

    def vehicle(self):
        print(self.bike_name)
        print(self.bike_number)
        print(self.owner_name)

##a = vehicle_r()
##vehicle_r.rto_info()
##a.bike_name = "pulsar--125"
##
##a.bike_number = "MH 18 BT 8174"
##
##a.owner_name = "roshan pardeshi"
##
##a.vehicle()
##
##    
##
##


##class A:
##
##    def m1():
##        print("m1 is static method")
##
##    def m2(self):
##        print("m2 is non static method")
##        A.m1()

##a = A()
##
##a.m2()

##class A:
##
##    def m1():
##        print("m1 is static method")
##
##    def m2():
##        print("the m2 is also static method")
##        A.m1()
##
##
##A.m2()
##




##class A:
##
##    def m1(self):
##        print("m1 is a non static method")
##
##    def m2(self):
##        print("m2 is a non static method also")
##        a.m1()
##
##
##a = A()
##a.m2()


##class A:
##
##    def m1(self):
##        print("h1")
##        
##        def m2():
##            print("hellow")
##
##            def m3():
##                print("m3 say hello")
##                
##            return m3
##
##        return m2
##    
##
##a = A()
##b = a.m1()
##c = b()
##c()

class A:

##    x = 10
    pass


a = A()
a.x = 20
print(a.x)

a1 = A()

print(a1.x)



    







































































































































































































































































































































































































        

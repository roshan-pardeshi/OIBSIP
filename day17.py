####
####
####
####
####class A:
####    
####    x = 20
####
####    
####    def m1(self,a,b):
####        print("m1--a")          #NON STATIC METHOD 
####        self.d = 200
####
####        
####
####    def m2():
####        print("m2 using class name")    #STATIC MRTHOD
######        print(a+b)
####        
####
####
######a = A()
######a.m1(20,20)
######a.x = 10
######a.y=20
######print(a.x)
######print(a.y)
######
######a.m1(20,20)
########A.m2()
######
######
######a.m1(20,23)
######
######
########a.x=10
########print(a.x)
########print(A.x)
####
######
######a1 = A()
######print(a1.x)
######
######a1.m2(a1)
######print(a1.x)
######
######A.m2(a1)
####
####
####
####
####
####class A:
####
####    x = 10
####    y = 20
####
####    def m1(self):
####        print("m1 is call by the object")
####
####    def m2():
####        print("m2 is called")
######        print(x)
######        print(y)
######        self.d=100
####
####
####a = A()
######A().m1()
######A.m1(a)
####A.m2()
####a.m1()
####
####A.m1(a)
####
######print(A.m2(a))
######a.m2()
######print(a.d)
##
##
##class movie:
##    movie_name = "kakan"
##    director = "roshan **"
##    rating = "5 star"
##
##    def details(self):
##        print(self.movie_name)
##        print(self.director)
##        print(self.rating)
##
##    def d():
##        print("roshan")
##        
##
####a = movie()
####a.x=10
####print(a.x)
####a.details()
####movie.d()
####movie.deta(a)
##
##
##
##class animal:
##    animal_name = "tushar"
##    color = "black"
##    age = "20"
##
##    def display(self):
##        print("animal name ",self.animal_name)
##        print("animal color",self.color)
##        print("animal age",self.age)
##
##
####a = animal()
####animal.display(a)
##
####class  flight:
####    flight_number = 1232
####    source = "pune"
####    destination = "mumbai"
####
####
####    def info(self):
####        print("the flight",self.flight_number)
####        print("the source",self.source)
####        print("the destination",self.destination)
####
####
####a = flight()
####
####flight.info(a)
##
####class restaurant:
####    restaurant_name = "roshan"
####    food_type = " veg & non-veg"
####    rating = "5 star"
####
####    def restaurant_info(self):
####        print("restaurant name ",self.restaurant_name)
####        print("food type",self.food_type)
####        print("rating ",self.rating)
####
####
####a = restaurant()
####a.restaurant_info()
##
##
##
##
##
##class bus:
##    bus_number = 1
##    route ="dhule"
##
##    def bus_details(self):
##        print(self.bus_number)
##        print(self.route)
##
##
####a = bus()
####bus.bus_details(a)
##
##class d:
##    def m1(self):
##        print(self.name)
##        print(self.id)
##
##
##a = d()
##a.name ="roshan"
##a.id = 10
##
##d()



















class movie:
    def details(self):
        print(self.movie_name)
        print(self.director)
        print(self.rating)



##a = movie()
##a.movie_name = "ved"
##a.director = "ritesh deshmukh"
##a.rating = "5 star"
##movie.details(a)
##



class animal:
    def display(self):
        print("animal name is a:-",self.animal_name)
        print("animal color :-",self.animal_color)
        print("animal age",self.animal_age)


##a = animal()


##a.animal_name = "dog"
##a.animal_color = "black"
##a.animal_age = 10
##
##animal.display(a)



class flight:
    def flight_info(self):
        print(self.flight_number)
        print(f"source of the flight {self.flight_source}")
        print("the flight destination is {}".format(self.flight_destination))


##a = flight()
##
##a.flight_number = "D11"
##a.flight_source = "pune"
##a.flight_destination = "mumbai"
##
##
##flight.flight_info(a)



class restaurant:
    def restaurant_info(self):
        print(self.restaurant_name)
        print(self.food_type)
        print(self.rating)


##a = restaurant()
##
##a.restaurant_name = "baba ka dhaba"
##a.food_type = "veg & non veg"
##a.rating = "a1"
##
##restaurant.restaurant_info(a)
##
##


class bus:
    def bus_details(self):
        print(f"the bus number is a{self.bus_number}")
        print("the bus route is a:-",self.bus_route)
        print("the bus fare is a:-",self.bus_fare)


##a = bus()
##a.bus_number = 1
##a.bus_route = "karvynager"
##a.bus_fare = " i dont under stand the meaning of this word"
##
##bus.bus_details(a)

class university:
    university_name = "north maharastra university"

    def detalis(self):
        print("the university name is a:-",self.university_name)
        print("the student name is a:-",self.student_name)
        print("the name of the department",self.department)


##a = university()
##
##a.student_name = "roshan"
##a.department = "computer name"
##
##
##university.detalis(a)
##


class library:
    library_name = "pardeshi libaray "
    def info(self):
        print("the book name is a:-",self.book_name)
        print("the autor of the a name is a:-",self.author)
        print("the library name is a:-",self.library_name)


##a = library()
##
##
##a.book_name = "pyhton & data science"
##a.author = " roshan pardeshi"
##
##library.info(a)


class airline:
    airline_name = "TATA Airline"
    def information(self):
        print(f"airline name is a:-",self.airline_name)
        print("passenger name is a:-",self.passenger_name)
        print("ticket number is a:-",self.ticket_number)


##a = airline()
##
##a.passenger_name = "pratik patil"
##a.ticket_number = "D103540"
##
##airline.information(a)

class mall:
    mall_name = "zudio"
    def details(self):
        print("the mall name is a:-",self.mall_name)
        print("the shop name is a:-",self.shop_name)
        print("the floor number of the shop:-",self.floor_number)



##a = mall()
##a.shop_name="roshan"
##a.floor_number = "3 floor"
##
##mall.details(a)

class hotel:
    hotel_name = "baba ka dhaba"
    def info_hotel(self):
        print("the hotel name is a:-",self.hotel_name)
        print("the customer name is a:-",self.customer_name)
        print("the room numberof the customer:-",self.room_number)


##a = hotel()
##
##
##a.customer_name = "roshan"
##a.room_number = "123"
##
##hotel.info_hotel(a)
##



class converter:
    def meter_to_centimeter(self,meter):
        print("before conversion :-",meter)
        a = meter * 100
        print("after the convertion the:-",a)

        def kilometer_to_meter(kilometer):
            s = kilometer * 1000
            print("the after conversion:-",s)

        return kilometer_to_meter


##a = converter()
##b = a.meter_to_centimeter(20)
##
##b(200)


class discount:

    def discount_price(self,price):
        discount_after = price - (price * 10) /100
        print("after the discount the total price is a:-",discount_after)


##a = discount()
##a.discount_price(100)

class vote:
    def voting(age):
        if age >=18:
            print("eligiable for vote:**",age)

        else:
            print("not eligiable for vote:**",age)

##a = vote()
##vote.voting(19)



class number_check:
    def po_ne(num):
        if num > 0:
            print("the number is a positive")

        else:
            print("the number is a negative:**")

##a = number_check()
##number_check.po_ne(-1)

class cinema:
    cinema_name = "hit"
    
    def show_cinema():
        print("the cinema name is a",a.cinema_name)
        

    def show_movie(self):
        print("the movie name is a:=",self.movie_name)
        print("the movie ticket price:=",self.ticket_price)



##a = cinema()
##cinema.show_cinema()
##a.movie_name="ved"
##a.ticket_price ="1000"
##
##cinema.show_movie(a)



class gym:
    gym_name = "rk fiteness"

    def gym_info():
        print("the gym name is a:-",a.gym_name)

    def member_info(self):
        print("the member name ::--",self.member_name)
        print("the membership_fee ::--",self.membership_fee)

##a = gym()
##gym.gym_info()
##a.member_name = "roshan"
##a.membership_fee = "12k"
##a.member_info()

        




class courier:
    company_name = "tcs"

    def company_info():
        print("the company name is a:--",a.company_name)

    def parcel_info(self):
        print("the parcel id is a:-=",self.parcel_id)
        print("the customer name is a:==-",self.customer_name)


##a = courier()
##courier.company_info()
##
##a.parcel_id = 1
##a.customer_name = "roshan"
##
##a.parcel_info()


class train:
    raliway_name = "maharastra"

    def zone_info():
        print("the a raliway name is a:-",a.raliway_name)

    def train_info(self):
        print("the train route is a:-",a.train_route)
        print("the train stating date is a:-",a.train_date)



##a = train()
##train.zone_info() # static method is call
##
##a.train_route = "dhule to pune"
##a.train_date = "12/05/2026"
##
##train.train_info(a) # non static method is a call
##a.train_info()  #anthor method is a:==


class exam:
    exam_name = "MHT-CET"
    
    def info():
        print("the exam name is a:--",a.exam_name)

    def result_info(self):
        print("the student marks is a:-",self.student_marks,self.exam_name)
        print("the student name is a:-",self.student_name)




##a = exam()
##exam.info()
##
##a.student_name="roshan"
##a.student_marks="99"
##
##a.result_info()

class electricity:

    board_name = "mh"

    def board_info():
        print("the borad info is a:-",a.board_name)

    def board_unit(self):
        total_bill = self.previous_bil - self.current_bil
        
        print("the a board unit is a:-",total_bill)


##a = electricity()
##electricity.board_info()
##a.previous_bil = 100
##a.current_bil = 20
##
##a.board_unit()
##electricity.board_unit(a)


class water_bill:
    depart_name = "mscb mumbai"

    def depart_info():
        print("the department information is a:-",a.depart_name)

    def bill_account(self,water_unit):
        print("the water unit is a:---",water_unit)



##a = water_bill()
##water_bill.depart_info()
##a.bill_account(20)




class emp_a:
    emp_id = "D10"
    emp_name = "roshan"


    def info():
        print("the emp id is a:--",a.emp_id)
        print("the emp_name is a:--",a.emp_name)

    def details(self):
        print("emp_company name is a:-",self.emp_company_name)
        print("the emp_working days:--",self.company_working_days)


##a = emp_a()
##emp_a.info()
##
##a.emp_company_name = "tcs"
##a.company_working_days = "7 days in week"
##a.details()




class online_c:
    platform_name = "coursera"

    def platform_info():
        print("the platform name is a:-",a.platform_name)

    def course_info(self):
        print("the course name is a",self.course_name)
        print("the course duration is a",self.course_duration)
        print("course fees is a:-",self.course_fees)

a = online_c()

online_c . platform_info()


##a.course_name = "python & data science"
##a.course_duration = "6 mouth"
##a.course_fees = "60 k "
##a.course_info()
##


class vehicle_r:
    rto_name = "ravi pardeshi"

    def rto_details():
        print("the rto name is a:-",a.rto_name)


    def vehicle_details(self):
        print("the vehicle name is a:--",self.vehicle_name)
        print("the vehicle number is a:--",self.vehicle_number)
        print("the type of the vehicle is a:-",self.vehicle_type)
        print("the vehicle owner name is a:-",self.owner_vehicle)


a = vehicle_r()

vehicle_r.rto_details()

a.vehicle_name = "pulsar"
a.vehicle_number = "MH 18 BT 8174"
a.vehicle_type = "bike"
a.owner_vehicle = "roshan"

a.vehicle_details()















    


































        

        











































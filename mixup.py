



##for i in range(1,101,1):
##    if i % 2 ==0:
##        print("even#####################",i)
##    else:
##        print("odd---------------------------",i)
##    


##name = "python"
##
####for i in range(0,len(name),1):
####    print(name[i])
##
##print(name[0:4])


##course = "data science"
##count=0
##for i in range(1,len(course),1):
##    if course[i]=='a' or course[i]=='e' or course[i]=='i' or course[i]=='o' or course[i]=='u':
##        print(course[i])
##        count+=1
##
##print(count)


##name = "roshan"
####print(len(name))
##
##for i in range(5,-1,-1):
##    print(name[i])



##name = input("enter your name:--")
##
##
##for i in range(1,len(name),1):
##    if name[i] == 'a' or name[i] == 'e' or name[i] =='i' or name[i]=='o' or name[i] =='u':
##        print("vowel word")
##
##    else:
##        print("consonet word",name[i])


##vowel = "programming"
##
##count = 0
##for i in range(1,len(vowel),1):
##    if vowel[i]=='a' or vowel[i]=='e' or vowel[i]=='i' or vowel[i]=='o' or vowel[i]=='u':
##        print("vowel is a",vowel[i])
##        count+=1
##
##print(count)

##fact = 1
##
##def fact(num):
##    fact = 1
##    for i in range(1,num+1,1):
##        fact = fact*i
##        
##
##    print("factorial",fact)
##
##fact(5)
##
##num = int(input("enter the number for fibonacci series"))
##a = 0
##b = 1
##
##for i in range(1,num+1,1):
##    print(a)
##    c = a+b
##    a=b
##    b=c
##
####print(a)



##def solved(n):
##    num=n
##    factor = 0
##    for i in range(2,num-1,1):
##        if num % i==0:
##            factor += 1
##
##
##    if factor == 0:
##        print("number is  a prime number",num)
##    else:
##        print("not a prime number")
##
##for i in range(1,101,1):
##    solved(i)
##        
##




##for i in range(10,100,1):
##    if i%2==0:
##        print("even numbers--",i)
##
##        



##for i in range(0,101,5):
##    print(i)






##no= int(input("enter the number"))
##rev = 0
####no =0
##no1 = no
##while(no1>0):
####    print("heyy...............")
##    a = no1 %10
##    rev = rev*10+a
##    no = no1/10
##
##if rev==no1:
##    print("the number is palindrome")
##else:
##    print("the number is not a palindrome")




class movie:
    def details_movie(self):
        print(self.movie_name)
        print(self.movie_rating)
        print(self.movie_hero_name)


##a=movie()
##a.movie_name="ved"
##a.movie_rating="5 Star"
##a.movie_hero_name="ritesh deshmuhuk"
##a.details_movie()

##class animal:
##    def animal_details(self):
##        print(self.animal_name)
##        print(self.animal_color)
##        print(self.animal_age)
##        print(self.animal_address)
##
##
##a = animal()
##a.animal_name="tushar"
##a.animal_color = "black"
##a.animal_age = "21"
##a.animal_address = "dhule"
##
##a.animal_details()



##class flight:
##    def details(self):
##        print("flight name is a",self.flight_name)
##        print("sourse of the flight",self.flight_sourse)
##        print("destination of flight",self.flight_destination)
##        print("plit name",self.flight_coplit_name)
##        print("air hostage name is a",self.flight_airhostage_name)
##
##a = flight()
##a.flight_name = "air india"
##a.flight_sourse ="pune"
##a.flight_destination = "mumbai"
##a.flight_coplit_name = "roshan bhau"
##a.flight_airhostage_name = "tushar"
##
##flight.details(a)
##
##print("second flight started here")
##
##a1 = flight()
##a1.flight_name = "indigo"
##a1.flight_sourse ="dhule"
##a1.flight_destination = "mumbai"
##a1.flight_coplit_name = "roshan"
##a1.flight_airhostage_name = "manish"
##
##
##flight.details(a1)
##




##class university:
##    university_name="north maharastra university"
##
##
##    def details(self):
##        print("university name is a",university.university_name)
##        print("student name is a:-",self.student_name)
##        print("department name is a:-",self.student_department)
##
##a = university()
##a.student_name = "roshan"
##a.student_department = "computer science"
##
##a.details()
##


##
##class train:
##    train_name = "roshan express"
##
##    def zone():
##        print(train.train_name)
##
##    def zone_2(self):
##        print(self.train_num)
##        print(self.train_ticket)
##
##
##a = train()
##train.zone()
##a.train_num = "1"
##a.train_ticket = "D103240"
##a.zone_2()
##


##
##
##class A:
##
##    def B(self):
##        print("hello")
##
##        A.c()
##
##
##    def c():
##        print("its a static method")
##
##
##a = A()
##a.B()
##


class A:

    def B(self):
        print("hi i am first question")

        def C():
            print("hi  i am  inner fuction")

##            def d():
##                print("i am inside function and function")

##            return d

        return C


##a = A()
##a1 = a.B()
####a2 = a1.C()
##a1()








def demo():
    def python():
        print("hello this is a python function")

    def java():
        print("java function is a java function")

    return python,java

##a,b = demo()
##a()
##b()



##name = "roshan"
##
##age = 20
##
##
##print("the name is a:-",name)
##print("the age is a:--",age)
##
##
##print("---------------------------------formating method-----------------------------------")
##
##
##print(f"the name is {name} the age is a:- {age}")
##
##
##print("the name is a {} the age is a {}".format(name,age))


##a = input("enter the a value")
##
##print("the a value is a:-",a)
##



##from math import factorial,sqrt,pi
##
##print(factorial(5))
##
##print(pi)
##
##print(sqrt(4))
##
##
##








##a = int(input("enter the value"))
##
##b =int(input("enter the value"))
##
##
##if a>0 and b>0:
##    print("quarant--1")
##elif a<0 and b>0:
##    print("quarant--2")
##elif a<0 and b<0:
##    print("quarant--3")
##elif a>0 and b<0:
##    print("quarant--4")
##


##angle = int(input("enter the a degree of the angle is a:-"))
##
##
##if angle ==90:
##    print("right angle")
##elif angle<90:
##    print("acute angle")
##elif angle>90:
##    print("octa angle")
##














##no = int(input("enter the number"))
##
##
##rev = 0
####no1 = 0
##no1 = no
##
##while no1>0:
##    a = no1 % 10
##    rev = rev * 10 + a
##    no1 = no1 // 10
##
##if rev==no:
##    print("the number is a palindrome")
##else:
##    print("the number is an not palinfrome",rev)











##                                                                                PRIME NUMBER


##                                                                          divisiable by 1 and it self





##def prime_number(num):
##
##    fact = 0
##    for i in range(2,num-1,1):
##        if num % i ==0:
##            fact +=1
##
##    if fact ==0:
##        print("yes it's prime")
##    else:
##        print("not prime")
##
##
##t = int(input("enter the number"))
##prime_number(t)




##num = 5
##fact = 1
##
##for i in range(1,num+1):
##    fact = fact * i
##
##print(f"factorial is a :-- number is a {num} factorial is a:--",fact)


##import math as m
##
##
##print(m.factorial(6))


##a = 10
##print("before swaping",a)
##
##b = 20
##print("after swapinh",b)
##
##print("swaping")
##
##a = a+b
##b = a-b
##a = a-b
##
##print("a is an",a)
##print("b is an",b)






































##num = int(input("enter"))
##
##fact = 1
##
##
##for i in range(1,num+1):
##    fact = fact * i
##
##
##print(fact)




##a = 0
##b = 1
##
##num = int(input("enter the number"))
##
##for i in range(1,num+1):
##    print(a)
##    c = a+b
##    a=b
##    b=c


##num = int(input("enter the number"))
##
##
##cube = 0
##
##no = num
##
##
##for i in range(1,num+1,1):
##    a = no % 10
##    cube = cube * a**a
##    no = no // 10
##
##if cube == no:
##    print("amstrong number")
##else:
##    print("not amstrong number")



##name = "roshan"
##
##res = 0
##
##
##for i in range(1,len(name),1):
##    res +=1
##
##print(res)





##name = "roshan"
##
##res = 0
##
##for i in range(len(name)-1,-1,-1):
##    print(name[i])

##def prime(n):
##    num = n
##
##    factor = 0
##
##    for i in range(2,num+1,1):
##        if num  % 2 == 0:
##            factor+=1
##
##
##    if factor == 0:
##        print("prime number :---------------------------------------------$",num)
##    else:
##        print("not a prime number:---",num)
##
##
##
##
##for i in range(1,101,1):
##    prime(i)


##def sonu():
##    for i in range(1,5,1):
##
##        for i in range(5,0,-1):
##            d="*" * i
##            print(d.rjust(40))
##
##        a = "*" * i
##        print(a.rjust(20))
##        
##    
##
##
##    for i in range(5,0,-1):
##        b="*" * i
##        print(b.rjust(20))
##
##sonu()




##for i in range(10,100,1):
##    d1 = i % 10
##    d2 = i// 10
##
##
##    if d1%2==0 and d2%2==0:
##        print("even",i)


##    
##def salary(basic):
##    d = basic + (basic* 10)/100
##
##    print(d)
##
##salary(100)



##def all():
##    def java():
##        print("java")
##    def python():
##        print("python")
##
##    return java,python
##
##a,b= all()
##
##a()
##b()
##
##



##print("1.addition\n 2.substraction\n 3.multiplication")
##choice = int(input("enter your choice"))
##
##
##match(choice):
##    case 1:
##        print("addition")
##    case 2:
##        print("substraction")
##        
##    case 3:
##        print("multiplication")


##class A:
##
##    def B():
##        print("hello")
##
##    def C(self):
##        print("heyy....")
##
##a = A()
##
##A.B()
##
##a.C()



##class A:
##    name = "roshan"
##
##    def st():
##        print(a.name)
##
##    def no_st(self):
##        print(self.name)
##
##a = A()
##a.no_st()
##A.st()




##class A:
##
##    name ="roshan"
##
##    def st():
##        print(a.name)
##
##    def no_st(self):
##        print("address",self.address)
##        print("age",self.age)
##
##
##a = A()
##
##A.st()
##a.address ="kusumba"
##a.age = 20
##A.no_st(a)





##num =10
##for i in range(1,10,1):
##    a = i** 3
##    print(a)



##name = "roshan"
##
##res = 0
##
##for i in range(1,len(name),1):
##    res = res + 1
##
##print(res)


##def rect(l,w):
##
##    d = l*w
##
##    print("area of the rectriangle",d)
##
##rect(10,34)


##name = "roshan"
##
##res = 0
##
##for i in range(1,len(name),1):
##    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] =='o' or name[i] =='u':
##        res+=1
##
##print(res)
##        


























































































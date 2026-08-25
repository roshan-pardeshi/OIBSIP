##
##
##
##
##
##
####
####class Student:
####
####    def __init__(self,rollno,name):
####        self.rollno = rollno
####        self.name = name
####
####    def __str__(self):
####        return f"the rollno {self.rollno} name is a{self.name}"
####
##
##class A:
##
##    def __init__(self,roll_no,name,age):
##        self.roll_no=roll_no
##        self.name = name
##        self.age=age
##
##
##    def __str__(self):
##
##        return f"the roll number is a :--{self.roll_no} the name is:--{self.name} the age is a{self.age}"
##
##
##while True:
##
##    choice= int(input("enter your choice"))
##    match(choice):
##        case 1:
##
##            n = int(input("enter the number you add"))
##
##            li = []
##
##            for i in range(n):
##                a = A(int(input("add roll number")),input("enter the name"),int(input("age is a")))
##                li.append(a)
##
##
##            for i in li:
##                print(i)
##
##        case 2:
##            enter = int(input("enter the number you remove roll number"))
##
####            li = []
##            a =[]
##
##            for i in range(len(li)):
##                if li[i]==enter:
##                    a=li[i]
##
##
##                print("emtey list",li[a])
##
##


##li = [1,2,3,4,5]
##
##
##li.remove(2)
##
##print(li)


##tu = (1,2,3,4,5)
##
##
##print(tu.count(2))
##
##print(tu)
##
##
##
##
##print(type(tu))
##
##d = list(tu)
##
##d.remove(2)
##
##print(d)
##print(type(d))


##def neon(n):
##
##    a = n
##
##
##    num = a**2
##
##    b=0
##    for i in str(num):
##        b+=int(i)
##
##
##        if b==a:
##            print("neon number---",a)
####        else:
####            print("not neon number")
##
##for i in range(0,100,1):
##    neon(i)

##
##def haradh(n):
##num = n
##
##a = 0
##for i in str(num):
##    a +=int(i)
##
##
##if num % a==0:
##    print("harshd number:-----",a)
####        else:
####            print("not a harshd number")
##
##
##for i in range(1,100,1):
##    haradh(i)
##
##    




##num = 153
##
##
##cube = 0
##
##no = num
##
##for i in range(1,num+1,1):
##    a = no%10
##    cube = cube + a**a
##
##    no = no//10
##
##if cube==num:
##    print("a:")
##else:
##    print("not")
##



num = 145


fact = 0


for i in range(0,num+1,1):
    fact =fact * i


pr





































   

#####print("hello")
####
####
####a=10
#####b=10
####
#####print(a+b)
#####print(a-b)
#####print(a*b)
#####print(a/b)
####
####
####a=10
####
####
####
#####if a%2==1:
####  #  print("prime")
#####else:
####    #print("not")
####
####
#####a=10
#####b=20
####
#####for i in range (2):
####    #a=a^b
####    #b=a^b
####   # c=a^b
####
#####print(a)
#####print(b)
####
####
####
####
####a=10
####b=20
####
####print(a//b)
####
#####a=0
#####b=1
#####n=int(input("enter the number"))
####
#####for i in range (n):
####    #print(a)
####    #c=a+b
####   # a=b
####    #b=c
####
####num = int(input("Enter a number: "))
####
####original = num
####reverse = 0
####
####while num > 0:
####    digit = num % 10
####    reverse = reverse * 10 + digit
####    num = num // 10
####
####if original == reverse:
####    print("Palindrome Number")
####else:
####    print("Not a Palindrome Number")
####
##
####from all_tasks import *
####
####
####print("hellow dosto")
####
####
####e = add(20,23)
####print((e))
####
####print("hellow i am run second ")
##
##
##
##
##from Student import Student
##
##print("1.add paient\n2.remove paient 3.exit")
##
####a = input("paient add paient remove")
##c = []
##while True:
##    a = input("paient add paient remove")
##    if a==" add":
##
##        li=[]
##        n = int(input("enter the number"))
##
##
##        for i in range(n):
##            a = Student(int(input("enter the rollno:-")),input("enter the name"))
##            li.append(a) 
##
##
##
##        for i in li:
##            print(i)
##
##    elif a==" remove":
##        roll_number = int(input("enter the roll number of the paient"))
####        li= li.split()
##        for i in range(0,len(li),1):
##            if li[i]==roll_number:
##                li.remove(li[i])
##
##        print(li[i])
##            
##    elif a==" show":
##        for i in li:
##            print("currently add student",i.rollno,"currently add the name",i.name)
####            print(i.name)




##
##class A:
##
##    def __init__(self,rollno,name,age):
##        self.rollno = rollno
##        self.name = name
##        self.age = age
##
##
##    def __str__(self):
##
##        return f"Roll_number:-{self.rollno} Name:-{self.name} age :-{self.age}"
##
##
##
##
##n = int(input("enter the how many user you add in the given method:-"))
##
##li=[]
##
##for i in range(n):
##    a = A(int(input("enter the Rollno:-")),input("enter the a name:-"),int(input("enter the a age")))
##    li.append(a)
##
##user = input("enter")
##
##l = 0
##for i in li:
##    if user=="remove":
##        li.remove(li[l])
##        print(li)
##    else:
##        print(i)
##        



##
##li = []
##
##
##a = input("enter the name")
##
##
##
##
##for i in range(len(a)-1,-1,-1):
##    print(a[i],end="")



##
##num = 15
##
##
##num = str(num)
##
##
##if num==num[::-1]:
##    print("palindrome")
##else:
##    print("not palindrome")
##










##li = "roshan pardeshi"
##
##
##for i in range(0,len(li),1):
##    print(li[i][::-1],end="")
##
##




##a = {1,2,3,4,54}
##
##
##b = frozenset(a)
##
##print(type(b))
##




##li = [(1,2),(2,3),(1,3)]
##
##
##s = set(li)
##
##print(s)




li =set{,}


li1 = 5

for i in range(li1):
    a = int(input("enter"))
    li.add(a)


print(li)















































##fact = 1
##
##
##num = 5
##
##
##for i in range(1,num+1):
##    fact = fact * i
##
##print("the factorial is a:-",fact)


##def prime_number(n):
##    num = n
##    factor = 0
##
##    for i in range(2,num-1,1):
##        if num % 2==0:
##            factor+=1
##
##    if factor==0:
##        print("prime number:-",num)
##    else:
##        print("non  prime number:--",num)
##
##for i in range(1,101,1):
##    prime_number(i)



##num = 153
##
##cube = 0
##
##no = num
##
##for i in range(1,num+1,1):
##    a = no % 10
##    cube = cube + a ** a
##    no = no // 10
##
##if cube == no:
##    print("amstrong number")
##else:
##    print("not a amstrong number")
##


##class A:
##    name = "roshan"
##
##    def st():
##        print("name is a:=",A.name)
##
##    def no_st(self):
##        print("the name is a:-",self.name)
##        print("the address is a:-",self.address)
##
##a = A()
##a.address = "kusumba"
##a.no_st()
##
##A.st()

##help("keywords")


##help("modules")


##name  = "roshan"
##
##
##print(f"the name is a:=={name}")
##



##
##for i in range(5,0,-1):
##    print(i ,end="")



##for i in range(1,11,1):
##    print(i,"the square of the number 1 to 10-----",i**2,"the cube of the number is a:-----",i**3,"addition is a:--",i**2 + i**3)


##for i in range(1,5,1):
##    for j in range(1,4,1):
##        print("*\t" * j)
####        print("\t")

    
##    for i in range(1,5,1):
##        for j in range(1,5,1):
##            print("*" * j)
##        print("\t")
    
    

##for i in range(5,0,-1):
##    print("*" * i)


##def simple(p,r,t):
##    a = (p*r*t)/100
##    print("simple interset is a:--",a)
##
##pp = int(input("enter the principal amount"))
##
##rr = int(input("enter the rate of the interest"))
##
##dd = int(input("enter the time"))
##
##simple(pp,rr,dd)

        

##class A:
##    
##    def st(self,p,r,t):
##        d = (p*r*t)/100
##        print("the simple interest is a:=",d)
##
##a = A()
##a.st(100,20,2)




##num = int(input("enter the ffirst number"))
##
##num2 = int(input("enter the second number"))
##
##
##if num>0 and num2>0:
##    print("there are in first qurant")
##elif num<0 and num2>0:
##    print("this is in seocnd quarant")
##elif num<0 and num2<0:
##    print("this is in third  qurants")
##else:
##    print("this in a four qurants")
##    
##


print("1.qurants-1\n2.qurants-2\n3.qurants-3\n4.qurants-4")


choice = int(input("enter your choice"))


num = int(input("enter the number"))

num2 = int(input("enter the number"))


match(choice):
    case 1:
        if num>0 and num2>0:
            print("the number in first qurants")
        else:
            print("not in first qurants")
        
    case 2:
        if num<0 and num2>0:
            print("the number in second qurants")
        else:
            print("not in second qurants")
            
    case 3:
        if num<0 and num2<0:
            print("the number in third qurants")
        else:
            print("the number is not third qurants")
    case 4:
        if num>0 and num2<0:
            print("the number in fourth qurants")
        else:
            print("the number is not in fourth qurants")
            
    case _:
        print("invalid choice")






































































##
##class A:
##
##
##    def display(self):
##        print("hellow")
##
##
##    def display1():
##        print("hellow")
##
##a = A()
##
##a.display()
##
##A.display1()





##
##class A:
##
##
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##
##
##    def add(self):
##        print(self.a+self.b)
##
##    def sub(self):
##        print(self.a-self.b)
##
##    def mul(self):
##        print(self.a*self.b)
##
##    def salary(self,salary1):
##        b = salary1 + (salary1*10)/100
##        print("total salary is a",b)
##
##    def discount(self,price):
##        d = price-(price*10)/100
##        print("total discount of this sells is a",d)
##
##
##a = A(20,30)
##
##a.add()
##
##a.sub()
##
##a.mul()
##
##a.salary(100)
##
##a.discount(100)


##for i in range(0,5,1):
##    print(" "*(4-1),"*"*((2-i)-1)) 

##for i in range(0,5,1):
####    for j in range(0,5,1):
####        if i==0 or i==4 or j==0 or j==4:
##            print("*",end=" | ")
##        elif i==2 and j==2:
##            print("*",end=" | ")
##        elif i==1 and j==3:
##            print("*",end=" | ")
##        elif i==3 and j==1:
##            print("*",end=" | ")
##        elif i==1 and j==1:
##            print("*",end=" | ")
##        elif i==3 and j==3:
##            print("*",end=" | ")
##
##
##        else:
##            print(" ",end="  ")
##
##
##    print()




##i = 0
##
##while (i<10):
##    print("hellow")
##    i+=1




##
##
##num = int(input("enter the number"))
##
##
##rev = 0
##
##no = num
##
##
##while(no>0):
##    a = no%10
##    rev = rev * 10 + a
##    no = no//10
##
##if rev==num:
##    print("palindrome number")
##
##else:
##    print("not palinfrome number")

##
##
##num = 154
##
##cube = 0
##
##no = num
##no = no+1
##while (no>0):
##    a = no %10
##    cube = cube + a**a
##    no = no //10
##
##if cube==no:
##    print("amstrong number")
##else:
##    print("not amstrong number")
##print("hii")
##




##
##def prime_number(n):
##
##    num = n
##
##    factor = 0
##
##    for i in range(2,num-1,1):
##        if num%i==0:
##            factor+=1
##
##
##    if factor==0:
##        print("the number is a prime number================================",num)
##    else:
##        print("not prime number-----------------------------",num)
##
##
##
##for i in range(1,50,1):
##    prime_number(i)


##
##fact = 1
##n = 5
##for i in range(1,n+1,1):
##    fact = fact * i
##
##
##print(fact)






##st = "roshan vijay pardeshi"
##
##count=0
##for i in range(0,len(st),1):
####    print(st[i],end=" ")
##    count+=1
##
##
##print(count)


##st = "roshan vijay pardeshi"
##
##for i in range(len(st)-1,-1,-1):
##    print(st[i])

##
##st = "roshan pardeshi"
##st = st.split()
##st1 = ""
##count = 0
##
##for i in range(0,len(st),1):
##    if len(st[i])>len(st1):
##        count+=1
##        
##
##print(count)

##
##st = "aaabbccvrreeereee"
##
##for i in range(0,len(st),1):
##    count = st.count(st[i])
##
##    if count==1:
##        print(st[i])
##




##
##st = "python@12$3%^"
##
##
##for i in range(0,len(st),1):
##    if st[i].isalpha():
##        pass
##    elif st[i].isdigit():
##        pass
##    else:
##        print(st[i],end="")
##


##st = "python@123"
##
##print(st.upper())
##
##print(st.lower())
##
##print(st.capitalize())
##
##print(st.startswith("p"))
##
##print(st.endswith("n"))
##
##print(len(st))
##
##print(st.isalpha())
##
##print(st.isalnum())






##
##
##
##
##
##
##balance = 10000
##
##pin = int(input("enter your pin"))
##
##if pin==1961:
##    print("1.deposit \n2.withdraw \n3.check balance \n4.Exit")
##    while (True):
##        choice = int(input("enter your choice"))
##        match(choice):
##            case 1:
##                deposit_amount = int(input("enter the deposit amount"))
##                balance+=deposit_amount
##                print(balance)
##            case 2:
##                withdraw_amount = int(input("enter the withdraw amount"))
##                balance-=withdraw_amount
##                print(balance)
##            case 3:
##                print("your avaliable balance is a:-",balance)
##            case 4:
##                print("thankuuu.. ladle")
##                break
##
##            case _:
##                print("invalid choice")

print





























































    








































































































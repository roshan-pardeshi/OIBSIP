##
##
##a=5
##b=4
##print(a+b)
##print(a-b)
##print(a*b)
##print(a**b)
##print(a//b)
##print(a/b)
##
##print("variables")
##
##
##print(5+4)
##print(5-4)
##print(4*4)
##print(5//4)
##print(5**4)
##print(5//4)
##print("roshan pardeshi")
##
##print(8*5+6/2)
##
##
##print(8**5+2//2)











##
##from day13pra import *
##
##
##
##
####
####a = add(24,56)
####
####a()
##
##
##s = cei(20)
##s()


##
##class A:
##
##    def __init__(self,first_name,last_name):
##        self.first_name=first_name
##        self.last_name=last_name
##
##
##    def __str__(self):
##
##        return f"the first name is a:-{self.first_name} and last name is a {self.last_name} "
##
##
##a = A("roshan","pardeshi")
##
##print(a)


##class A:
##
##
##    def __init__(self,roll_no,name):
##        self.roll_no = roll_no
##        self.name = name
##
####    def __str__(self):
####
####        return f"the roll_no is a:--{self.roll_no} and name is a {name}"
##
##
##a = A(1,"roshan")
##
##
##b = A(2,"sonu")
##
##li = [a,b]
##
##for i in li:
##    print(i.roll_no)
##    
##    print(i.name)






##class A:
##
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##
##
##    def __str__(self):
##        return f"{self.a+self.b} and sunstraction is a{self.a-self.b}"
##
##
##a = A(20,30)
##
##print(a)
##
##for i in range(1,11,1):
##    print(f"\t{i*2}  \t{i**i} \t " )


##
##for i in range(5,0,-1):
##    print(i*i)


##for i in range(5,0,-1):
##    print(" " * (5-i),"*"*5)
##


##for i in range(0,5,1):
##    print(" "*(4-i),"*"*((2*i)-1))
##
##for i in range(4,0,-1):
##    print(" "*(5-i),"*"*((2*i)-3))
##


##class bank_account:
##
##    def __init__(self,account_number,holder_name,balance):
##        self.account_number=account_number
##        self.holder_name=holder_name
##        self.balance=balance
##
##
##    def __str__(self):
##
##        return f"the account_number is a {self.account_number} the holder_name is a {self.holder_name} the balance is a:{self.balance}"
##
##
##a = bank_account(3240,"roshan pardeshi",1000)
##
##b = bank_account(4050,"manish borse",2000)
##
##print(a)
##
##print(b)

##
##a = 20
##
##b = 30
##
##temp=0
##
##temp = a
##
##a = b
##
##b=temp
##
##print("A after swaping",a)
##
##print("B after swaping",b)



##a = 20
##
##b = 30
##
##
##a = a+b
##b = a-b
##a = a-b
##
##print(a)
##
##print(b)




##num = int(input("enter the number"))


##a = 0
##b = 1
##
##
##for i in range(1,num+1,1):
##    print(a)
##    c = a+b
##    a=b
##    b=c
##    



##
##num = int(input("enter the number"))
##
##
##factor = 0
##
##for i in range(2,num-1,1):
##    if num%2==0:
##        factor+=1
##
##
##if factor==0:
##    print("the number is prime")
##else:
##    print("not prime number")




##def palindrome(n):
##        num = n
##
##        rev = 0
##
##        no = num
##
##
##        while no>0:
##            a = no%10
##            rev = rev * 10 + a
##
##            no=no//10
##
##
##            if rev == num:
##                print("palindrome number-------",num)
####else:
####    print("not palindrome")
##
##for i in range(1,500,1):
##    palindrome(i)
    





##st = "aa bbb cccc"
##
##size = 0
##
##index = 0
##
##st =st.split()
##
##for i in range(0,len(st),1):
##    if len(st[i])>size:
##        size = len(st[i])
##        index=i
##
##print(st[index])
    

##st = "rrrsssaaassddfff"
##
##
##new = ''
##
##
##for i in range(0,len(st),1):
##    if st[i] in new:
##        pass
##    else:
##        new+=st[i]
##
##print(new)


##num = 9
##
##
##neon = num*num
##v = 0
##for i in str(neon):
##    v +=int(i)
##
##if v == num:
##    print("neon number",v)




num = "1023"

for i in num:
   if num[0]!="0":
       if int(i)==0:
           print("duck number")



































































































































































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




##num = "1023"
##
##for i in num:
##   if num[0]!="0":
##       if int(i)==0:
##           print("duck number")
##








































##li = [1,2,3,4,5,6]
##
##
##li.append("roshan")
##
##print(li)
##
##
##li.remove(4)
##
##print(li)
##
##li.pop()
##
##print(li)
##
##
##li.insert(1,3)
##
##print(li)
##
##
##print(li.index(3,0,3))
##
##
##print(sorted(li))
##

##print(min(li))
##
##print(max(li))
##
##
##st = "roshan"
##
##print(st.upper())
##
##print(st.capitalize())
##
##print(st.lower())
##
##print(st.count("a"))
##
##print(st.startswith("a"))
##
##print(st.endswith("n"))
##
##print(st)

##
##
##class A:
##
##   def __init__(self,name,roll_no):
##      self.name = name
##      self.roll_no = roll_no
##
##
##   def __str__(self):
##      return f"the name is a {self.name} and roll_number is a {self.roll_no}"
##
##
##a = A("roshan",1)
##
##print(a)
      




##class A:
##
##   def sonu(self):
##      print("hii")
##
##
##   def roshan():
##      print("the a static are run")
##
##
##
##a = A()
##a.sonu()
##
##A.roshan()

##
##class A:
##
##
##   def __init__(self,name,age):
##      self.name = name
##      self.age = age
##
##   def __str__(self):
##      return f"the name {self.name} age {self.age}"

##a= A("roshan",20)
##
##b = A("sonu",23)
##
##c = A("manish",22)
##
##li = [a,b,c]
##
##for i in li:
##   print(i)






##st = "roshan"
##
##
##for i in range(len(st)-1,-1,-1):
##   if st[i]=="n":
##      print(st[i])


##st = 12
##
##
##st = str(st)
##
##
##if st == st[::-1]:
##   print("palindrome")
##else:
##   print("not palinfrome")

##st = "123"
##
##sum=0
##for i in st:
##   sum+=int(i)
##
##print(sum)



##st = "roshan pardeshi"
##
##
##st =st.split()
##
##
##print(st[::-1])

##for i in range(len(st)-1,-1,-1):
##   print(st[i])
##


##li = [[1,2,3],
##      [4,5,6],
##      [7,8,9]
##      ]
##
##sum=0
##for i in range(0,len(li),1):
##   for j in range(0,len(li[i]),1):
##      if i+j==2:
##         sum+=li[i][j]
##         print(li[i][j])
##
##print(sum)
##


tu = ((1,2,3),(4,5,6),(7,8,9))

for i in range(0,len(tu),1):
   for j in range(0,len(tu[i]),1):
      if i==j:
         print(tu[i][j])






























##a = 0
##b = 1
##
##
##for i in range(51,101,1):
##   if a>50 and a<=100:
##      print(a)
##   c=a+b
##   a=b
##   b=c




##li = [0,1,0,2,3,4,1]
##li1=[]
####print(len(li))
##for i in range(0,len(li),1):
##   if li[i]!=0:
##      li1.append(li[i])
##
####print(li1.append(0))
##      
##if len(li)!=len(li1):
##   for i in range(0,100):
##      if len(li)==len(li1):
##         break
##      else:
##         li1.append(0)
##
##
##print(li1)

##num= 151
##
##b = str(num)
##if b==b[::-1]:
##   print("palindrome")
##else:
##   print("not")
##







































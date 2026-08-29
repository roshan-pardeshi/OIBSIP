



##print("hello")


##class A:
##
##
##    def __init__(self,rollno,name,address):
##        self.rollno = rollno
##        self.name = name
##        self.address = address
##
##
##
##    def __str__(self):
##
##        return f"the rollno:-{self.rollno} the name:-{self.name} the address:-{self.address}"
##
##
####a = A(1,"roshan","pune")
####
####b = A(2,"manish","pune")
####
####c = A(3,"tushar","pune")
####
####li = [a,b,c]
####
####
####for i in li:
####    print(i)
##
##n = int(input("enter how many you add:-"))
##
##li=[]
##
##for i in range(n):
##    a = A(int(input("enter rollno:-")),input("enter name:-"),input("enter the address:-"))
##    li.append(a)
##
##for i in li:
##    print(i)



##
##def prime(n):
##
##    num = n
##
##    factor=0
##
##    for i in range(2,num-1,1):
##        if num%i==0:
##            factor+=1
##            
##
##
##    if factor==0:
##        print("prime number:----",num)
##    else:
##        print("not prime number")
##
##
####prime(40)
##
##for i in range(1,101,1):
##    prime(i)
##
##
##


##def fibo(n):
##a = 0
##b = 1
####
####
##num=55
##
##for i in range(1,num+1,1):
##    if a>50 and a<100:
##        print(a)
##    c = a + b
##    a=b
##    b=c



##for i in range(0,101,1):
##    fibo(i)


##
##
##num = 122
##
##num = str(num)
##
##if num==num[::-1]:
##    print("the string is palindrome")
##else:
##    print("NOT Palindrome")



##def sonu():
##
##    def monu():
##        print("hello")
##
##
##    def golu():
##        print("heyy")
##
##
##    return monu,golu
##
##
##a,b=sonu()
##
##a()
##b()



##for i in range(1,6,1):
##    print(" " *(5-i),"*"*((2*i)-1))
##
##
##for i in range(5,1,-1):
##    print(" "*(6-i),"*"*((2*i)-3))






##li = [1,2,3,4,5,6]
##
##
##li.append(2)
##
##print(li)
##
##li.insert(2,33)
##
##print(li)
##
##li.extend([1,2,3,4,5])
##
##print(li)



##f = ["apple","carry","kiwi","banana"]
##
##
##f.pop()
##
##print(f)
##
##
##f.remove("apple")
##
##print(f)
##
##
##f.clear()
##
##print(f)




##
##li = [1,2,3,4,7,2,1,4,5,2]
##
##
##print(li.index(7,2,6))
##
##
##print(li.count(2))


##
##li = [12,54,32,8,56,17]
##
####print(sorted(li))
##
####li.sort(reverse=True)
####
####print(li)
##
##li.reverse()
##
##print(li)


##color = ["red","green","blue","yellow"]
####a=[]
##a.copy(color)
##
##print(a)


##sum = 0
##
##li = [[1,2,3],
##      [4,5,6],
##      [7,8,9]
##      ]
##print(li)
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i+j==2:
##            sum+=li[i][j]
##

##print(sum)
3



##
##
##
##st = "roshan pardeshi"
##st = st.split()

##for i in range(len(st)-1,-1,-1):
##    print(st[i][::-1])

##
##st = "aabbccdeeesssaeaasww"
##
##factor=0
##for i in range(0,len(st),1):
##    count = st.count(st[i])
##    
##    if count==2:
##        factor+=1
##        if factor==2:
##            
##            print(st[i])











































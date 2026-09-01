##
####
####d1 = {1:"roshan",2:"sonu"}
####
####print(d1)
####
####print(type(d1))
####
####
####
####d1.pop(2)
####
####print(d1)
####
####
####d2 = {1:10,2:20,3:30,4:40}
##
##
####for i in d2:
####    print(i)
##
####print(d2.keys())
####
####print(d2.values())
####
####
####d2.popitem()
####
####print(d2)
####
####
####print(max(d2))
####
####print(min(d2))
##
######
####x = d2.keys()
####
####y = d2.values()
##
####print(x)
####
####print(y)
####
####d2.update({1:23,12:23,44:55})
####
####print(d2)
##
##d3 = {}
####
####for i in range(len(d2)):
####    d3[i] = d2[i]
####
####
####print(d2)
##
##
####d3[1] = 100
####
####print(d3)
####
####
####d2= list(d2)
####
####print(d2)
####print(type(d2))
####
####d2 = tuple(d2)
####
####print(type(d2))
##
##
####
####d4 = {1:10,2:20,3:30,4:40}
######
######for i in d4.values():
######    print([i])
####
####d5 = {}
####
####d = d4.keys()
####c = d4.values()
####
####
####for i in range(len(d4)):
####    d5[d4[i]] = d4[i]
####
####print(d5)
##
##
####
##stu = {"amit":86,"ravi":99 ,"roshan":34,"krishna":23}
####
####
######print(stu["roshan"])
####
####print(stu["amit"])
####
####print(stu[34])
##
####stu.update({"sonu":32})
####print(stu)
##
####stu["ravi"]=100
####
####print(stu)
####
####stu.pop("krishna")
####
####print(stu)
##
##
####stu = stu.keys()
####
####for i in stu:
####    if i=="roshan":
####       print("peresent in dict")
##
####st = {1:10,2:20,3:30,4:40}
####
####st = st.keys()
####
####for i in st:
####    print(st)
##
######
####st = {1:20,2:30,3:30}
######
######for i in st.values():
######    print(i)
####
####
####for i in range(len(st)):
####    print(st)
####
####st = {"roshan":99,"ravi":10,"neha":20,"krishna":90}
####
####st = st.values()
####
####print(max(st))
##
##
##
##
##
####d1 = {"amit":85,"ravi":72,"sita":91,"vasudha":99}
####
####
####d1.update({"ankit":44})
####
####print(d1)
####
####
####d1["ravi"]=80
####
####print(d1)
####
####
####d1.pop("vasudha")
####
####print(d1)
####
####for i in d1.keys():
####    if i=="sit":
####        print("yes hi is present")
####        break
##
####
####d1 = {1:"roshan",2:"sita",3:"vasdhua",4:"mohit"}
####
####
####print(d1.keys())
####
####print(d1.values())
####
####
####for i in range(len(d1)):
####    print(d1)
####    break
##
##
##d1 = {"roshan":99,"vasudha":100,"manish":888,"mohit":99.9}
##
##
####max1 = d1.values()
####
####print(max1)
##sum1=0
##avg = 0
##count=0
##for i in d1.values():
##    sum1+=i
##    count+=1
##
##
##print(sum1)
##print(count)
##avg = sum1/count
##print(avg)
##
##
##
####print(avg)
####
####
####
####d = 99+100+888+99.9/4
####
####print(d)
####



##d1 = {"a":1,"b":2}
##
##d2 = {"c":3,"d":4}
##
##
##
##d1[3]=d2
##
##print(d1)
##



##
##d1 = {1:1,2:4,3:9}
##
####print(d1)
####
####
####d1 = list(d1)
####
####print(d1[1])
##
##d2 = {}
##
##
##for i in range(len(d1)):
##    d2[i]=d1[i]
##
##
##print(d2)






##stu ={
##    "101":{"name":"amit","age":22,"marks":99},
##    "102":{"name":"roshan","age":32,"marks":90}
##    }
##
##print(stu["102"])
##
##print(stu["101"])


##a = {1:"roshan",2:"sonu",3:"rohit"}
##
##b = {1:"manish",2:"mohit",3:"sneha"}
##
##a = b[1]
##
##print(a)

##li = [1,2,3,4,5]
##
##print(li.count(1))
##
##print(li.index(2,0,2))
##
##li.append(20)
##
##print(li)
##
##li.pop()
##
##print(li)
##
##li.remove(2)
##
##print(li)

##li1 = [12,11,22,21,[1,2,2,3],1,2,3]
##
####print(sorted(li1))
##
####print(li1[4][2])
##
##for i in range(0,len(li1),1):
##    print(li1[i])


##tu = (1,(2,2),(3,3),3,4,5,5)

##print(tu.count(1))
##
##print(tu.index(2,0,1))

##t1 = {1,2,3,[1,2,3,3],1}
##
##x = list(t1)
##
####x = t1[3]
##
##print(x)


##t = [1,2,3,4,[1,2,3,4],1]
##
##
##x = t[4]
##
##x.extend([1,2,3])
##
##t[4]=x
##
##print(t)

##t1 = (1,2,3,4,5,6,[1,2,3],1)
##
##t = t1[6]
##
##t.append(10)
##
##print(t)
##
##
####t1[6] = t
##
##print(t1)










##def prime(n):
##    num = n
##
##    factor= 0
##
##    for i in range(2,num-1,1):
##        if num%i==0:
##            factor+=1
##
##
##    if factor==0:
##        print("prime number:---",num)
##
####        else:
####            print("not prime number")
####
##
##for i in range(101):
##    prime(i)







##num = 211
##
##
##num = str(num)
##
##if num==num[::-1]:
##    print("palindrome number")
##else:
##    print("not palindrome number")

##num = 9
##
##num1 = num*num
##
##num1 = str(num1)
##sum1=0
##for i in num1:
##    sum1+=int(i)
##
##
##
##
##if num == sum1:
##    print("is neon number")
##
##else:
##    print("not a neon number")





##class A:
##
##    def __init__(self,name,address,pincode,city):
##        self.name = name
##        self.address = address
##        self.pincode = pincode
##        self.city = city
##
##
##    def __str__(self):
##
##        return f"the name is a:--{self.name} address is a:--{self.address} pincode is a:--{self.pincode} the city is a{self.city}"
##
##
##
##print("1.Add the name \n2.remove the record")
##
##while True:
##    choice = int(input("enter your choice"))
##    match(choice):
##        case 1:
##            n = int(input("enter the number how many student you add:--"))
##
##            li=[]
##            for i in range(n):
##                a = A(input("enter the name:--"),input("enter the address:--"),int(input("enter the pincode:--")),input("enter the city name:--"))
##                li.append(a)
##
##
##            for i in li:
##                print(i)
##        case 2:
##            b = input("enter the name for remove the a student")
##            li.pop()
##            
##            for i in li:
##                print(i)
##
##        case 3:
##            break
##
##        case _:
##            print("invalid choice")
##
##        
##
##for i in li:
##    print(i)







































































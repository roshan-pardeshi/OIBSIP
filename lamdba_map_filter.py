


##d = lambda x:x**x
##
##print(d(5))



##li = [1,2,3,4,5,6,7]
##
##
##res = list(map(lambda x:x*x,li))
##
##print(res)

##tu = (


##li = [1,2,3,4,5]
##
##
##res = list(map(lambda x:x**2,li))
##
##print(res)

##res  = list(filter(lambda x:x%2==0,li))
##
##print(res)

##
##li1 = ["apple","banana","kiwi","pear"]
##
##
##res = list(filter(lambda x:len(x)>4,li1))
##
##print(res)

##
##li = [0,20,37,100]
##
##res = list(map(lambda x: x*(9/5)+32,li))
##
##print(res)
##

##li = [12,15,20,22,29,30]
##
##
##res = list(filter(lambda x:x%5==0 and x%10==0,li))
##
##
##print(res)

           
##li = ["python","java","c language"]
##
##
##res = list(map(lambda x:len(x),li))
##
##print(res)
##
##tu = (10,20,30,40,50)
##
##res = tuple(map(lambda x:str(x),tu))
##
##print(res)


##
##li = (3,9,12,18,21,25)
##
##
##res = tuple(filter(lambda x:x%3==0,li))
##
##print(res)
##



##li = (1,-2,-3,1,2,4)
##
##
##res = tuple(map(lambda x:x*(-1) if x<0 else x,li))
##
##print(res)
##
##
##
##t1 = (23,33,1,2,4,5,6)
##
##t1 = list(t1)
##
##res = list(filter(lambda x:x%3==1,t1))
##
##print(res)

##
##
##st =  "datascience"
##
##
##d1 = {}
##
##for i in range(len(st)):
##    val = st.count(st[i])
##    d1[st[i]]=val
##
##print(d1.keys())
##
##print(d1.values())
##
##print(d1.items())
##
##d1.update({33:"ct"})
##
##print(d1.pop("a"))
##
##print(d1.popitem())





##li = {1,2,3,4,5,6,7,8,9,10}
##
##
##res = set(map(lambda x:x*2,li))
##
##print(res)


##li = [1,4,9,16,25]
##
##res = set(map(lambda x:x**0.5,li))
##
##print(res)


##li = {100,200,300,400,500,600}
##
##res = set(filter(lambda x:x>300,li))
##
##print(res)

##li = {"a":2,"b":3,"c":12,"v":90,"t":34}
##
##res = dict(filter(lambda x:x[1]>10,li.items()))
##
##print(res)


##li = {"x":1,"y":2,"z":3}
##
##res = dict(map(lambda x:(x[0],x[1]**3),li.items()))
##
##
##
##print(res)

##li = {"apple":1,"banana":2,"carry":3,"kiwi":4}
##
##res = dict(map(lambda x:(x[0].upper(),x[1]),li.items()))
##
##
##
##print(res)

##li = {"ravi":99.9,"roshan":55,"swarup":95,"manish":85}
##
##res = dict(filter(lambda x:x[1]>90,li.items()))
##
##print(res)


##li = {"pen":100,"book":25,"pencil":5}
##
##res = dict(map(lambda x:(x[0],x[1]-(x[1]*10)/100),li.items()))
##
##print(res)
##

##li = (1,2,33,34,32,93,54,343)
##
##
##res = tuple(filter(lambda x:x%10==3,li))
##
##print(res)



##
##st = "abcdessrfdfs"
##
##count = 0
##
##for i in range(len(st)):
##    count+=1
##
##print(count)


##a = 0
##
##b = 1
##
##num = 100
##
##
##for i in range(1,num+1,1):
##    if a>50 and a<100:
##        print(a)
##    c = a+b
##    a = b
##    b = c


def factorial(n):
    fact = 1
    num=n
    for i in  range(1,num+1,1):
        fact=fact*i

    return fact


sum1= 0

num = 145

for i in str(num):
    sum1+=factorial(int(i))


if sum1==num:
    print("strong number")

else:
    print("not a strong number")
    











































##print("hello")

##
##a = "1233"
##
##
##b = int(a)
##
##
##print(type(b))


##name = "roshan"
##
##age = 34
##
##address = "kasba peth pune"
##
##
##print("name is a {}".format(name))
##
##print(f"name is a {name} age is a {age} address is a {address}")



##help("math")


##def a():
##    print("addition")
##
##a()




##def prime_number(n):
##    num=n
##    factor = 0
##
##    for i in range(2,num-1,1):
##        if num % i ==0:
##            factor+=1
##
##    if factor==0:
##        print("the number is a prime :-----------------",num)
##    else:
##        print("the number is a not a prime number :---------------",num)
##
##
##for i in range(1,101,1):
##    prime_number(i)
    



##a = 0
##b = 1
##
##num = int(input("enter the number"))
##
##
##for i in range(1,num+1,1):
##    print(a)
##    c = a+b
##    a=b
##    b=c
##



##num=5
##fact = 1
##
##for i in range(1,num+1,1):
##    fact *=i
##
##
##print("factorial is a:--",fact)




##num = 153
##
##
##cube = 0
##
##
##no = num
##
##
##for i in range(1,no+1,1):
##    a = no % 10
##    cube = cube + a**3
##    no = no //10
##    
##
##
##if cube==num:
##    print("amsteong number")
##else:
##    print("not a amstrong number")

##




num = 212

rev = 0

no = num

while no>0:
    a = no%10
    rev = rev*10+a
##    print(rev)
    no = no // 10


if rev == num:
    print("palindrome number")
else:
    print("not palindrome number")
    


























































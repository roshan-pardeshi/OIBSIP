


##i = 1
##while i<=10:
##    print(i)
##    i+=1


##i = 10
##
##while i>=1:
##    print(i)
##    i-=1


##i = 2
##
##while i <=20:
##    print(i)
##    i+=2


##i = 1
##while i <=20:
##    if i % 2==0:
##        print("even number",i)
##    i+=1


##def odd(n):
##    if n % 2!=0:
##        print("the number is a odd",n)
##
##i=1
##while i<=20:
##    odd(i)
##    i+=1


##i = 65
##
##while i<=90:
##    print(chr(i))
##    i+=1
##




##i = 97
##while i <= 122:
##    print(chr(i))
##    i+=1


##for i in range(6,1,-1):
##    print("*" * i)


##
##while (True):
##    print("1.deposit\n2.withdraw\n3.check balance\n4.exit")
##    choice = int(input("enter your choice "))
##
##    match(choice):
##        case 1:
##            print("deposit successfully")
##
##        case 2:
##            print("withdraw successfully")
##        case 3:
##            print("your balance is a")
##
##        case 4:
##            break
##
##        case _:
##            print("invalid choice")



##for i in range(1,11,1):
##    print(i*5)


##for i in range(1,11,1):
##    if i % 2==0:
##        print(i)

##
##name = "python"
##
##for i in range(0,len(name),1):
##    print(name[i])

##result = 0
##for i in range(1,11,1):
##    result+=i
##
##print(result)
##
##for i in range(1,11,1):
##    print(i**3)


##for i in range(1,11,1):
##    print("square is a",i**2)

##name = "programming"
##
##count = 0
##
##for i in range(1,len(name),1):
##    if name[i] =='a' or name[i] == 'e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
##        count+=1
##
##print(count)
##        

##count =0
##for i in range(1,51,1):
##    if i % 2!=0:
##        count+=1
##
##print(count)


##name = "python is very powerful"
##
##for i in range(0,len(name),1):
##    print(name[i])

##
##fact = 1
##num =5
##for i  in range(1,num+1,1):
##    fact=fact*i
##
##print("factorial is a:-",fact)

##a = 0
##b = 1
##num = 10
##for i in range(1,num+1,1):
##    print(a)
##    c = a+b
##    a = b
##    b = c
##


##num = 9423664345
##count = 0
##i = 1
##while num>0:
####    d = num%10
##    num = num//10
##    count+=1
##
##print(count)






##num = 1234567891
##
##i=1
##a = 0
##sum1 = 0
##while num>0:
##    d = num %10
##    num = num // 10
####    a+=num
##    sum1+=d
##
##    
##
##print(sum1)

def prime_number(n):
    num = n
    factor = 0

    i = 2
    while num-1:
        if num%i==0:
            factor+=1
	

        if factor==0:
            print("prime number",num)
        else:
            print("not a prime number",num)
            
        i+=1
            

for i in range(1,100):
    prime_number(i)


##def number(n):
##    num = n
##    factor = 0
##    
##    i = 2
##    while num-1:
##        if num % i ==0:
##            factor +=1
##   
##
##
##    if factor == 0:
##        print("prime number")
##    else:
##        print("not prime number")
##
##    i+=1
##
##number(3)


















































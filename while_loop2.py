



##def prime_number(n):
##    num = n
##    
##    factor = 0
##    i = 2
##    while(num-1):
##        if num % i ==0:
##            factor +=1
##
##        if factor==0:
##            print("the number is a prime number")
##            else:
##            print("not a prime number")

##prime_number(3)
  



##num = int(input("enter the number for checking the prime or not "))
##
##i = 2
##factor = 0
##while i<=num-1:
##    if num % 2==0:
##        factor +=1
##
##    i+=1
##  
##if factor ==0:
##    print(":********:prime number:******:",num)
##else:
##    print("not a prime number")


##num = 5
##
##fact = 1
##
##i=1
##while i<=num:
##    fact = fact * i
##    i = i +1
##
##print("factorial is a:-",fact)
##    
##





num = 153

cube = 0

no = num

i = 1
while i<=num:
    a =no%10
    cube = cube + a**3
    no = no // 10
    i+=1


if cube == num:
    print("the number is amstrong number")
else:
    print("not a amstrong number")









































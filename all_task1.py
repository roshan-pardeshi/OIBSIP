

##name = "python"
##count = 0
##
##for i in range(0,len(name),1):
##    count+=1
##
##print(count)


##name = "roshan pardeshi"


##print(name[::-1])


##if name == name[::-1]:
##    print("palindrome")
##else:
##    print("not palindrome")


##name = "roshan pradeshi"
##
##count=0
##for i in range(1,len(name),1):
##    if name[i]=="a" or name[i]=="i":
##        count +=1
##
##
##print(count)

##
##name = "roshan"
##
##
##print(name.upper())
##print(name.lower())
####print(name.capitlize())
##
##print(name.startswith("a"))
##print(name.endswith("n"))
##print(name.isdigit())
##print(name.isalpha())
##print


##name = "roshan vijay pardeshi"



##print(name.replace(" ","-"))



##name = "roshan vijay pardeshi"

##
##for i in range(0,len(name),1):
##    if name[i]=="a" or name[i]=="e" or name[i]=="i" or name[i]=="o" or name[i]=="u":
        

##print(name)



##print(name.remove())



##for i in range(1,5,1):
##    print(" "*(1*i),"*"*((5*i)-5))



##for i in range(1,5,1):
##    for j in range(1,6,1):
##        if i==1 or i==4 or j==1 or j==5:
##            print("*",end="")
##        else:
##            print(" ",end="")
##
##    print()





##name = "roshan vijjay pardeshi"


##print(name.split(" "))

##a = name.split()
##
##count = 0
##
##for i in range(0,len(a),1):
##    count+=1
##
##print(count)
##

##name = "Roshan is a good boy"
##
##count=0
##count1=0
##count2 = 0
##
##a = name.split()
##for i in range(0,len(a),1):
##
##    if name[i].upper():
##        print(name[i])
##        count+=1
##    elif name[i]==lower():
##        count1+=1
##
##
##print("count=",count)
##print("count1",count2)
##        


name = "Roshan vijay pardeshi"


##for i in range(0,len(name),1):
####    if name[i].upper():


        

##for i in range(65,90+1,1
##    if 
##
##
##
##a = chr(i)
##for i in range(0,len(name),1):
##    if chr(i)>=65:
##        print(i)
##    else:
##        print("not")



##li = [[1,2,3],
##      [4,5,6],
##      [7,8,9]]
##sum=0
##
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i==j:
##            sum+=li[i][j]
##
##print(sum)

##sum=0
##
##tu = ((1,2,3),(4,5,6),(7,8,9))
##
##for i in range(0,len(tu),1):
##    for j in range(0,len(tu[i]),1):
##        if i==j:
##            sum+=tu[i][j]
##
##print(sum)


##st = "roshan"
##
##print(len(st))


##
##li = [1,2,3,4,4,5]
##
##li1=[]
##i=0
##for i in range(0,len(li),1):
##    if li[i] not in li1:
##        li1.append(li[i])
##
##print(li1)


def perfect_number(num):
    n = num

    count  = 0

    for i in range(1,n,1):
        if num%i==0:
            count+=i

    if count==num:
        print("perfect number",num)


for i in range(1,2000,1):
    perfect_number(i)
            









a = 0
b = 1
num=5
for i in range(1,num+1,1):
    print(a)
    c = a+b
    a=b
    b=c






















































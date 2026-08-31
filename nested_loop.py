##
##
##
####num = 123344
##
####digit=0
####
####while num>0:
####    digit+=num%10
####    num = num // 10
##
##
####print(digit)
##
####count = 0
####while num>0:
####    num = num //10
####    count +=1
####
####print(count)
##
##
####for i in range(1,11,1):
####    for j in range(1,11,1):
####        print(j*i)
##
##
##
####for i in range(10,1,-1):
####    for j in range(0,i):
####        print(j)
##
##
##
####for i in range(1,2,1):
####    for j in range(1,11,1):
####        print(j**2,"cube",j**3,j**2 + j**3)
##
##
##
####****
####***
####**
####*
####
####for i in range(4,0,-1):
####    for j in range(0,i):
####        print("*",end="")
####
####    print()
##    
##
####for i in range(1,6,1):
####    for j in range(1,i,1):
####        print("*\t*" ,end = "")
####
####    print()
##
##
##
##
####***********
####**********
####********
####*******
####******
####*****
####****
####***
####**
####*
##
##
####for i in range(11,1,-1):
####    for j in range(1,i):
####        print("*",end="")
####    print()
##
##
##
##
####for i in range(1,5,1):
####    for j in range(1,11,1):
####        print(j*i)
##
##
##
##
####for i in range(0,3,1):
####    for j in range(1,5,1):
####        print("*",end ="")
####    print()
##
##
####for i in range(0,3,1):
####    for j in range(0,6,1):
####        print(j,end="")
####    print()
##
##
##
####
####for i in range(3,0,-1):
####    for j in range(1,6):
####        print(j,end="")
####    print()
##
##
##
##
####for i in range(0,10,1):
####    for j in range(1,i,1):
####      print("*",end="")
####    print()
##
##          
####for i in range(0,10,1):
####    for j in range(1,i,1):
####        print(j,end="")
####    print()
##
##
####for i in range(65,90,1):
####    print(chr(i))
####
##
##
##
####for i in range(65,70,1):
####    for j in range(65,i):
####        print(chr(j),end="")
####    print()
##
####for i in range(1,4,1):
####    print("*" * i)
####
####for i in range(4,0,-1):
####    print("*" * i)
##        
##
####for i in range(0,4,1):
####    for j in range(1,5,1):
####        print()
####    print("*" * j,end="")
##
####*****
####*   *
####*   *
####*****
##
####for i in range(1,4,1):
####    for j in range(1,5,1):
####        print("*",end="") 
####
####for i in range(1,7,1):
####    if i==3:
####        if i==5:
####            print("*" * 5)
####
##
##
##
##
####for i in range(1,6,1):
####    for j in range(0,6,1):
####        if i==2 or i==3 or i==4:
####            continue
####        else:
####            print("*",end=" ")
####    print(" ")
####
##
####for i in range(1,5,1):
####    for j in range(1,6,1):
####        if j==1 or j==5:
####            if j ==2 or j==3:
####                continue
####            else:
####                print("%",end="")
####        else:
####            if i==1 or i==4:
####                print("*",end=" ")
####
####    print()
##
##
##
##
##
####for i in range(1,5,1):
####    for j in range(1,5,1):
####        if j==1 or j==4:
####            print("*",end="")
####        else:
####            if i==1 or i==4:
####                print("*",end="")
####            else:
####                print(end=" ")
####
####    print("  ")
####
##
####
####for i in range(1,6,1):
####    for j in range(0,4,1):
####        if  j==1 or  j==2 or j==3:
####            print("*",end="")
####        if i==1 or i==5:
####            print("*",end="")
####        else:
####        
####            print(" ",end="")
######            continue
####    print()
######
##
##for i in range(1,5,1):
##    for j in range(1,5,1):
##        if j==1 or j==4:
##            print(j,end="")
##        else:
##            if i==1 or i==4:
##                print(j,end="")
##            else:
##                print(end=" ")
##
##    print()
##
####print("\n")
####
####for i in range(1,5,1):
####    for j in range(1,5,1):
####        if j==1 or j==4:
####            print(i,end="")
####        else:
####            if i==1 or i==4:
####                print(i,end="")
####            else:
####                print(" ",end="")
####    print()
######
##
####
##
####a="*"
####for i in range(5,0,-1):
######    print(i)
####    for k in range(5,0,-1):
####        print(a,end="")
####    print()
####
####    for j in range(1,i+1,1):
####        print(" ",end=" ")
##
##             
##   
##
####a="*"
####for i in range(5,0,-1):
######    print(i)
####    for k in range(5,0,-1):
####        print(a,end=" ")
####    print()
####
####    for j in range(1,i+1,1):
####        print(" ",end="")
####
##
####  *
#### * *
####* * *
##
####c = 4
####
####for i in range(1,5,1):
####
####    
####    for k in range(1,i):
####        if i==1 or  k==1:
####            print("*",end=" ")
####            c-=1
####        elif i==3 or k==3:
####            print("*",end=" ")
####            
####        elif i==4 or k==4:
####            print("*",end=" ")
####            c-=1
####        else:
####            print("--")
####
####    print()
####    j=1
####    for j in range(c,j,-1):
####            print(" ",end="")
##            
##        
##            
####    print()
##
##
##
##
##
##
##
##
##
##
##
##
##
####    for k in range(1,i):
####        print("*",end="")
##
####for i in range(1,4,1):
####    for j in range(0,5,1):
####        print("*",end="")
####
####    if j==1 or j==2:
####        for k in range(1,i+1,1):
####            print("")
####            
####    print()
##
##
####****
####*  *
####*  *
####****
##
####for i in range(1,5,1):
####    for j in range(1,5,1):
####        if j==1 or j==4:
####            print("*",end="")
####        else:
####            if i==1 or i==4:
####                print("*",end="")
####            else:
####                print(" ",end="")
####
####    print()
##
##
##
##
####c = 4
####
####for i in range(1,7,1):
####
####    for k in range(1,i):
####        if i==1 or  k==1:
####            print("*",end=" ")
####            c-=1
####        elif i==3 or k==3:
####            print("*",end=" ")
####            
####        elif i==4 or k==4:
####            print("*",end=" ")
####            c-=1
####        else:
####            print("")
####
####    print()
####    j=1
####    for j in range(c,j,-1):
####            print(" ",end="")
####
######d = 4
####
####for e in range(5,0,-1):
####
####    
####    for w in range(1,i):
####        if e==1 or  w==1:
####            print("*",end=" ")
####            d-=1
####        elif e==3 or w==3:
####            print("*",end=" ")
####            
####        elif e==4 or w==4:
####            print("*",end=" ")
####            d-=1
####        else:
####            print("")
####
####    print()
####    t=1
####    for t in range(d,t,-1):
####            print(" ",end="")
##
####print("hi")
####                   * 
####                  * * 
####                 * * * 
####                * * * * 
####               * * * * * 
####              * * * * * * 
####             * * * * * * * 
####              * * * * * * 
####               * * * * * 
####                * * * * 
####                 * * * 
####                  * * 
####                   * 
##                    
##                    
##
##
##c = 20
##
##for i in range(1,8,1):
##
##    for k in range(1,i):
##        if i==1 or  k==1:
##            print("*",end=" ")
##            c-=1
##        elif i==3 or k==3:
##            print("*",end=" ")
##            
##        elif i==4 or k==4:
##            print("*",end=" ")
####            c-=1
##            
##        elif i==5 or k==5:
##            print("*",end=" ")
##            
##        elif i==6 or k==6:
##            print("*",end=" ")
##            
##        elif i==7 or k==7:
##            print("*",end=" ")
####            c-=1
##
##        elif i==8 or k==8:
##            print("*",end=" ")
####            c-=1
##
##        elif i==9 or k==9:
##            print("&",end=" ")
####            c-=1
####        
####        
####            
####        else:
####            print("")
####
####    print()
####    j=1
####    for j in range(c,j,-1):
####            print(" ",end="")
####
####
####d = 13
####
####for r in range(8,0,-1):
####
####    for t in range(1,r):
####        if r==1 or  t==1:
####            print("*",end=" ")
####            d+=1
####        elif r==2 or t==2:
####            print("*",end=" ")
####            
####        elif r==3 or t==3:
####            print("*",end=" ")
####            
####        elif r==4 or t==4:
####            print("*",end=" ")
######            c-=1
####            
####        elif r==5 or t==5:
####            print("*",end=" ")
####            
####        elif r==6 or t==6:
####            print("*",end=" ")
####
####        elif r==7 or t==7:
####            print("*",end=" ")
####            
####        elif r==8 or t==8:
####            print("*",end=" ")
######            c-=1
####
####        elif r==9 or t==9:
####            print("*",end=" ")
####            d-=1
####
####        elif r==9 or t==9:
####            print("*",end=" ")
######            c-=1
####        
####        
####            
####        else:
####            print(" ")
####
####    print()
####    j=0
######    d=1
####    for j in range(d,j,-1):
####            print(" ",end="")
##
##
##
##
##c = 20
##
##for i in range(1,8,1):
##
##    for k in range(1,i):
##        if i==1 or  k==1:
##            print("*",end=" ")
##            c-=1
##        elif i==3 or k==3:
##            print(" ",end=" ")
##            
##        elif i==4 or k==4:
##            print(" ",end=" ")
####            c-=1
##            
##        elif i==5 or k==5:
##            print(" ",end=" ")
##            
##        elif i==6 or k==6:
##            print(" ",end=" ")
##            
##        elif i==7 or k==7:
##            print(" ",end=" ")
####            c-=1
##
##        elif i==8 or k==8:
##            print(" ",end=" ")
####            c-=1
##
##        
##        
##        
##            
##        else:
##            print("")
##
##    print()
##    j=1
##    for j in range(c,j,-1):
##            print(" ",end="")
##
##
##d = 13
##
####for r in range(8,0,-1):
####
####    for t in range(1,r):
####        if r==1 or  t==1:
####            print("*",end=" ")
####            d+=1
####        elif r==2 or t==2:
####            print(" ",end=" ")
####            
####        elif r==3 or t==3:
####            print(" ",end=" ")
####            
####        elif r==4 or t==4:
####            print(" ",end=" ")
######            c-=1
####            
####        elif r==5 or t==5:
####            print(" ",end=" ")
####            
####        elif r==6 or t==6:
####            print(" ",end=" ")
####
####        elif r==7 or t==7:
####            print(" ",end=" ")
####            
####        
####            
####        else:
####            print(" ")
####
####    print()
####    j=0
######    d=1
####    for j in range(d,j,-1):
####            print(" ",end="")
####
####
####





##
##for i in range(0,5,1):
##    for j in range(0,5,1):
##        if i==0 or i==4 or j==0 or j==4:
##            print("*",end="")
##        else:
##            print(" ",end="")
##
##    print()



##for i in range(5,0,-1):
##    print(" "*i,"*"*5)


##for i in range(0,5,1):
##    print(" "*(5-i),"*"*((2*i)-1))
##

##for i in range(0,6,1):
##    for j in range(0,i,1):
##        print(i,end="")
##
##    print()

##li = [1,2,3,4,5]


##li.remove(4)
##
##print(li)
##
##li.append("roshan")
##
##print(li)
##
##li.extend([1,2,3,4,5])
##
##print(li)
##
##li.pop()
##
##print(li)
##
##li.remove(1)
##
##print(li)
##
##
####print(sorted(li))
##
##print(li.count(1))
##
##print(li.index(1,0,5))
##
##
##li.clear()
##
##print(li)



##print(type(li))
##
##a = tuple(li)
##
##b = set(li)
##
##print(type(a))
##
##print(type(b))


##li = [[1,2,3],[1,2,3],[1,2,3]]

##
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i==1 or j==4:
##            print(li[i][j])


##
##class A:
##
##    def __init__(self,name,address):
##        self.name = name
##        self.address = address
##
##
##    def __str__(self):
##
##        return f"the name is a {self.name} the address is a {self.address}"
##
##
##
##
##n = int(input("enter how many you add"))
##
##li = []
##
##for i in range(n):
##    a = A(input("enter the name"),input("address is a"))
##
##    li.append(a)
##
##
##for i in li:
##    print(i)


##li = {1,2,3,4,5,6,11,1,2,3,4}
##
##
##print(li)
##
##print(type(li))
##
##
##for i in li:
##    print(i)
##
##print(min(li))
##
##print(max(li))
##
##print(sorted(li))
##
##li = frozenset(li)
##
##print(type(li))
##
##
##
##for i in li:
##    print(i)


##
##li = [(1,2),(3,4),(5,6),(1,2)]
##
##li = set(li)
##
##
##
##print(li)


##li = ["amit","rahul","roshan","kusumba","tiger"]
##
##
##print(sorted(li))
##
##

##li = [1,2,3,4,5,6]
##
##
##for i in li:
##    print(i)



##a = [1,2,3,4,5]
##
##b = [1,2,4,6,7,8]
##
##
##b = set(b)
##
##a= set(a)
##
##print(a.symmetric_difference(b))
##
##
##tu = (12,33,4,5,6,6,)
##
####
####for i in tu:
####    print(i)
##
##
##print(min(tu))
##
##print(max(tu))
##
##
##print(tu.count(1)





























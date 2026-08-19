

##li = [1,2,3,4,5]
##
##print(li)

##print(li[4])


##li = [[1,2,3],[23,44,55],[344,33]]

##for i in range(0,len(li),1):
####    print(li[i])
##
##
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        print(li[i][j])


##li[1].append(144)
##print(li)
##
##
##li[2].pop(1)
##print(li)


##li[1].remove(23)
##print(li)
##
##
##li[1][2]=233
##
##print(li)


##li = [1,2,3,4,5,6,7,8,9,10]
##
##for i in range(0,len(li),1):
##    if li[i]%2==0:
##        print(li[i])




##li = [[1,2],[2,3,4],[1,2,3,[24,23]]]

##print(li[2][3][1])

##num = [10,20,30,40]
##
##num.insert(2,25)
##
##print(num)


##li = [11,22,33,44,55]
##
##sum1=0
##
##for i in range(0,len(li),1):
##    if li[i]%2==0:
##        print("even",li[i])
##    else:
##        sum1+=li[i]
##
##print(sum1)
##
##-----------


##li = ["roshan","sonu"]
##
##for i in range(0,len(li),1):
##    print(li[i].upper())
####    print(li)
##



##
##li = [[1,2,3],
##      [4,5,6],
##      [7,8,9]]
##sum1=0
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##            if i+j==2:
##                sum1+=li[i][j]
##                
##                   
##print(sum1)




##
##li = [1,2,3,4,5,6,7,8,9,10]
##
##s = 0
##for i in range(0,len(li),1):
##    s = li[i]**2
##
##    print("square is a:-",s)
##
##    if li[i]%2==0:
##        print("even",li[i])
##



##li=[[1,2,3],[4,5,6],[7,8,9]]
##
##for i in range(0,len(li),1):
##    for j in range(0,len(li),1):
##        s = li[i][j]**2
##        print(s)
##


##
##li = ["r","o","s","a","n","t"]
##
##new =0
##
##for i in range(0,len(li),1):
##    if li[i] in new:
##        pass
##    else:
##        new.extend(li[i])
##
##print(new)    
##



##def A():
##    def add(a,b):
##        print(a+b)
##
##    def sub(a,b):
##        print(a-b)
##
##    return add,sub
##
##
##e,r = A()
##
##e(20,34)
##r(23,45)
##


##li = [1,3,4,5,6,7]
##
##
##li.append("roshan")
##
##li.remove(3)
##
##li.extend([1,2,3,4])
##
##
##print(li)

##
##li = [1,2,3,4,5,6,7,8]
##
##print(li.index(7,5,7))
##


##print(li.count(2))


##li.sort(reverse=False)
##
##print(li)


##li = ["red","green","blue","yellow"]
##
##
##li.remove("green")
##print(li)
##print(d)

##
##li = [[1,2],[3,4],[5,6]]
##
####print(li[1][1])
##
##li.append([7,8])
##
##print(li)

##li.extend([[20,21],[23,34]])
##
##print(li)



##li = [1 3,2,3,4,5,6]
##
##s=0
##s.min(li)
##
##print(s)

##d = max(li)
##
##print(d)

##print(len(li))
##count=0
##for i in range(0,len(li),1):
##    count+=1
##
##print(count)

##
##li = [1,2,3,4,5,6,7,8,9,10]
##
####print(li[0:5])
####
####print(li[5:10])
####
##
##
##li.insert(2,25)
##print(li)
##
##li.remove(5)
##print(li)
##
##li[2]=55
##print(li)

##
##
##
##li = [1,2,3,4,5,6,6,7,6,7,7,8,8,9,9,9]
##
##sum1=0
##for i in range(0,len(li),1):
##    if li[i]%2==0:
##        print(li[i])
##    else:
##        sum1+=li[i]
##        print("odd number",li[i])
##        
##
##
##print("sum of all odd number is a",sum1)
##

##
##word = ["apple","banana","cherry","kiwi","mango"]
##
##for i in range(0,len(word),1):
##    if len(word[i])>5:
##        print(word[i].upper())
##

##li = [[1,2,3],[4,5,6],[7,8,9]]
##sum1=0
##for i in range(0,len(li),1):
##    for j in range(0,len(li),1):
##        if i+j==2:
##            sum1+=li[i][j]
##
##print(sum1)
##

##
##li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
##
##
##for i in range(0,len(li),1):
####    d = li[i]**2
####    print("square is a:--------------",d)
##
##    if li[i]%2==0:
##        d = li[i]**2
##        print("even number :---",d)
##
##
####
##
##
##
##li = [1,2,3,4,22,344,22,2,1,3]
##li2 = [0]
##for i in range(0,len(li),1):
##    if li[i] in li2:
##        pass
##    else:
##        li2.append(li[i])
##        
##
##print(li2)
####    
##

##print(li[::-1])
##
##for i in range(len(li)-1,-1,-1):
##    print(li[i])
##    


##li2 = ["roshan","sonu","rohit"]
##
##li.extend(li2)
##
##print(li[10:15])



##
##for i in range(0,6,1):
##    print(" "*(5-i),"*"*((2*i)-1))
##
##for i in range(5,0,-1):
##    print(" "*(6-i),"*"*((2*i)-3))


##
##for i in range(0,5,1):
##    for j in range(0,4,1):
##        if i==0 or i==4 or j==0 or j==3:
##            print(" "*(4-i),"*",end="")
##        else:
##            print(" ",end="")
##
##    print()
##
##
####
##for i in range(0,5,1):
##    for j in range(0,5,1):
##        print("*",end="")
##
##    print()
##
##
##
##
####
##for i in range(1,5,1):
##    print(" "*i,"*"*5)
##







##def prime(n):
##    num=n
##    factor=0
##
##    for i in range(2,num-1,1):
##        if num%2==0:
##            factor+=1
##
##    if factor==0:
##        print(f"prime number {num}")
##    else:
##        print("not a prime number------------------",num)
##
##
##
##for i in range(1,100,1):
##    prime(i)
##



##
##num = 121
##
##rev = 0
##
##no = num
##
##while (no>0):
##    a = no%10
##    rev = rev * 10 +a
##    no = no//10
##
##
##if rev == num:
##    print("the number is palindrome",no,rev)
##else:
##    print("the number is not palindrome")
##
##print("hii")



##
##
##num = 370
##
##
##cube = 0
##
##
##no = num
##
##
##for i in range(1,num+1,1):
##    a = no%10
##    cube = cube * a**a
##    no = no//10
##
##if cube==no:
##    print("amstrong number",cube)
##else:
##    print("not amstrong number")








##
##st = "aaccbbdssdsssssssssssssiaaaaaaaaaaaa"
##
##
##count=0
##for i in range(0,len(st),1):
##    count = st.count(st[i])
##    if count==1:
##        print(st[i])
##
##
##333
####
##st = "programming"
##
##
##for i in range(0,len(st),1):
##    if st[i]=="g":
##        count=i
##        break
##
##
##print(count)


##st = "aaaa bbbbb cccccc"
##count=0
##index=0
##for i in range(0,len(st),1):
##    for j in range(0,len(st[i]),1):
##        count=len(st[i])
##
##        if len(st[i])>count:
##            index=i
##
##		
##print(count)
##print(index)
##

##
##print(st.count("a"))
##        
##
##for i in range(0,len(st),1):
##    if len(st[i])==3:
##        print(st[i].startswith("a"),end="")





##st = "python"
##
##st1 = "cyton"
##
##count=""
##for i in range(0,len(st),1):
##    if len(st)==len(st1):
##        if st[i] in st1:
##             count=st[i]
##             print(count,end="")
##    else:
##        print("your sting len is not same")
##        break
##


##
##st = "listen"
##st1 = "slent"
##master=True
##for i in range(0,len(st),1):
##    if st[i] not in st1:
##        master=False
##
##
##if master==True:
##    print("the word")
##else:
##    print("not words")




st = "python1233"

print(st.isdigit())
print(st.isalnum())

print(st.upper())
print(st.lower())
print(st.startswith("p"))
print(st.endswith("3"))

print(st.count("3"))

print(st.isalpha())

























































































































































































































































##
##
##t = (1,2,3,4,5)
##
##print(t)


##t1 = (1,2,3,4,5,6,7,8,9)

##for i in range(0,len(t1),1):
##    print(t1[i])


##print(t1.count(1))
##
##print(t1.index(4,0,7))
##
##
##print(len(t1))

##t1 = (1,2,3,4,5,6,7,8,9,10)
##
##print(t1)
##
##t1 = (1,2,3,4,5,6,7,8)
##
##print(t1[0])
##
##print(t1[7])

##t1 = (1,2,3)
##
##t2 = (4,5,6)
##
##print(t1+t2)


##t1 = ("hi",)
##
##print(t1 *5,"\n")






##
##t1 = (1,2,3,4,5,7)
##
##
##for i in range(0,len(t1),1):
##    if t1[i]==5:
##        print("five is present",t1[i])
##        break
##    else:
##        print("not present")
##





##t1 = (1,2,3,4,5,6)
##
##print(len(t1))
##
##count = 0
##
##t1 = (1,2,3,4,5,6,7)
##
##for i in range(0,len(t1),1):
##    count+=1
##
##
##print(count)
##




##li = [1,2,3,4,5]
##
##print(type(li))
##
##d = tuple(li)
##
##print(type(d))
##
##t1 = (20,30,40,50,60)
##
##
##d = list(t1)
##
##print(d)
##
##
##t1 = (1,2,3,4,5)
##
##print(min(t1))
##print(max(t1))


##
##t1 = ((1,2),(3,4),(5,6),(12,3,(1,2,3)))
##
##print(t1[3][2][1])

##
##t1 = (1,2,3,4,5,6,8,7)
##
##t2 = (11,22,33,44,55,7)
##
##
##for i in range(0,len(t1),1):
##    if t1[i] in t2:
##        print(t1[i])
##


##t1 = ()
##
##print(type(t1))
##



##t1 = (11,22,33,44,55)
##
##
##print(t1[4])



##
##t1 = (1,2,3,4,5,6)
##
##print(t1[1:4])
##



##li = [1,2,3,4,5,6]
##
##
##print(li)
##
##li.append(200)
##
##print(li)


##li.remove(3)
##
##print(li)
##
##
##li.insert(2,44)
##
##print(li)
##
##li.extend([2,3,4,5,5])
##
##print(li)
##
##
##print(li.count(4))
##
##
##li.sort(reverse=True)
##
##print(li)
##
##
##print(li.index(5,0,len(li)))
##
##d = li.copy()
##
##print(d)
##
##
##t1 = (1,22,33,4,55,6,7,8,9,10)
##
##
##print(sorted(t1))
##
##
##












##
##
##li = [1,2,3,3,4,5,6]
##
##li.append(5)
##
##print(li)
##
##
##li.insert(2,55)
##
##print(li)
##
##
##li.extend([1,2,3,4,5])
##
##print(li)

##li = ["apple",2,3,4,5,6]
##
##li.remove("apple")
##print(li)

##
##li = ["apple","cherry","apple","mango"]
##
##li.pop()
##
##print(li)
##
##li.clear()
##
##print(li)
##


##li = [1,2,3,4,5,6]
##
##
##print(li.index(2,0,5))
##
##print(li.count(3))


##li = [90,323,453,343,213]


##print(sorted(li))

##
##print(reversed(li))

##
##li = ["red","green","blue","yellow"]
##
##d = li.copy()
##
##print(d)
##
##d.remove("green")
##print(d)
##
##


##m = [[1,2],[3,4],[5,6]]
##
##print(m[1][1])
##
##
##m.append([1,3])
##
##print(m)
##
##
##m.extend([12,33,44,55])
##
##print(m)


##li = [1,2,3,4,5,6,7,8,9,10]
##
##
##print(min(li))
##
##
##print(max(li))
##
##print(sum(li))
##
##
##print(len(li))

##
##li = [1,2,3,4,5,6,7,8,9,10]
##
##count = 0
##
##for i in range(0,len(li),1):
##    count+=1
##
##print(count)


##li = [1,2,3,4,5,6,7,8,9,10]
##
##print(li[0:5])
##
##print(li[5:10])


##
li = [1,2,3,4,5,6,7]
##
##
##li.insert(1,22)
##
##
##print(li)

##
##li.remove(4)
##
##print(li)
##sum=0
##
##for i in range(1,len(li),1):
##    if li[i]%2==0:
##        print(li[i])
##    else:
##        sum+=li[i]
##
##print("odd",sum)


##word = ["apple","banana","cherry","kiwi","mango"]
##
##for i in range(0,len(word),1):
##    if len(word[i])>5:
##        print(word[i].upper())

##li = [[1,2,3],
##      [4,5,6],
##      [7,8,9]]
##
##sum=0
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i==j:
##            sum+=li[i][j]
##
##print(sum)
##
##
##for i in range(0,len(li),1):
##    for j in range(0,len(li[i]),1):
##        if i+j==2:
##            print(li[i][j])
##            sum+=li[i][j]
##
##print(sum)


##li = [1,2,3,4,5,6,7,8,9,10]
##
##
##for i in range(0,len(li),1):
##    if li[i]%2==0:
##        print("square is a:-",li[i]**2)



##li = [1,2,3,4,5]

##li1=[1,2,3]
##
##print(li+li1)
##
##for i in range(0,len(li),1):
##    if li[i] not in li1:
##        print(li+li1)
##        


##print(li1)
##


li = [1,2,3,44,22,111,22]

largest = [0]

for i in range(0,len(li),1):
    if li>=largest:
        largest=li[i]


print(largest)



























##
##
##
####
####li = [1,2,3,4,5]
####
####
####li.append(6)
####print(li)
####
####
####li.insert(3,100)
####
####print(li)
####
####
####li.extend([12,234,455])
####print(li)
####
####
####print("\n")
####
####print(li[1])
####
####
####f = ["apple","cherry","banana","cherry"]
####
####f.remove("apple")
##
##print(f)
##
####
####f.pop()
####print(f)
####
######f.clear()
####
####print("\n")
####
####l = [1,3,5,7,8]
####
####l.index(7,0,4)
####
####print(l)
####
####
####print(l.count(7))
######print(l)
##
##
##
##
##data = [23,1,24,2,45]
####
####
####data.sort()
####print(data)
##
##
####
####data.sort(reverse=True)
####
####print(data)
##
####print(data[::-1])
##
##
####data.reverse()
####print(data)
##
####
####
####color = ["red","green","blue","yellow"]
####
####color.remove("green")
####print(color)
####
####
####d = color.copy()
####print(d[::-1])
##
##
##
##
##
##li = [[1,2],[3,4],[5,6]]
####
######print(li)
####
####
####li.index(4,0,5)
####print(li)
##
####li.append([7,8])
####
####print(li)
####l2 = [23,1,3,4]
####
####li.extend(l2)
####print(li)
####
##
##
##
####l = min(li)
####
####l2 = max(li)
####print("min",l)
####print("max",l2)




##
a  = [1,2,3,4,5,6,7,8,9,10]
##
##
####print(len(a))
##
##
##for i in range(0,len(a)):
##    if a[i]==0 and a[i]==5 and a[i]==10:
##        print(a[i])
##

##print(li)



number = [11,22,33,44,55,66]

number.append(77)
print(number)

number.remove(44)
print(number)

number.pop()
print(number)


##li = [2,3,4,5,6,7,8]
##sum1 = 0
##for i in range(0,len(li),1):
##    if li[i] % 2 ==0:
##        print(li[i],end=" ")
##    else:
##        sum1+=li[i]
##
##print("odd number sum is a:--",sum1)
##    



##words = ["aple","banana","cherry","kiwi"]
##
##for i in range(0,len(words),1):
##    if len(words[i])>5:
##        print(words[i])
##
##
##word = ["apple","banana","cherry","kiwi"]
##
##for i in range(0,len(word),1):
##    word[i].upper()
##    print(word)
##


##
##
##matrix = [[1,2,3],[1,5,6],[7,8,9]]
##sum1= 0
##for i in range(0,len(matrix),1):
##    if len(matrix[i])>0:
##        if matrix[0]==0 or matrix[1]==1 or matrix[2]==2:
##            sum1 +=matrix[i]
##        else:
##            print("*")
##
##
##print(sum1)
##
##



##li = [11,2,3,3,4,4]
##count = 0
##for i in range(0,len(li),1):
##    if li[i] in count:
##        pass
##    else:
##        count=li[i]
##
##
##print(count)

li1 = [1,2,3,4,"roshan"]
li2 = ["roshan","sonu",123]

li1.extend(li2)
print(li1)




































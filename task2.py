
##
##
##name = "abcdeccsa"
##
##new_st=""
##for i in range(0,len(name),1):
##    if name[i] in new_st:
##        pass
##    else:
##        new_st+=name[i]
##
##print(new_st)

##
##name ="roshan pardeshi vijay"
##
##count=0
##count1=0
##for i in range(0,len(name),1):
##    if name[i]!="a" and name[i]!="e" and name[i]!="i" and name[i]!="o" and name[i]!="u":
##        count+=1
##    else:
##        count1+=1
##
##print(count)
##print(count1)


##name = "abcdefccddaa"
##new_st =""
##
##for i in range(0,len(name),1):
##    if name[i] not in new_st:
##        new_st+=name[i]
##
##
##print(new_st)


##st = "roshan pardeshi"
##
##st = st.split()
##size=0
####print(st)
##index=0
##for i in range(0,len(st),1):
##    if len(st[i])>size:
##        size=len(st[i])
##        index=i
##
##print(st[index])
##        

    
##st = "aaabbbcdsadd"
##fact = 0
##for i in range(0,len(st),1):
##    count = st.count(st[i])
##    if count == 1:
##        fact +=1
##        if fact==2:
##            print(st[i])
    


                  
##st = "roshan vijay pardeshi"
##
##
##st = st.split()
##
##print(st)

#############################




st = "roshan pardeshi"


st = st.split()

size=0
for i in range(0,len(st),1):
    if len(st[i])>size:
        size+=len(st[i])

print(size)

















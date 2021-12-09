list=[15,48,'hello',6, 19,"world"]
s = 0
s2=0
for i in list:
    if type(i) is int:
      if i % 2 == 0:
            while i>0:
               s+=i%10
               s2=i//10
            print(i,s)
    else:
        list[list.index(a2)]=1
    print(list)


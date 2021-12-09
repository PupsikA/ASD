qmi=input("Число:")
orr=0
att=0
er=0
yu=1
for i in ty:
     if i % 2 == 0:
         orr += 1
     elif i//10==0:
         att += 1
if orr>att:
    for yt in ty:
        er+=yt
    print(er)
elif orr<att:
    we=ty[0:8:2]
    for t in we:
        yu*=t
    print(yu)



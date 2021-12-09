import random
a=input("ВВедите число от 1 до 20:")
b=input("ВВедите второе число от 1 до 20:")
rtt=0
ytt=0
iter4_1=0
iter4_2=0
equal=0
for i in range(9):
    a2 = random.randint(1,20)
    b2 = random.randint(1,20)
    if i==4:
        iter4_1=a2
        iter4_2=b2
    if a+b>a2+b2:
        rtt+=1
    elif a+b<a2+b2:
        ytt+=1
    else:
        equal+=1
    if




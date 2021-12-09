import random
a=random.randint(1,20)
b=random.randint(1,20)
t=0
while t<5:
    t+=5
z=input("")
z=z.split("")
if int(z[0])==a and int(z[1])==b:
    print("")
    break
else:
    print("")
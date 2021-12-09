import random
alt=[random.randint(0,100) for i in range(10)]
if 20 in alt:
    alt[alt.index(20)]=200
    print(alt)
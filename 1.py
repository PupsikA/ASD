W=input("Ввод")
import random
a=random.randint(1,3)
if (W==1 and a==3)or(W==2 and a==1)or(W==3 and a==2):
    print("Вы победили")
elif W==a:
    print("Ничья")
else:
    print("Вы проиграли")

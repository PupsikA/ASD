t=int(input("Введите первое число"))
y=int(input("Введите второе число"))
u=int(input("Введите третье число"))
if t == y+u:
    print(y,"+",u,"=",t)
if y == t+u:
    print(t,"+",u,"=",y)
if u == t+y:
    print(t,"+",y,"=",u)
elif t > y+u:
    print("Неправильные числа")
elif y > t + u:
    print("Неправильные числа")
elif u > y+t:
    print("Неправильные числа")







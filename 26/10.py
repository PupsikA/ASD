A=input("Введи строку")
B=(A[6:])
С =int(B.isdigit())
X = (A[7:])
Z = (A[:6])
if Z =="строка":
 print(X*3)
elif Z!="строка":
    print("Неправильный ввод!")
    if A == "True":
        print("Ты ввел ложь!")
    if A == "False":
        print("Ты ввел правду!")
    if С==False:
        print("Неверный ввод!")
    if С==True:
        D=input("Введите второе число")
        E=(D[6:])
        W =(E.isdigit())
    if W ==True:
        print("Сумма чисел:",int(B)+int(E))











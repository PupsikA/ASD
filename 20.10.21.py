Q=input("Введите фигуру:")
if Q == "прямоугольник":
    Y=int(input("Введите 1 сторону"))
    print(Y+T)
if Q == "треугольник":
    Z = int(input("Введите сторону"))
    if Z>0:
        p=Z*3
        print(p)
    else:
        print("Неверное число")
if Q == "круг":
    R=input("Укажите радиус")
    while True:
        try:
            R = input()
            if R <= 0:
                print("Не верный ввод")
            R = input("Введите радиус")
            break
        except ValueError:
            print("Введите значение")
    print(2*R*3.14)





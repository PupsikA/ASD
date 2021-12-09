a=input("Введите фигуру")
if a == "треугольник":
    b=int(input("Введите сторону"))
    if b>0:
        p=b*3
        print(p)
    else:
        print( "Неверное число")

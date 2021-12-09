import random
qwe=int(input("Введите количество играков:"))
asd=input("Введите их имена:")
ert=asd.split()
SD=[]
#print(ert)
while True:
    er=int(random.randint(1,6))
    print(er)
    for i in enumerate(ert):
        ty = input("Введите число от 1 до 6:")
        SD.append(ty)
        print(f'{i[1]} - {ty}')
        if i==qwe:
            break
        for u in enumerate(SD):
            if er==u:
                SD.remove(u)
                print("Выбыл")






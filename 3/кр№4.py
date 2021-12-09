import random
qwe=int(input("Введите количество рандомных чисел:"))
ewq=input("Введите число, которое нужно искать:")
cv=0
for i in range (qwe):
    er=str(random.randint(1,1000))
    for j in er:
        if ewq == j:
            cv+=1
print(cv)

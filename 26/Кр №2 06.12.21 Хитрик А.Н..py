#Задание №1
# a=[1,2,3,4,5,6,1,2,3,4,5,6]
# b=[]
# for i in a:
#   if i not in b:
#     b.append(i)
# print(b)

#Задание №2
# qwe=[1,2,1,3,3,4,5]
# q = 0
# for i in range(len(qwe)):
#     for j in range(i + 1, len(qwe)):
#         if qwe[i] == qwe[j]:
#             q += 1
# print(q)

#Задание №3
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# q=sum(C_1)
# w=sum(C_2)
# if q>w:
#     print('Сумма больше в кортеже - C_1')
# else:
#     print('Сумма больше в кортеже - C_2')
# print('min C_1','номер- ',C_1.index(min(C_1)))
# print('max C_1','номер- ',C_1.index(max(C_1)))
# print('min C_2','номер- ',C_2.index(min(C_2)))
# print('max C_2','номер- ',C_2.index(max(C_2)))


#Задание №6
# Rrt=[1,2,3,4,5,6,1,2,3,4,5,6]
# we=[45, 21,124,76,5,23,91,234]
# print(f'Список Rrt-{len(Rrt)} чисел, Список we -{len(we)} чисел')

#Задание №7
di = {"a": 1, "b": 2, "c": 3}
try:
    value = di["d"]
except KeyError:
    print(" KeyError!")
finally:
    print("Оператор выполнен")
tra=input("Введите строку:")
lower=0
upper=0
for i in enumerate(tra):
    if i[0] == len(tra)-1:
        break
    else:
        if i[1].islower() and tra[i[0]+1].islower():
            lower+=1
        elif i[1].isupper()and tra[i[0]+1].isupper():
            upper+=1
print()


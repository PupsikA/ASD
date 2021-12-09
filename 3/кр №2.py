ott=input("Введите текст:")
nm=0
pom=0
tre=[]
for i in ott:
    if i in 'ёуеыаоэяиюЁУЕЫАОЭЯИЮaeyiouAEYIOU':
        nm += 1
        tre.append(i)
    else:
        pom += 1
if nm==pom:
    print(",".join(tre))
else:
    print("Гласные:",nm,"Согласные:",pom)



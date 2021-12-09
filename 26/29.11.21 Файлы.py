# w=open('fail.txt,r')
# we=w.readline()
# er=[]
# for i in we:
#     if
#     i+=er
#     ty=''.split(er)
#     print(sum(er))

# with open('fail.txt','r') as re:
#     rt=re.readlines()
#     print(rt)
# for i in rt:
#     i=i[:-1]


# with open('fail.txt','r') as user:
#     while True:
#         user=input("Введите данные")
#         if user == "":
#             break
#             else:
#             f.write(user+"\n")

# with open('fail.txt','r',encoding='') as user:
#     lines={}
#     for index,line in enumerate(f):
#         index+=1
#         line =line.replise

# Домашнее задани
qwe = ['Autodesk', '23', 'Piton', '45', 'youtube', '3456']
qw =[]
ew=[]
for i in qwe:
    if i.isdigit():
        i = int(i)
        qw.append(i)
    elif i.isalpha():
        i=str(i)
        ew.append(i)
rt=(' '.join(sorted(ew, key=len)))
print(rt)
ty=(sorted(qw))
ad=" ".join(str(x) for x in ty)
print(ad+'n'rt)
f=open('fail.txt','w')
f.write(rt)
f.write(ad)
f.close()



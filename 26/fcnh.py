qwe=("Курица, Кепка, Сыр, Салат, информатика")
long_word=(qwe).split()
leters=[]
for i in long_word:
    if i in leters:
        continue
    else:
        print(f"{i}-{long_word.count(i)}")
        leters.append(i)
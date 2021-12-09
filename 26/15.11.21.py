
while True:
    qwe=input("Введите логин:")
    if"@" in mail:
        if "." in [qwe.index("@")]:
           break
        else:
           print("Неверная почта")
    else:
        print("Почта неверна")
while True:
    phone=input("Введите телефон:")
    if phone [:4]=="+375":
        if phone[1:].isdigit():
            if len(phone)==13:
                break
        else:
            pass
    else:
        pass
else:
    pass


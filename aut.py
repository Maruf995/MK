print('__Sign_Up__')

username = input("Введите свой ник: ")

name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")

while True:
    gmail = input("Введите свой gmail: ")
    if gmail[-10:] != "@gmail.com":
        print("Почта должна содержать @gmail.com !")
    else:
        break
    
phone = input("Введите свой номер: ")

while True:
    age = 2021 - int(input("Введите год вашего рождения: "))
    if age < 8:
        print("Щегол иди спи!")
    else:
        break

while True:
    password1 = input("Введите свой пароль: ")
    password2 = input("Повторите свой пароль: ")
    if password1 != password2:
        print("ЭЭЭ нормально пиши!!!!!")
    else:
        break

user = dict(
    username=username, 
    name=name, 
    surname=surname, 
    gmail=gmail,
    age=age,
    phone=phone,
    password=password1
    )

for key, values in user.items():
    print(f"{key}: {values}")


while True:
    username = input("Введите свой ник: ")
    password = input("Введите пароль: ")
    if username != user['username'] or password != user['password']:
        print("Неверный логин или пароль!")
    else:
        print("Успешная авторизация <3 ")
        break
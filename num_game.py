import random

count = 0

tries = int(input("Введите количество попыток: "))
        

while count != tries:
    a = random.randint(1,9)
    b = random.randint(1,9)
    product = a*b
    try:
        answer = int(input(f"{a} * {b} = ? "))
        count += 1 

        if answer != product:
            print(f"Неправильно! Ответ - {product}\n")

        else:
            print(f"Правильно! Ответ - {product}")

        if tries != count:
            print(f"Количество оставшихся попыток - {tries-count}.\n")
            
    except ValueError:
        print("Вводите только целые числа!")
        
print("Игра окончена! Спасибо за игру <3")
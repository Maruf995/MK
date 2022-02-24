import random

number = random.randint(1, 100)
count = int(input("Сколько попыток вам нужно? "))

while count != 0:
    count -= 1
    try:
        guess = int(input('Отгадайте число: '))
    except ValueError:
        print('Вводите целые числа!')
        continue
    if guess == number:
        print(f'Поздравляю, вы угадали!')
        break
    elif guess < number:
        print('Больше')
        print(f'У вас осталось {count} попыток!')
    elif guess > number:
        print('Меньше')
        print(f'У вас осталось {count} попыток!')

print("Это число:", number)
print('Игра окончена!')

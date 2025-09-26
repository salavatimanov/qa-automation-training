# Задание проверка возраста
from operator import index

age = 35

if age < 18:
    print('Доступ запрещен')
elif 18 < age < 65:
    print('Добро пожаловать')
else:
    print('Особый случай')

# Задание для закрепления цикла for

i = [1,2,3,4,5]

for square in i:
    print(square**2)


names = ['Salavat', 'Alina', 'Daniil']
for hello in names:
    print(f'Hello, {hello}')

nums = [2,5,7,10,13]

for i in nums:
    if i % 2 == 0:
        print(i)


# Задание таблица умножения

for i in range(7,77,7):
    print(i)

# Сумма чисел через while

i = 1
total = 0

while i <= 100:
    total += i
    i += 1
print('Сумма:', total)

# Списки + условия

names1 = ['Anya', 'Boris', 'Vasya', 'admin']

for n in names1:
    if n != 'admin':
        print(f'Здравствуй, {n}')
    else:
        print('Привет, админ')
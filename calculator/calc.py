
first_input = input('Введите число: ')

try:
    num1 = int(first_input)
except:
    num1 = float(first_input)

print(num1)

second_input = input('Введите второе число: ')

try:
    num2 = int(second_input)
except:
    num2 = float(second_input)

print(num2)

op_input = input('Введите знак сложения, вычитания, умножения или деления: ')

if op_input == '+':
    print(f' Результат: {num1 + num2}')
elif op_input == '-':
    print(f' Результат: {num1 - num2}')
elif op_input == '*':
    print(f' Результат: {num1 * num2}')
elif op_input == '/':
    print(f' Результат: {num1 / num2}')
else:
    print('Ошибка, иди нахуй')

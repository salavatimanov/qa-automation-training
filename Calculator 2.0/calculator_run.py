from calculator_logic import Calculator


calc = Calculator()

a = input('Введите первое число: ')

b = input('Введите второе число: ')

operation = input('Введите знак сложения, вычитания, умножения или деления: ')

if operation == '+':
    print(calc.add(a, b))
elif operation == '-':
    print(calc.sub(a, b))
elif operation == '*':
    print(calc.mul(a, b))
elif operation == '/':
    print(calc.div(a, b))
else:
    print('Ошибка со знаком')







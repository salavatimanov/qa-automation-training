class Calculator:
    def add(self, a, b):
        try:
           a = float(a)
           b = float(b)
        except ValueError:
            print('ОШИБКА: Введи число')
            return None
        return a + b


    def sub(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('ОШИБКА: Введи число')
            return None
        return a - b

    def mul(self, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('ОШИБКА: Введи число')
            return None
        return a * b

    def div(self, a, b):
        try:
            a = float(a)
            b = float(b)
            result = a / b
        except ValueError:
            print('ОШИБКА: Введи число')
            return None
        except ZeroDivisionError:
            print('На ноль делить нельзя')
            return None
        return result


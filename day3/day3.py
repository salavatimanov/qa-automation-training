


def welcome():
    """Приветствие в автотестах"""
    print('Добро пожаловать в автотестирование')

welcome()

def welcome_name(name):
    """Приветствие по имени"""
    print(f'Добро пожаловать, {name}')

welcome_name('Салават')

def mp(a,b):
    return a * b

result = mp(7,8)
print(result)


import utils as ut

result = ut.add(9,7)
print(result)

result = ut.sub(98, 8)
print(result)
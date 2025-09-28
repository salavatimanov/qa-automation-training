class User:
    def __init__(self, name, age):
        self.age = age
        self.name =  name

User1 = User('Salavat' , 23)
User2 = User('Alina', 23)

print(User1.name)

def say_hello(self):
    print('Привет, меня зовут ' + self.name + ', мне ' + str(self.age))

say_hello(User1)

say_hello(User2)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f'Автомобиль: {self.brand}, {self.model}, {self.year}')



car1 = Car('Mercedes','E212', '2012' )
car2 = Car('Mercedes', 'CLA', '2014')
car3 = Car('Changan', 'UNI-V', '2023')


Car.info(car1)

Car.info(car2)

Car.info(car3)

import os

class Person:
    def __init__(self):
        ...
    
    def __str__(self):
        return f'Name: {self.__name}\nAge: {self.__age}'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name
        print('Свойство имя удалено.')

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
    @age.deleter
    def age(self):
        del self.__age
        print('Свойство возраст удалено.')

me = Person()
me.name = 'Egor'
me.age = 20
print(me)
del me.name
del me.age

os.system('pause')
os.system('cls')

friend = Person()
friend.name = 'Ilya'
friend.age = 21
print(friend)
del friend.name
del friend.age

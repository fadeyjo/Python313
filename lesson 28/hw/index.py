import math
import os

class Validator:
    @staticmethod
    def input_float_positive_value(line: str) -> float:
        while True:
            try:
                value = float(input(line))
                if value <= 0:
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите ввод.')
            except Exception:
                print('Число должно быть положительным. Повторите ввод.')
        return value

class Table:
    def __init__(self, width: float = None, height: float = None, radius: float = None):
        if radius:
            self._radius = radius
        else:
            self._width = width
            self._height = height

class Rectangle_table(Table):
    def __init__(self):
        super().__init__(width = Validator.input_float_positive_value('Ширина стола: '), height = Validator.input_float_positive_value('Высота стола: '))
    
    def __str__(self) -> str:
        return f'Площадь прямоугольного стола: {self.__area()}'
    
    def __area(self) -> float:
        return round(self._width * self._height, 2)

class Circle_table(Table):
    def __init__(self):
        super().__init__(radius = Validator.input_float_positive_value('Радиус стола: '))
    
    def __str__(self) -> str:
        return f'Площадь круглого стола: {self.__area()}'
    
    def __area(self) -> float:
        return round(math.pi * math.pow(self._radius, 2), 2)

rectangle_table = Rectangle_table()
print(rectangle_table)

os.system('pause')
os.system('cls')

circle_table = Circle_table()
print(circle_table)
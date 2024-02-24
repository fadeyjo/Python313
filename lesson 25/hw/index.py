import turtle
import math
import os

class Controller:
    @staticmethod
    def input_valid_positive_float(line):
        while True:
            try:
                value = float(input(line))
                if value <= 0:
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите попытку.')
            except Exception:
                print('Недопустимое значение. Повторите ввод.')
        return value

class Rectangle:
    def __init__(self):
        self.__length = Controller.input_valid_positive_float('Введите длину прямоугольника: ')
        self.__width = Controller.input_valid_positive_float('Введите ширину прямоугольника: ')
        self.__calculate_area()
        self.__calculate_perimetr()
        self.__calculate_diagonal()
        self.__print__info()
        self.__draw()
    
    def __calculate_area(self):
        self.__area = self.__length * self.__width
    
    def __calculate_perimetr(self):
        self.__perimetr = 2 * (self.__length + self.__width)
    
    def __calculate_diagonal(self):
        self.__diagonal = round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
    
    def __print__info(self):
        os.system('cls')
        print(f'Длина прямоугольника: {self.__length}')
        print(f'Ширина прямоугольника: {self.__width}')
        print(f'Площадь: {self.__area}')
        print(f'Периметр: {self.__perimetr}')
        print(f'Диагональ: {self.__diagonal}')
    
    def __draw(self):
        pen = turtle.Pen()
        pen.forward(self.__length)
        pen.left(90)
        pen.forward(self.__width)
        pen.left(90)
        pen.forward(self.__length)
        pen.left(90)
        pen.forward(self.__width)
        pen.left(90)

rectangle = Rectangle()
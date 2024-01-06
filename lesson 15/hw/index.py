import math

print_area_of_circle = lambda radius = 2: print(f'Площадь окружности радиуса {radius}: {radius**2 * math.pi}')
print_area_of_rectangle = lambda length = 10, width = 13: print(f'Площадь прямоугольника размером {length}*{width}: {length * width}')
print_area_of_trapezoid = lambda base1 = 7, base2 = 5, height = 3: print(f'Площадь трапеции для a={base1}, b={base2}, h={height}: {(base1 + base2) * height * 0.5}')

print_area_of_circle()
print_area_of_rectangle()
print_area_of_trapezoid()
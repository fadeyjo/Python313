class Area:
    count = 0

    @staticmethod
    def triangle_area_by_geron(a, b, c):
        p = (a + b + c) / 2
        Area.count += 1
        return (p * (p - b) * (p - a) * (p - c)) ** (0.5)
    
    @staticmethod
    def triangle_area_base_and_height(base, height):
        Area.count += 1
        return 0.5 * base * height
    
    @staticmethod
    def square_area(side):
        Area.count += 1
        return side ** 2
    
    @staticmethod
    def rectangle_area(first_side, second_side):
        Area.count += 1
        return first_side * second_side
    
print(f'Площадь треугольника по Герону: {Area.triangle_area_by_geron(3, 4, 5)}')
print(f'Площадь по основанию и высоте: {Area.triangle_area_base_and_height(6, 7)}')
print(f'Площадь квадрата: {Area.square_area(7)}')
print(f'Площадь прямоугольника: {Area.rectangle_area(2, 6)}')
print(f'Количество подсчётов: {Area.count}')
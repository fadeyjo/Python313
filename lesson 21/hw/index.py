def quantity_of_negative_numbers(numbers):
    if len(numbers) == 1:
        return 1 if numbers[0] < 0 else 0
    else:
        return (1 if numbers[0] < 0 else 0) + quantity_of_negative_numbers(numbers[1:])

my_list = [-2, 3, 8, -55, -11, -4, 6, -8, 5]
print(f'Количество отрицательных чисел списка {my_list}: {quantity_of_negative_numbers(my_list)}')
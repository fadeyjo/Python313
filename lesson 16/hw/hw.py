def my_decorator(line):
    def function_doing(my_function):
        def wrap(*numbers):
            print(f'{line} {numbers}: ', end = '')
            my_function(*numbers)
        return wrap
    return function_doing

@my_decorator('Сумма чисел: ')
def additional(*numbers):
    print(sum(numbers))

@my_decorator('Среднее арифметическое чисел: ')
def middle(*numbers):
    print(sum(numbers) / len(numbers))

additional(5, 8)
middle(5, 8)
def count_functions(fn):
    count = 0
    def wrap():
        nonlocal count
        count += 1
        fn(a1, a2)
        print('Вызов функции', count)
    return wrap

@count_functions
def hello(a, b):
    print('Hello', a, b)

hello('Python', 'JavaScript')
class Power:
    def __init__(self, num):
        self.num = num
    
    def __call__(self, func):
        def wrap(*args, **kwargs):
            return func(args[0], args[1]) ** self.num
        return wrap

@Power(3)
def my_func(a, b):
    return a * b

print(my_func(5, 5))

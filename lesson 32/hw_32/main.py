class ValidPositiveInt:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Value must be int!!!')
        if value <= 0:
            raise Exception('Value must be positive!!!')
        instance.__dict__[self.__name] = value


class ValidPositiveFloat:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError('Value must be float!!!')
        if value <= 0:
            raise Exception('Value must be positive!!!')
        instance.__dict__[self.__name] = value


class ValidStr:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be str!!!')
        instance.__dict__[self.__name] = value


class Order:
    __name = ValidStr()
    __price_once = ValidPositiveFloat()
    __amount = ValidPositiveInt()

    def __init__(self, name: str, price_once: float, amount: int):
        self.__name = name
        self.__price_once = price_once
        self.__amount = amount

    def __str__(self):
        return f'All cost is {self.__price_once * self.__amount} RUB.'


first_order = Order('T-short', 1500.90, 350)
print(first_order)

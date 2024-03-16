class Clock:
    __seconds_in_minute = 60
    __seconds_in_hour = 3600

    def __init__(self, seconds: int = 600):
        self.__time_in_seconds = seconds
        self.__hours = self.__convert_seconds_to_hours()
        self.__minutes = self.__convert_seconds_to_minutes()
        self.__seconds = self.__remaining_seconds()
    
    def __sub__(self, other):
        if isinstance(other, Clock):
            return Clock(self.__time_in_seconds - other.__time_in_seconds)
        if isinstance(other, int):
            return Clock(self.__time_in_seconds - other)
        raise ValueError('Type of q argument is incororrect')
    
    def __mul__(self, other):
        if isinstance(other, Clock):
            return Clock(self.__time_in_seconds * other.__time_in_seconds)
        if isinstance(other, int):
            return Clock(self.__time_in_seconds * other)
        raise ValueError('Type of right argument is incororrect')
    
    def __floordiv__(self, other):
        if isinstance(other, Clock):
            return Clock(self.__time_in_seconds // other.__time_in_seconds)
        if isinstance(other, int):
            return Clock(self.__time_in_seconds // other)
        raise ValueError('Type of right argument is incororrect')
    
    def __mod__(self, other):
        if isinstance(other, Clock):
            return Clock(self.__time_in_seconds % other.__time_in_seconds)
        if isinstance(other, int):
            return Clock(self.__time_in_seconds % other)
        raise ValueError('Type of right argument is incororrect')
    
    def __add__(self, other):
        if isinstance(other, Clock):
            return Clock(self.__time_in_seconds + other.__time_in_seconds)
        if isinstance(other, int):
            return Clock(self.__time_in_seconds + other)
        raise ValueError('Type of right argument is incororrect')
    
    def __str__(self) -> str:   
        return f'{self.__hours if self.__hours > 9 else '0' + str(self.__hours)}:{self.__minutes if self.__minutes > 9 else '0' + str(self.__minutes)}:{self.__seconds if self.__seconds > 9 else '0' + str(self.__seconds)}'
    
    def __convert_seconds_to_hours(self) -> int:
        return self.__time_in_seconds // Clock.__seconds_in_hour
    
    def __convert_seconds_to_minutes(self) -> int:
        return (self.__time_in_seconds - self.__hours * Clock.__seconds_in_hour) // Clock.__seconds_in_minute
    
    def __remaining_seconds(self) -> int:
        return self.__time_in_seconds - self.__hours * Clock.__seconds_in_hour - self.__minutes * Clock.__seconds_in_minute

first_clock = Clock(5503)
second_clock = Clock(1234)

print(f'Submition {first_clock - second_clock}')
print(f'Additional {first_clock + second_clock}')
print(f'Multiplication {first_clock * second_clock}')
print(f'Floor div {first_clock // second_clock}')
print(f'Mod {first_clock % second_clock}')
first_clock -= second_clock
print(f'Submition (-=) first_clock = {first_clock}')
first_clock += second_clock
print(f'Additional (+=) first_clock = {first_clock}')
first_clock *= second_clock
print(f'Multiplication (*=) first_clock = {first_clock}')
first_clock //= second_clock
print(f'Floor div (//=) first_clock = {first_clock}')
first_clock %= second_clock
print(f'Mod (%=) first_clock = {first_clock}')
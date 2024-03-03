from abc import ABC, abstractmethod

#class Currency(ABC):
#    course_USD_to_RUB = 0.010949
#    course_EUR_to_RUB = 0.010129
#    suffix_EUR = 'EUR'
#    suffix_RUB = 'RUB'
#    suffix_USD = 'USD'
#
#    def __init__(self, value):
#        self._value = value
#    
#    @abstractmethod
#    def convert_to_RUB(self):
#        pass
#    
#    @abstractmethod
#    def print_info(self):
#        pass
#
#class USD(Currency):
#    def __init__(self, value):
#        super().__init__(value)
#    
#    def convert_to_RUB(self):
#        self.__in_rubles =  self._value / Currency.course_USD_to_RUB
#    
#    def print_info(self):
#        print(f'{self._value} {Currency.suffix_USD} = {self.__in_rubles} {Currency.suffix_RUB}')
#
#class EUR(Currency):
#    def __init__(self, value):
#        super().__init__(value)
#    
#    def convert_to_RUB(self):
#        self.__in_rubles =  self._value / Currency.course_EUR_to_RUB
#    
#    def print_info(self):
#        print(f'{self._value} {Currency.suffix_EUR} = {self.__in_rubles} {Currency.suffix_RUB}')
#
#bank_a = USD(50)
#bank_a.convert_to_RUB()
#bank_a.print_info()
#
#print('*' * 40)
#
#bank_b = EUR(50)
#bank_b.convert_to_RUB()
#bank_b.print_info()


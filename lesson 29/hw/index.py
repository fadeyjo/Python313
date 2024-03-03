class Student:
    def __init__(self, surname: str = 'Иванов', name: str = 'Иван', age: int = 16, model: str = 'msi', processor: str = 'Intel core i5', RAM: int = 8):
        self.__surname = surname
        self.__name = name
        self.__age = age
        self.__computer = self.__Computer(model, processor, RAM)
    
    def __str__(self) -> str:
        return f'Фамилия: {self.__surname}\nИмя: {self.__name}\nВозраст: {self.__age}\n{self.__computer}'
    
    class __Computer:
        def __init__(self, model: str, processor: str, RAM: int):
            self.__model = model
            self.__processor = processor
            self.__RAM = RAM
        
        def __str__(self) -> str:
            return f'Модель: {self.__model}\nПроцессор: {self.__processor}\nОперативная память: {self.__RAM}'
        


student = Student('Ечин', 'Илья', )
print(student)
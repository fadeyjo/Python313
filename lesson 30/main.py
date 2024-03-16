class Good:
    def __init__(self, name, weight, price):
        print('Инициализатор Good')
        self.name = name
        self.weight = weight
        self.price = price
        super().__init__()
    
    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')

class Mixin_log:
    ID = 0

    def __init__(self):
        print('Инициализатор Mixin_log')
        Mixin_log.ID += 1
        self.id = Mixin_log.ID
    
    def save_cell_log(self):
        print(f'{self.id} товар был продан')

class Note_book(Good, Mixin_log):
    pass

note_book = Note_book('HP', 1.5, 35000)
note_book.print_info()
note_book.save_cell_log()
import os
import re

class Menu:
    def __init__(self, type_of_menu: str):
        self.__exit_from_menu_flag = False
        self.__type_of_menu = type_of_menu
        self.__titles = []
        self.__menu_items = []
    
    def add_menu_item(self, title_of_menu_item: str, menu_item):
        self.__titles.append(title_of_menu_item)
        self.__menu_items.append(menu_item)
    
    def run_menu(self):
        while not self.__exit_from_menu_flag:
            self.__print_menu()
            command = Validator.input_valid_positive_int_with_up_boundary('Введите номер пункта меню: ', len(self.__titles))
            os.system('cls')
            self.__menu_items[command - 1]()
            os.system('pause')
            os.system('cls')

    def exit_from_menu(self):
        self.__exit_from_menu_flag = True
    
    def __print_menu(self):
        print(self.__type_of_menu)
        for number, title in enumerate(self.__titles):
            print(f'[{number + 1}]\t{title}')

class Data_base:
    def __init__(self, type_of_entity):
        self.__type_of_entity = type_of_entity
        self.__data_base = []
        self.__create_data_base()
    
    def __create_data_base(self):
        quantity_of_clients = Validator.input_valid_positive_int('Введите количество вводимых клиентов: ')
        [self.__data_base.append(self.__type_of_entity()) for i in range(quantity_of_clients)]
    
    def print_data_base(self):
        for number, element in enumerate(self.__data_base):
            print(f'№{number + 1}')
            element.print_self_data()
            print()
    
    def add_new_element(self):
        self.__data_base.append(self.__type_of_entity())
    
    def delete_element(self):
        self.print_data_base()
        number = Validator.input_valid_positive_int_with_up_boundary('Введите номер удаляемой записи: ', len(self.__data_base))
        del self.__data_base[number - 1]

class Client:
    def __init__(self):
        self.__surname = Validator.input_valid_snp('Введите фамилию: ')
        self.__name = Validator.input_valid_snp('Введите имя: ')
        self.__patronimyc = Validator.input_valid_snp('Введите отчество: ')
        self.__age = Validator.input_valid_positive_int_with_down_boundary('Введите возраст: ', 18)
        self.__number_of_pasport = Validator.input_valid_series_of_pasport()
        self.__series_of_pasport = Validator.input_valid_number_of_pasport()
        self.__account_number = Validator.input_valid_account_number()
    
    def print_self_data(self):
        print(f'Фамилия: {self.__surname}')
        print(f'Имя: {self.__name}')
        print(f'Отчество: {self.__patronimyc}')
        print(f'Возраст: {self.__age}')
        print(f'Серия и номер паспорта: {' '.join([str(self.__series_of_pasport), str(self.__number_of_pasport)])}')
        print(f'Номер счёта: {self.__account_number}')

class Validator:
    @staticmethod
    def input_valid_positive_int_with_up_boundary(text_for_input: str, up_boundary: int):
        while True:
            try:
                value = int(input(text_for_input))
                if value < 1 or value > up_boundary:
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите попытку.')
            except Exception:
                print('Невозможный ввод. Повторите Попытку.')
        return value
    
    @staticmethod
    def input_valid_positive_int_with_down_boundary(text_for_input: str, down_boundary: int):
        while True:
            try:
                value = int(input(text_for_input))
                if value < down_boundary:
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите попытку.')
            except Exception:
                print('Невозможный ввод. Повторите Попытку.')
        return value
    
    @staticmethod
    def input_valid_positive_int(text_for_input: str):
        while True:
            try:
                value = int(input(text_for_input))
                if value < 1:
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите попытку.')
            except Exception:
                print('Невозможный ввод. Повторите Попытку.')
        return value
    
    @staticmethod
    def input_valid_snp(text_for_input: str):
        while True:
            value = input(text_for_input)
            expresions = re.findall('[А-Яа-яЁё]', value)
            if len(expresions) == len(value):
                break
            else:
                print('Невозможный ввод. Повторите попытку.')
        return value
    
    @staticmethod
    def input_valid_series_of_pasport():
        while True:
            value = input('Введите серию паспорта: ')
            expresions = re.findall('[0-9]', value)
            if len(expresions) == len(value) == 4:
                break
            else:
                print('Невозможный ввод. Повторите попытку.')
        return int(value)
    
    @staticmethod
    def input_valid_number_of_pasport():
        while True:
            value = input('Введите номер паспорта: ')
            expresions = re.findall('[0-9]', value)
            if len(expresions) == len(value) == 6:
                break
            else:
                print('Невозможный ввод. Повторите попытку.')
        return int(value)
    
    @staticmethod
    def input_valid_account_number():
        while True:
            value = input('Введите номер счёта: ')
            expresions = re.findall('[0-9]', value)
            if len(expresions) == len(value) == 5:
                break
            else:
                print('Невозможный ввод. Повторите попытку.')
        return int(value)

def create_local_data_base_of_clients():
    global data_base_of_clients
    data_base_of_clients = Data_base(Client)
    
def print_local_data_base_of_clients():
    data_base_of_clients.print_data_base()
    
def add_client_to_local_data_base_of_clients():
    data_base_of_clients.add_new_element()
    
def delete_client_from_local_data_base_of_clients():
    data_base_of_clients.delete_element()
    
def output_local_data_base_of_clients_to_JSON_file():
    ...
    
def input_data_base_of_clients_from_JSON_file_to_local_data_base():
    ...
    
def redact_course_of_ruble_about_dollar():
    ...
    
def redact_course_of_ruble_about_euro():
    ...
    
def exit_from_administrator_menu():
    ...

administrator_menu = Menu('Меню администратора.')
administrator_menu.add_menu_item('Создать локальную базу данных клиентов банка.', create_local_data_base_of_clients)
administrator_menu.add_menu_item('Вывести базу данных.', print_local_data_base_of_clients)
administrator_menu.add_menu_item('Добавить нового клиента в локальную базу данных', add_client_to_local_data_base_of_clients)
administrator_menu.add_menu_item('Удалить клиента из локальной базы данных.', delete_client_from_local_data_base_of_clients)
administrator_menu.add_menu_item('Выгрузить локальную базу данных в файл output_data_base.json.', output_local_data_base_of_clients_to_JSON_file)
administrator_menu.add_menu_item('Загрузить базу данных из файла input_data_base.json в локальную базу данных.', input_data_base_of_clients_from_JSON_file_to_local_data_base)
administrator_menu.add_menu_item('Изменить курс рубля по отношению к доллару.', redact_course_of_ruble_about_dollar)
administrator_menu.add_menu_item('Изменить курс рубля по отношению к евро.', redact_course_of_ruble_about_euro)
administrator_menu.add_menu_item('Выход из меню.', administrator_menu.exit_from_menu)
administrator_menu.run_menu()
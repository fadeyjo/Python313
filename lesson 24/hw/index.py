import os
import xml.etree.ElementTree as ET

class Menu:
    def __init__(self):
        self.__titles = []
        self.__actions = []
    
    exit_flag = False
    
    def add_menu_item(self, title, action):
        self.__titles.append(title)
        self.__actions.append(action)
    
    def run_menu(self):
        self.__print_menu()
        while True:
            try:
                command = int(input('Введите команду: '))
                if command < 1 and command > len(self.__titles):
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите ввод.')
            except Exception:
                print('Такого пункта меню не существует. Повторите ввод.')
        os.system('cls')
        self.__actions[command - 1]()
        os.system('pause') 
        os.system('cls')
        if not(self.exit_flag):
            self.run_menu()
    
    def __print_menu(self):
        for title in self.__titles:
            print(title)

class Car:
    def __init__(self, car = False):
        if car == False:
            self.__model = input('Введите название модели: ')
            while True:
                try:
                    self.__year_of_release = int(input('Введите год выпуска: '))
                    if not(1885 <= self.__year_of_release <= 2024): #года выпуска обусловлены выпусками самых первых автомобилями в мире и  автомобилями на текущий, 2024, год
                        raise Exception
                    break
                except ValueError:
                    print('Некорректный ввод. Повторите попытку.')
                except Exception:
                    print('Недопустимый год выпуска. Повторите попытку.')
            self.__manafacturer = input('Введите производителя: ')
            while True:
                try:
                    self.__engine_power = float(input('Введите мощность двигателя (в лошадиных силах): '))
                    if not(0.75 <= self.__engine_power <= 1500): #числа обусловлены самыми слабым и мощным двигателями автомобилей на   данный момент
                        raise Exception
                    break
                except ValueError:
                    print('Некорректный ввод. Повторите попытку.')
                except Exception:
                    print('Недопустимая мощность автомобиля. Повторите попытку.')
            self.__color = input('Введите цвет машины: ')
            while True:
                try:
                    self.__price = float(input('Введите цену (в рублях): '))
                    if self.__price < 25000:
                        raise Exception
                    break
                except ValueError:
                    print('Некорректный ввод. Повторите попытку.')
                except Exception:
                    print('Недопустимая цена автомобиля. Повторите попытку.')
        else:
            for appanage in car:
                if appanage.tag == '__model':
                    self.__model = appanage.text
                    continue
                if appanage.tag == '__year_of_release':
                    self.__year_of_release = int(appanage.text)
                    continue
                if appanage.tag == '__manafacturer':
                    self.__manafacturer = appanage.text
                    continue
                if appanage.tag == '__engine_power':
                    self.__engine_power = float(appanage.text)
                    continue
                if appanage.tag == '__color':
                    self.__color = appanage.text
                    continue
                if appanage.tag == '__price':
                    self.__price = float(appanage.text)
    
    def print_self_data(self):
        print(f'Модель: {self.__model}')
        print(f'Год выпуска: {self.__year_of_release} год')
        print(f'Производитель: {self.__manafacturer}')
        print(f'Мощность двигателя: {self.__engine_power} л.с.')
        print(f'Цвет: {self.__color}')
        print(f'Цена: {self.__price} (рублей)')
    
    def get_model(self):
        return self.__model
    
    def get_release_year(self):
        return self.__year_of_release
    
    def get_manufacturer(self):
        return self.__manafacturer
    
    def get_engine_power(self):
        return self.__engine_power
    
    def get_color(self):
        return self.__color
    
    def get_price(self):
        return self.__price
    
    def get_appanages(self):
        return [('__model', self.get_model), ('__year_of_release', self.get_release_year), ('__manafacturer', self.get_manufacturer), ('__engine_power', self.get_engine_power), ('__color', self.get_color), ('__price', self.get_price)]

class Data_base:
    def __init__(self, type_of_data_base, input_file_name = ""):
        self.__data_base = []
        self.__type_of_data_base = type_of_data_base
        if input_file_name:
            self.input_file_name = input_file_name
            self.in_put_data_base()
        else:
            self.__create_data_base()
        self.__isEmpty = False
        
    def __create_data_base(self):
        while True:
            try:
                quantity_of_elements = int(input('Введите количество автомобилей: '))
                if quantity_of_elements < 1:
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите попытку.')
            except Exception:
                print('Недопустимое количество записей. Повторите попытку.')
        for i in range(quantity_of_elements):
            self.__data_base.append(self.__type_of_data_base())
            print()

    def add_record_to_data_base(self):
        self.__data_base.append(self.__type_of_data_base())
    
    def delete_record_from_data_base(self):
        self.print_data()
        while True:
            try:
                number = int(input('Введите номер удаляемой записи: '))
                if number < 1 or number > len(self.__data_base):
                    raise Exception
                break
            except ValueError:
                print('Некорректный ввод. Повторите попытку.')
            except Exception:
                print('Недопустимый номер записи.')
        del self.__data_base[number - 1]
        print('Запись удалена.')
    
    def print_data(self):
        for element in enumerate(self.__data_base):
            print(f'№{element[0] + 1}')
            element[1].print_self_data()
            print()
    
    def out_put_data_base(self, line, file_name):
        root = ET.Element('Database')
        for element in self.__data_base:
            item = ET.SubElement(root, line)
            for appanage in element.get_appanages():
                sub_item = ET.SubElement(item, appanage[0])
                sub_item.text = str(appanage[1]())
        with open(file_name, 'wb') as file_xml:
            file_xml.write(ET.tostring(root))
        print(f'Локальная база данных выгружена в файл {file_name}.')
    
    def in_put_data_base(self):
        tree = ET.parse(self.input_file_name)
        root = tree.getroot()
        for car in root:
            self.__data_base.append(self.__type_of_data_base(car))
        print('База данных успешно считалась из файла input.xml.')
        

################################################

def exists_in_globals(identificator):
    return identificator in globals()

def create_data_base_of_cars():
    if exists_in_globals('data_base_of_cars'):
        print('Локальная база данных непустая.')
    else:
        global data_base_of_cars
        data_base_of_cars = Data_base(Car)

def add_car_to_data_base():
    if exists_in_globals('data_base_of_cars'):
        data_base_of_cars.add_record_to_data_base()
    else:
        print('Локальная база данных пустая.')

def delete_car_from_data_base():
    if exists_in_globals('data_base_of_cars'):
        data_base_of_cars.delete_record_from_data_base()
    else:
        print('Локальная база данных пустая.')

def print_data_base():
    if exists_in_globals('data_base_of_cars'):
        data_base_of_cars.print_data()
    else:
        print('Локальная база данных пустая.')

def out_put_data_base_of_cars():
    if exists_in_globals('data_base_of_cars'):
        data_base_of_cars.out_put_data_base('Car', 'output.xml')
    else:
        print('Локальная база данных пустая.')

def in_put_data_base_of_cars():
    if exists_in_globals('data_base_of_cars'):
        print('Локальная база данных непустая.')
    else:
        global data_base_of_cars
        data_base_of_cars = Data_base(Car, 'input.xml')

def clear_data_base_of_car():
    if exists_in_globals('data_base_of_cars'):
        global data_base_of_cars #без повторного объявления глобальной перемнной не удаляет переменную
        del data_base_of_cars
    else:
        print('Локальная база данных уже пустая.')

def exit_from_menu():
    Menu.exit_flag = True

menu = Menu()
menu.add_menu_item('[1]    Создать локальную базу данных автомобилей.', create_data_base_of_cars)
menu.add_menu_item('[2]    Добавить атомобиль в локальную базу данных.', add_car_to_data_base)
menu.add_menu_item('[3]    Удалить автомобиль из локальной базы данных.', delete_car_from_data_base)
menu.add_menu_item('[4]    Вывести локальную базу данных.', print_data_base)
menu.add_menu_item('[5]    Выгрузить локальную базу данных в файл output.xml.', out_put_data_base_of_cars)
menu.add_menu_item('[6]    Выгрузить базу данных из файла input.xml в локальную базу данных.', in_put_data_base_of_cars)
menu.add_menu_item('[7]    Очистить локальную базу данных.', clear_data_base_of_car)
menu.add_menu_item('[8]    Выход.', exit_from_menu)
menu.run_menu()
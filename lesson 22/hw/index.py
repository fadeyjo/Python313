'''Сначала идёт создание файла, далее его считывание, затем строки меняются местами.'''

import os

with open('input.txt', 'w') as file_writer:
    while True:
        try:
            quantity = int(input('Сколько строк вы хотите ввести: '))
            if quantity < 2:
                raise Exception
            break
        except ValueError:
            print('Неккоректный ввод. Повторите попытку.')
        except Exception:
            print('Недопустимое количество строк. Повторите попытку.')
    file_writer.write('\n'.join([input(f'Строка {i + 1}: ') for i in range(quantity)]))

os.system('cls')
print('Файл создан.')
try:
    with open('input.tdxt', 'r') as file_reader:
        data = file_reader.read()
        print(f'Содержимое введённого файла:')
        print(data)
        data = data.split('\n')
        print('Введите номера строк, которые вы хотите поменять местами: ')
        while True:
            try:
                number_of_first_line = int(input('Номер первой строки: '))
                if number_of_first_line < 1 or number_of_first_line > len(data):
                    raise Exception
                break
            except ValueError:
                print('Неккоректный ввод. Повторите попытку.')
            except Exception:
                print('Недопустимый номер строки. Повторите попытку.')
        while True:
            try:
                number_of_second_line = int(input('Номер второй строки: '))
                if number_of_second_line < 1 or number_of_second_line > len(data) or number_of_second_line == number_of_first_line:
                    raise Exception
                break
            except ValueError:
                print('Неккоректный ввод. Повторите попытку.')
            except Exception:
                print('Недопустимый номер строки. Повторите попытку.')
        buffer = data[number_of_first_line - 1]
        data[number_of_first_line - 1], data[number_of_second_line - 1] = data[number_of_second_line - 1], buffer
        with open('input.txt', 'w') as file_writer:
            file_writer.write('\n'.join(data))
except FileNotFoundError:
    print('Файл не найден.')
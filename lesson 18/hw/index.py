while True:
    try:
        line = input('Введите строку: ')
        first_index = line.index('h')
        second_index = line.rindex('h')
        if first_index == second_index:
            raise Exception
        break
    except ValueError:
        print('Некорректный ввод. Отсутствует буква h.')
    except Exception:
        print('Некорректный ввод. В строке только одна буква h.')

print(f'Результат: {line[:first_index + 1] + line[second_index - 1:first_index:-1] + line[second_index:]}')
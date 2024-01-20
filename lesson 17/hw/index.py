while True:
    try:
        first_zone = int(input('Введите нижнюю границу: '))
        second_zone = int(input('Введите верхнюю границу: '))
        if first_zone >= second_zone or first_zone < 0 or second_zone < 0:
            raise Exception
        break
    except (ValueError, Exception):
        print('Некорректный ввод. Потворите попытку.')

print(*[chr(code) for code in range(first_zone, second_zone + 1)])
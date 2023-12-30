while True:
    try:
        quantity_of_students = int(input('Количество студентов: '))
        if quantity_of_students < 1:
            raise Exception
        break
    except (ValueError, Exception):
        print('Некорректный ввод. Потворите попытку.')

students = dict()
for i in range(quantity_of_students):
    print(i + 1, 'студент:')
    surname = input('Фамилия: ')
    name = input('Имя: ')
    while True:
        try:
            points = int(input('Балл: '))
            if points < 0 or points > 100:
                raise Exception
            break
        except (ValueError, Exception):
            print('Некорректный ввод. Потворите попытку.')
    students[name] = dict()
    students[name]['surname'] = surname
    students[name]['points'] = points

print('--------------------------------------------------')

midle_of_points = sum([students[name]['points'] for name in students]) / len(students)
print('Средний балл: ', midle_of_points)

print('Студенты с баллом выше среднего: ')
for name in students:
    if students[name]['points'] > midle_of_points:
        print(students[name]['surname'], name)
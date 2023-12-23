my_dict = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New York'
}

new_my_dict = {
    list(my_dict.keys())[0]: list(my_dict.values())[0],
    list(my_dict.keys())[2]: list(my_dict.values())[2]
}

del my_dict[list(my_dict.keys())[0]]
del my_dict[list(my_dict.keys())[1]]

print('Старый словарь:', my_dict)
print('Новый словарь:', new_my_dict)

line = input('Введите строку: ')
vowels = set('аеёиоуяэюы')
count_of_vowels = 0
for letter in line:
    if letter in vowels:
        count_of_vowels += 1
print('Количество гласных в строке:', count_of_vowels)

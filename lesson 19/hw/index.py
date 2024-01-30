import re

addresses = ['123456@i.ru', '123_456@ru.name.ru', 'login@i.ru', 'логин-1@i.ru', 'login.3@i.ru', 'login.3-67@i.ru', '1login@ru.name.ru']

pattern = r'[a-zA-Z0-9-_.а-яА-ЯЁё]{1,64}@[a-zA-Z0-9-.]{1,255}'

#Информация о синтаксисе адреса электронной почты была взята из https://en.wikipedia.org/wiki/Email_address и https://journalovirus.ru/skolko-chastey-v-adrese-elektronnoy-pochty-razbiraemsya-shag-za-shagom/ (Я не уверен насчёт использования русского алфавита)

print('Корректные адреса электронных почт:', re.findall(pattern, ' '.join(addresses)))
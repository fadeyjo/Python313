from jinja2 import Template

my_template = Template('Мне {{ age * 2 }} лет, меня зовут {{ name.upper() }}.')
print(my_template.render(name='Егор', age=19))

my_template1 = Template('''{% raw %}Меня зовут {{ name }} #экранирование
Мой возраст {{ age }}{% endraw %}''')
print(my_template1.render(name='Илья', age=19))

link = '''В браузере будет просто ссылка, а должно быть
<a href="#">Ссылка</a>'''
my_template2 = Template('{{ link | e}}')  #таким образом устанавливаются флаги, e (escape) - экранирование
print(my_template2.render(link=link))

cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 2, 'city': 'Kaluga'},
          {'id': 10, 'city': 'Kirov'}]
link1 = '''<select name="cities">
{% for city in cities -%}
{% if city['id'] > 5 -%}
    <option value="{{ city['id'] }}">{{ city['city'] }}</option>"
{% endif -%}
{% endfor -%}
</select>'''
my_template3 = Template(link1)
print(my_template3.render(cities=cities))

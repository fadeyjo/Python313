#print('sum(2)(4)(6)', (lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))
players = [
    {
        'name': 'Антон',
        'surname': 'Бирюков',
        'rate': 9
    },
    {
        'name': 'Алексей',
        'surname': 'Бодня',
        'rate': 10
    },
    {
        'name': 'Фёдор',
        'surname': 'Сидоров',
        'rate': 4
    },
    {
        'name': 'Михаид',
        'surname': 'Семёнов',
        'rate': 6
    }
]

print(sorted(players, key = lambda player: player['surname']))
print(sorted(players, key = lambda player: player['rate']))
print(sorted(players, key = lambda player: player['rate'], reverse = True))
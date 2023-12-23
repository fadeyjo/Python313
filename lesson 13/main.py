a = {
    'first': {
        1: 'one',
        2: 'two',
        3: 'three'
    },
    'second': {
        4: 'four',
        5: 'five'
    }
}

for key in a:
    for key1 in a[key]:
        print(key1)
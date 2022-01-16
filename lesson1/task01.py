user_input = []

for i in range(3):
    user_input.append(int(input('Введите время в секундах: ')))

for i in user_input:
    dd = i // 86400
    hh = i % 86400 // 3600
    mm = i % 3600 // 60
    ss = i % 60

    print(f'{i} сек. =', end=' ')

    if dd > 0:
        print(f'{dd} д.', end=' ')
    if hh > 0:
        print(f'{hh} ч.', end=' ')
    if mm > 0:
        print(f'{mm} мин.', end=' ')
    print(f'{ss} сек.', end='\n')


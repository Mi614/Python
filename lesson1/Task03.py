ending_word = ['процентов', 'процента', 'процент']

for prc in range(1, 101):
    i = prc % 10
    if i == 0 or i >= 5 or 10 < prc < 20:
        m = 0
    elif 1 < i < 5:
        m = 1
    else:
        m = 2
    print(f'{prc} {ending_word[m]}')

price_list = [57.8, 46.51, 97, 456.12, 4164.15, 794.57, 5.05]

print(f'Id списка "price_list": {id(price_list)}')
price_list.sort()

for price in price_list:
    print(f'{int(price):02d} руб. {int(price % int(price) * 100):02d} коп.', end=', ')
print('\n')

print(price_list)
print(f'Id списка "price_list" после сортировки : {id(price_list)}')

new_price_list = price_list
new_price_list.reverse()

print(new_price_list)

for el in reversed(range(5)):
    print(f'{int(new_price_list[el]):02d} руб. {int(new_price_list[el] % int(new_price_list[el]) * 100):02d} коп.', end=' ')

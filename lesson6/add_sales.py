from sys import argv


def add_sales(args):
    if len(args) > 1:
        with open('bakery.csv', 'a', encoding='utf-8') as f:
           for i in range(1, len(args)):
               el = round(float(args[i]), 2)
               f.write(str(el) + '\n')
        return print('ok')
    else:
        return print('Вы ничего не добавили!!!')


run = add_sales(argv)

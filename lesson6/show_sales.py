from sys import argv
import linecache as lc

def show_sales(args):
    if len(args) == 2:
        el = lc.getline('bakery.csv', int(args[1]))
        lc.clearcache()
        return print(el)

    elif len(args) > 2:
        for i in range(int(args[1]), int(args[2])):
            el = lc.getline('bakery.csv', i)
            lc.clearcache()
            print(el, end='')
        return print('end')


run = show_sales(argv)

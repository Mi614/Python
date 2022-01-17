mylist = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, el in enumerate(mylist):
    if el.isdigit():
        el = el.zfill(2)
    if el.startswith('+') or el.startswith('-'):
        el = el.zfill(3)
    mylist[i] = el
print(mylist)

for el in mylist.copy():
    y = 0
    for d in el:
        if d.isdigit():
            y = 1
    if y == 1:
        mylist.append('"')
        mylist.append(el)
        mylist.append('"')
    else:
        mylist.append(el)
    mylist.remove(el)

print(mylist)

my_str = ' '.join(mylist)

for i in my_str.split():
    if i.isdigit() or i.startswith('+') or i.startswith('-'):
        my_str = my_str.replace(f' {i} ', i)

print(my_str)

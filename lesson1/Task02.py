task_list = []
sum_a = 0
sum_b = 0

for i in range(1, 1000, 2):
    task_list.append(i ** 3)

for n, el in enumerate(task_list):
    sum_el = 0
    while el:
        m = el % 10
        el //= 10
        sum_el +=m
    if sum_el % 7 == 0:
        sum_a += task_list[n]

for n, el in enumerate(task_list):
    sum_el = 0
    el += 17
    while el:
        m = el % 10
        el //= 10
        sum_el +=m
    if sum_el % 7 == 0:
        sum_b += task_list[n]

print(sum_a)
print(sum_b)

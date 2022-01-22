def thesaurus_adv(*kwargs):
    my_list = {x.split()[1][0] for x in kwargs}
    my_dict = {i: {x.split()[0][0]: [] for x in kwargs if x.split()[1][0] == i} for i in my_list}
    for x in kwargs:
        my_dict[x.split()[1][0]][x.split()[0][0]].append(x)
    return my_dict

print(thesaurus_adv("Петр Алексеев", "Илья Иванов", "Анна Савельева", "Вадим Васильев", "Иван Сергеев", "Инна Серова"))

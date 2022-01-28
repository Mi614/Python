from itertools import zip_longest

tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена', 'Мария',
        'Тимур', 'Евгений'
        ]

klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
        ]


def list_by_class(tut, klas):
    for i in list(zip_longest(tut, klas, fillvalue=None)):
        yield i


get_list_klass = list_by_class(tutors, klasses)
print(list(get_list_klass))

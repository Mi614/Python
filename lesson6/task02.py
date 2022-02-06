from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as user:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        list = zip_longest(user, hobby, fillvalue=None)

        with open('answer.txt', 'w', encoding='utf-8') as answer:
            for el in list:
                print(f'{str(el[0]).strip()} {str(el[1]).strip()}', file=answer)

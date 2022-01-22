from random import randrange
from random import choice


def get_jokes(number, repeat=False):
    """
    :param number: количество генераций (max "5")
    :param repeat: "True" -> Слова в шутках будут повтаряться,
    :return: Возращает "List" состоящий из фраз
    """

    print(repeat)
    number = int(number)
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    send = []
    if number > 5:
        return print('5 максимальное колличество')

    for joke in range(number):
        if repeat:          # генерация с повторяющимися словами
            send.append('{0} {1} {2}'.format(choice(nouns), choice(adverbs), choice(adjectives))
                        )
        else:               # элементы генерируються без повторов
            send.append(
                '{0} {1} {2}'.format(nouns.pop(randrange(0, len(nouns))), adverbs.pop(randrange(0, len(adverbs))),
                                     adjectives.pop(randrange(0, len(adjectives))))
                )
    return print(send)


jokes = get_jokes(number=input("Введите число от 1 до 5:"),
                  repeat=True if input('повторять слова? (y/n):') == 'y' else False
                  )

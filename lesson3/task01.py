num_dict = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шеть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять'}


def num_translate(num_eng):
    num = (lambda x: num_dict.get(x))(num_eng.lower())
    if num_eng.istitle():
        return num.capitalize()
    else:
        return num


user_input = num_translate(num_eng=input('Введите число: '))
print(user_input)

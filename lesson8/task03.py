from functools import wraps


def val_checker(el):
    def _val_checker(func):
        cache = {}

        @wraps(func)
        def wrapper(num):
            nonlocal cache
            key = str(num)
            if not el(num):
                raise ValueError(f'Wrong value: {num}')
            if key not in cache:
                cache[key] = type(num)
            return func.__name__, cache
        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(y):
   return y ** 3


a = calc_cube(-5)
a = calc_cube(5)
print(a)

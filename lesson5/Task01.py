def gen_odd_num(num):
    for i in range(1, num+1, 2):
        yield i


odd_to_15 = gen_odd_num(15)
print(next(odd_to_15))
print(type(odd_to_15))

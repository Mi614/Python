def my_odd_gen(num):
    return (i for i in range(1, num+1, 2))


run = my_odd_gen(15)
print(type(run))

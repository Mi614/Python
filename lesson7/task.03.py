import os
import json
from collections import Counter
from collections import namedtuple


print(os.getcwd())
dir_ph = os.getcwd()

def get_stat_folder(args):
    my_list = [100, 1000, 10000, 100000]
    my_dict = {x: [0] for x in my_list}
    for i in os.walk(args):
        for el in i[-1]:
            f_path = os.path.join(i[0], el)
            f_size = os.stat(f_path).st_size
            f_ext = os.path.splitext(f_path)[-1]
            key = my_list[len(str(f_size)) - 2] if len(str(f_size)) > 2 else my_list[0]
            if f_ext not in my_dict[key]:
                my_dict[key].append(f_ext)
            my_dict[key][0] += 1
    print(my_dict)

    print(os.path.basename(args))
    with open(f'{os.path.basename(args)}_summer.json', 'w') as f:
        dum_dict = {x: (y[0], y[1::]) for x, y in my_dict.items()}
        json.dump(dum_dict, f)
    return print('Done!')


run = get_stat_folder(dir_ph)

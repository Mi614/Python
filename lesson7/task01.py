import os
import yaml


def create_files(files, fold):
    for i in files:
        if type(i) == dict:
            create_dir(i, fold)
            break
        with open(os.path.join(fold, f'{i}'), 'w') as f:
            pass


def create_dir(el, fol=''):
    root = fol
    for key, val in el.items():
        folder = os.path.join(root, key)
        if not os.path.exists(key):
            os.mkdir(folder)
        if type(val) == dict:
            create_dir(val, folder)
        else:
            create_files(val, folder)


with open('config.yaml', 'r') as conf_f:
    my_dict = yaml.full_load(conf_f)

try:
    run = create_dir(my_dict)
except (FileExistsError) as e:
    print(e)
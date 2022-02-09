import os
import shutil

folder = 'my_project'
templ_folder = os.path.join(folder, 'templates')
if not os.path.exists(os.path.join(folder, 'templates')):
    os.mkdir(templ_folder)
    print(f'директория {templ_folder} создана!')

for i in os.walk(folder):
    for el in i[-1]:
        if el.endswith('.html'):
            src_r = os.path.join(i[0], el)
            dst_r = os.path.join(templ_folder, src_r.split('\\')[-2])
            if not os.path.exists(dst_r):
                os.mkdir(dst_r)
            shutil.move(src_r, os.path.join(dst_r, el))
            print(f'файл {src_r} перемещен в {dst_r} !')


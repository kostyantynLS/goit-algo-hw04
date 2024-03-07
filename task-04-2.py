'''
Друге завдання
У вас є текстовий файл, який містить інформацію про котів. 
Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
'''

import os, re

def get_cats_info(path_to_cats) -> list:
    cats_id = set()
    resl = list()
    if not os.path.exists(path_to_cats):
        print(f'file {path_to_cats} not exist!')
    else:
        with open(path_to_cats, "r", encoding="utf-8") as cats_file:
            while True:
                lines = cats_file.readline()
                lines = re.sub(r'\s+', ' ', lines)
                lines = lines.strip()
                lines = lines.replace(" ,", ",")
                lines = lines.replace(", ", ",")
                if len(lines)==0:
                    break
                cinfo = dict()
                try:
                    cid, cname, cage = lines.split(',')
                    if not cid in cats_id:
                        cats_id.add(cid)
                        cinfo["id"]=cid
                        cinfo["name"]=cname
                        cinfo["age"]=cage
                        resl.append(cinfo)
                    else:
                        print(f'cat with ID {cid} already added!')
                except:
                    print(f'error at line {lines}')

    return resl

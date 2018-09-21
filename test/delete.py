# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     delete
   Description :
   Author :       'li'
   date：          2018/7/29
-------------------------------------------------
   Change Activity:
                   2018/7/29:
-------------------------------------------------
"""
from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'
des_path = 'F:/dataset/container_dataset/training_data/txt/'
new_path = 'F:/dataset/container_dataset/training_data/new_dataset/'
des_path = get_all_file_from_dir(des_path)
for path in des_path:
    if not path.find('.txt'):
        continue
    with open(path, mode='r', encoding='utf8')as file:
        lines = file.readlines()
        name = path.split('\\')[-1]
        with open(new_path + name, mode='w', encoding='utf8')as f:
            if len(lines) > 0:
                for line in lines:
                    line.split()
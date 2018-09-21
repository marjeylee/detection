# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       'li'
   date：          2018/7/29
-------------------------------------------------
   Change Activity:
                   2018/7/29:
-------------------------------------------------
"""
import shutil

from utility.file_path_utility import get_all_file_from_dir

__author__ = 'li'

img_path = 'F:/dataset/second_label/image/'
annotation_path = 'F:/dataset/second_label/detection_label/'
des_path = 'F:/dataset/second_label/des/'
img_path = get_all_file_from_dir(img_path)
annotation_path = get_all_file_from_dir(annotation_path)


def load_map(img_path):
    map = {}
    for path in img_path:
        name = path.split('\\')[-1].split('.')[0]
        map[name] = path
    return map


img_map = load_map(img_path)
anno_map = load_map(annotation_path)
i = 1
for key in anno_map.keys():
    if key in img_map.keys():
        a_path = anno_map[key]
        i_path = img_map[key]
        shutil.copyfile(a_path, des_path + 'img_' + str(i) + '.txt')
        shutil.copyfile(i_path, des_path + 'img_' + str(i) + '.jpg')
        i = i + 1

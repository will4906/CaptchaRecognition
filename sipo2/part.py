# -*- coding: utf-8 -*-
"""
Created on 2018/3/17

@author: will4906
"""
import os
import shutil

part_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\part'
target_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\target'
last = ''
last_index = 0
for title in os.listdir(part_path):
    t = title.split('_')[0]
    if last == t:
        if last_index < 10:
            shutil.copy(os.path.join(part_path, title), os.path.join(target_path, title))
            last_index += 1
    else:
        last = t
        shutil.copy(os.path.join(part_path, title), os.path.join(target_path, title))
        last_index = 0
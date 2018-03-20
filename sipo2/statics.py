# -*- coding: utf-8 -*-
"""
Created on 2018/3/17

@author: will4906
"""
import os

result_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\result'

char_dict = {}
for result in os.listdir(result_path):
    title = result.split('.')[0]
    for t in title:
        if t == 'O':
            print(title)
        n = char_dict.get(t)
        if n is not None:
            char_dict.__setitem__(t, n + 1)
        else:
            char_dict.__setitem__(t, 1)

for i, v in char_dict.items():
    print(i, ':', v)
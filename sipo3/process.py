# -*- coding: utf-8 -*-
"""
Created on 2018/3/21

@author: will4906
"""
import numpy as np
import os
import shutil

from PIL import Image
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier

tmp_dict = {}
split_part = [(6, 18), (19, 31), (33, 45), (45, 57)]
train_x = []
train_y = []
for file in os.listdir('label'):
    image = np.asarray(Image.open(os.path.join('label', file)).convert('L'))
    image = (image > 135) * 255
    for i in range(4):
        t = tmp_dict.get(file[i])
        if t is None:
            tmp_dict.__setitem__(file[i], 1)
        else:
            tmp_dict.__setitem__(file[i], t + 1)
        t = tmp_dict.get(file[i])
        if t >= 7:
            break
        else:
            letter = image[:, split_part[i][0] : split_part[i][1]]
            train_x.append(letter.reshape(letter.shape[0] * letter.shape[1]))
            train_y.append(file[i])


def split_letters(image):
    image = (image > 135) * 255
    letters = [image[:, 6:18].reshape(20*12), image[:, 19:31].reshape(20*12), image[:, 33:45].reshape(20*12), image[:, 45:57].reshape(20*12)]
    return letters


# knn = KNeighborsClassifier()
# knn.fit(np.asarray(train_x), np.asarray(train_y))
# joblib.dump(knn, 'sipo3.job')

knn = joblib.load('sipo3.job')
for file in os.listdir('source'):
    line = ''
    for c in knn.predict(split_letters(np.asarray(Image.open(os.path.join('source', file)).convert('L')))):
        line += c
    print(file, eval(line))

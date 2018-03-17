# -*- coding: utf-8 -*-
"""
Created on 2018/3/17

@author: will4906
"""
import numpy as np
import os

from PIL import Image
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier

target_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\target'
part_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\part'


def load_dataset():
    X = []
    y = []

    for title in os.listdir(target_path):
        pix = np.asarray(Image.open(os.path.join(target_path, title)).convert('L'))
        X.append(pix.reshape(20 * 15))
        y.append(title.split('_')[0])

    # print(X)
    X = np.asarray(X)
    y = np.asarray(y)
    return X, y


def check_everyone(model):
    pre_list = []
    y_list = []
    for title in os.listdir(part_path):
        pix = np.asarray(Image.open(os.path.join(part_path, title)).convert('L'))
        pix = pix.reshape(20 * 15)
        pre_list.append(pix)
        y_list.append(title.split('_')[0])
    pre_list = np.asarray(pre_list)
    y_list = np.asarray(y_list)
    result_list = model.predict(pre_list)
    acc = 0
    for i in result_list == y_list:
        # print(i, type(i))
        if i == np.bool(True):
            acc += 1
    print(acc, acc / len(result_list))


X, y = load_dataset()
knn = KNeighborsClassifier()
knn.fit(X, y)
joblib.dump(knn, 'sipo_knn2.job')
check_everyone(knn)
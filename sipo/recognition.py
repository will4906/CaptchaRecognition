# -*- coding: utf-8 -*-
"""
Created on 2017/3/19

@author: will4906
"""

import sys
import pickle

from PIL import Image
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def load_dataset():
    X = []
    y = []

    for i in range(70):
        path = "./train/%d%d.png" % (i / 7, i % 7)
        pix = np.array(Image.open(path).convert("L"))
        # print(pix.reshape(8*20).shape)
        X.append(pix.reshape(9*13))
        y.append(int(i / 7))
    return np.array(X), np.array(y)


def split_letters(path):
    pix = np.array(Image.open(path).convert('L'))
    # threshold image
    pix = (pix > 135) * 255

    split_parts = [
        [7, 16],
        [20, 29],
        [33, 42],
        [46, 55]
    ]
    letters = []
    for part in split_parts:
        letter = pix[7:, part[0]: part[1]]
        letters.append(letter.reshape(9*13))
    return letters


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python recognizer.py <image_filename>")

    letters = split_letters(sys.argv[1])

    X, y = load_dataset()
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)
    with open('sipoknn.pkl', 'wb') as f:
        pickle.dump(knn, f)

    print(knn.predict(letters))
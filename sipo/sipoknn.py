# -*- coding: utf-8 -*-
"""
Created on 2017/3/19

@author: will4906
"""
import pickle
import numpy as np
import os

from PIL import Image


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
    sipoknn = None
    with open('sipoknn.pkl', 'rb') as f:
        sipoknn = pickle.load(f)


    for test in os.listdir('./test'):
        letters = split_letters('./test/' + test)
        print(sipoknn.predict(letters))

# -*- coding: utf-8 -*-
"""
Created on 2017/3/19

@author: will4906
"""

import numpy as np
import uuid
import os

from PIL import Image


def splitSingle(filename):
    pix = np.array(Image.open(filename).convert('L'))
    # threshold image
    pix = (pix > 135) * 255

    split_parts = [
        [7, 16],
        [20, 29],
        [33, 42],
        [46, 55]
    ]

    for part in split_parts:
        letter = pix[7:, part[0]: part[1]]
        im = Image.fromarray(np.uint8(letter))

        save_path = './letters/' + str(uuid.uuid4()) + '.png'
        print('\t', save_path)
        # im.save(save_path)


def splitAndSave(path):
    path = './source/' + path
    pix = np.array(Image.open(path).convert('L'))
    # threshold image
    pix = (pix > 135) * 255

    split_parts = [
        [7, 16],
        [20, 29],
        [33, 42],
        [46, 55]
    ]

    for part in split_parts:
        letter = pix[7:, part[0]: part[1]]
        im = Image.fromarray(np.uint8(letter))
        save_path = './letters/' + str(uuid.uuid4()) + '.png'
        print('\t', save_path)
        im.save(save_path)


if __name__ == '__main__':
    # splitSingle('test1.png')
    im_paths = filter(lambda fn: os.path.splitext(fn)[1].lower() == '.png',
    os.listdir('./source'))

    for im_path in im_paths:
        print(im_path)
        splitAndSave(im_path)



# -*- coding: utf-8 -*-
"""
Created on 2018/3/15

@author: will4906
"""
import uuid

import numpy as np
import os

from PIL import Image, ImageFilter


def image_as_array(image):
    image = np.asarray(image)
    image.flags['WRITEABLE'] = True
    return image


def convert_to_pure_black_white(image):
    width = image.shape[1]
    height = image.shape[0]
    image[0] = 255
    for line in image:
        line[0] = 255
        line[-1] = 255
    image[-1] = 255
    for w in range(width):
        for h in range(height):
            if image[h][w] < 237:
                image[h][w] = 0
            else:
                image[h][w] = 255
    image2 = image[:, 13:75]
    return image2


def split_letters(image):
    letters = [image[:, : 15], image[:, 15: 30], image[:, 30: 45], image[:, 45: 60]]
    return letters


def remove_noise_line(image):
    width = image.shape[1]
    height = image.shape[0]
    for w in range(width):
        count = 0
        for h in range(height):
            if image[h][w] < 100:
                count += 1
            else:
                if 2 > count > 0:
                    for c in range(count):
                        image[h - c - 1][w] = 255
                count = 0

    for h in range(height):
        count = 0
        for w in range(width):
            if image[h][w] < 100:
                count += 1
            else:
                if 2 > count > 0:
                    for c in range(count):
                        image[h][w - c - 1] = 255
                count = 0
    return image


def check_domain(image):
    width = image.shape[1]
    height = image.shape[0]
    for w in range(width):
        count = 0
        for h in range(height):
            if image[h][w] < 100:
                count += 1
            else:
                if 2 > count > 0:
                    for c in range(count):
                        image[h - c - 1][w] = 255
                count = 0


part_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\part'
dir_path = r'G:\Core\python\workspace\CaptchaRecognition\sipo2\result'
for file in os.listdir(dir_path):
    file_name = file.split('.')[0]
    file_path = os.path.join(dir_path, file)
    image = Image.open(file_path)
    pix = image_as_array(image.convert('L'))

    pix = convert_to_pure_black_white(pix)
    # Image.fromarray(pix).show()
    letters = split_letters(pix)
    for i, l in enumerate(letters):
        try:
            l = remove_noise_line(l)
            image2 = Image.fromarray(l)
            # image2 = image2.filter(ImageFilter.MaxFilter)
            image2.save(os.path.join(part_path, file_name[i] + '_' + str(uuid.uuid4())+ '.png'))
        except Exception as e:
            print(file)
            print(e)


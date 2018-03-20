# -*- coding: utf-8 -*-
"""
Created on 2018/3/20

@author: will4906
"""

from PIL import Image

image = Image.open('doc/0AUA.png')

image = image.convert('L')

import numpy as np

image = np.asarray(image)
print(image.shape)


def convert_to_pure_black_white(image):
    image2 = (image > 237) * 255
    width = image2.shape[1]
    height = image2.shape[0]
    image2[0] = 255
    for line in image2:
        line[0] = 255
        line[-1] = 255
    image2[-1] = 255
    for w in range(width):
        for h in range(height):
            if image2[h][w] < 237:
                image2[h][w] = 0
            else:
                image2[h][w] = 255
    image2 = image2[:, 13:75]
    return image2


image = convert_to_pure_black_white(image)

# image = Image.fromarray(image).convert('RGB')
# image.show()
# image.save('0AUA_2.png')


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


image = remove_noise_line(image)
image = Image.fromarray(image).convert('RGB')
image.show()
image.save('0AUA_3.png')
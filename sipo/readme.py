# -*- coding: utf-8 -*-
"""
Created on 2018/3/20

@author: will4906
"""
from PIL import Image

image = Image.open('doc/9381.png')

image = image.convert('L')

import numpy as np

image = np.asarray(image)
print(image.shape)

image = (image > 135) * 255

image = Image.fromarray(image).convert('RGB')
image.show()
image.save('9381_2.png')
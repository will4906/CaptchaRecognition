# -*- coding: utf-8 -*-
"""
Created on 2018/3/21

@author: will4906
"""
import os
import requests
import uuid
import shutil

# for i in range(1, 500):
#     resp = requests.get('http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml')
#     file_name = str(uuid.uuid4()) + '.png'
#     with open('source/' + file_name, 'wb') as f:
#         print(file_name)
#         f.write(resp.content)

for i, file in enumerate(os.listdir('source')):
    if i < 100:
        shutil.move(os.path.join('source', file), os.path.join('test', file))
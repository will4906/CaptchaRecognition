# -*- coding: utf-8 -*-
"""
Created on 2018/3/15

@author: will4906
"""

import requests
import uuid

for i in range(1, 500):
    resp = requests.get('http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml')
    file_name = str(uuid.uuid4()) + '.png'
    with open('source/' + file_name, 'wb') as f:
        print(file_name)
        f.write(resp.content)
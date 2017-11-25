# -*- coding: utf-8 -*-
"""
Created on 2017/3/19

@author: will4906
"""
import requests
import uuid

for i in range(1, 200):
    resp = requests.get('http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml')
    with open('source/' + str(uuid.uuid4()) + '.png', 'wb') as f:
        f.write(resp.content)
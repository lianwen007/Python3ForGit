# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:33:47 2017

@author: Administrator
"""

import datetime

ndate=datetime.datetime.now() + datetime.timedelta(days=-1)

print(ndate.strftime('%Y%m%d'))
# -*- coding: utf-8 -*-
'''
Created on 2016��9��22��
@author: su
'''
import time
import datetime
timeArray = time.localtime(int(time.time()))
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
start = datetime.date(2012,10,16)
timeArray = time.localtime(int(time.time()))
now = datetime.date(timeArray.tm_year,timeArray.tm_mon,timeArray.tm_mday)
days = now-start
print days.days
# -*- coding: utf-8 -*-
'''
Created on 2016��9��18��
@author: su
'''
import argparse
import re
from multiprocessing import Pool
import requests
import bs4
import os
root_url = 'http://wufazhuce.com'
def save_img():
    pass
def get_url(num,string):
    return root_url + '/'+string+'/' +str(num)
def get_img_data(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text,"html.parser")
        
        for meta in soup.select('meta'):
            if meta.get('name') =='description':
                title = meta.get('content')
        for i in soup.select('.one-titulo'):
            titulo = i.get_text().strip()
        imgUrl = soup.find_all('img')[1]['src']
        
        print imgUrl
        print titulo
        print title
        return imgUrl,titulo,title
    except:
        pass
def push_code(num):
    pool = Pool(4)
    url = get_url(num, 'one')
    imgUrl,titulo,title = get_img_data(url)
    file = open('ONE-IMG\[ONE]-'+titulo+'.md', 'w')
    file.write('![one]('+imgUrl+')'+'\n')
    file.write('#'+titulo+'\n')
    file.write(title)
    file.close()
    os.system('git add -A')
    os.system('git commit -m "test"')
    os.system('git push origin master')
if __name__=='__main__':
    push_code(23)
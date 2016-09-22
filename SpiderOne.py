# -*- coding: utf-8 -*-
'''
Created on 2016��9��18��
@author: su
'''
import time
import datetime
from multiprocessing import Pool
import requests
import bs4
import os
root_url = 'http://wufazhuce.com'
todaytime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
        return imgUrl,titulo,title
    except:
        pass
def write_file(num):

    url = get_url(num, 'one')
    try:
        imgUrl,titulo,title = get_img_data(url)
        filename = 'ONE-IMG\\'+titulo+'.md'
        if os.path.exists(filename):
            pass
        else:
            file = open(filename, 'w')
            file.write('![one]('+imgUrl+')'+'\n')
            file.write('#'+titulo+'\n')
            file.write(title)
            file.close()
    except:
        pass

def push_data():
        gitadd = 'git add -A'
        gitcommit = 'git commit -m "'+todaytime+'"'
        gitpush =  'git push origin master'
        os.system(gitadd+' && '+gitcommit+' && ' +gitpush)
if __name__=='__main__':
    pool = Pool(4)
    start = datetime.date(2012,9,15)
    timeArray = time.localtime(int(time.time()))
    now = datetime.date.today()
    days = now -start
    for i in range(1,days.days):
        write_file(i)
    push_data()
    

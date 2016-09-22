# -*- coding: utf-8 -*-
'''
Created on 2016��9��18��
@author: su
'''
#git config core.autocrlf false
import time
import datetime
from multiprocessing import Pool
import requests
import bs4
import os
import pickle
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
def get_article_data(url):
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text,"html.parser")
        for i in soup.select('.comilla-cerrar'):
            cerrar = i.get_text().strip()
        for i in soup.select('.articulo-titulo'):
            titulo = i.get_text().strip()
        for i in soup.select('.articulo-autor'):
            autor = i.get_text().strip()
        for i in soup.select('.articulo-contenido'):
            contenido = i.get_text()
        return cerrar,titulo,autor,contenido
    except:
        pass
def write_article_file(num):
    url = get_url(num, 'article')
    print url
    try:
        cerrar,titulo,autor,contenido = get_article_data(url)
        filename = 'ONE-ESSAY\\'+titulo+'.md'
        file = open(filename, 'w')
        file.write('> '+cerrar+'\n\n')
        file.write('###'+titulo+'\n')
        file.write('####'+autor+'\n')
        file.write(contenido)
        file.close()
    except:
        pass
def write_img_file(num):

    url = get_url(num, 'one')
    try:
        imgUrl,titulo,title = get_img_data(url)
        filename = 'ONE-ESSAY\\'+titulo+'.md'
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
def write_pkl(begin):
    output = open('data.pkl', 'wb')
    pickle.dump(begin,output)
    output.close()
def read_pkl():
    data = 1
    try:
        pkl_file = open('data.pkl', 'rb')
        data = pickle.load(pkl_file)
    except:
        pass
    return data
if __name__=='__main__':
    pool = Pool(4)
    start = datetime.date(2012,9,15)
    timeArray = time.localtime(int(time.time()))
    now = datetime.date.today()
    days = now -start
    begin = read_pkl()
    for i in range(begin,days.days):
        begin = i
        write_img_file(i)
        write_article_file(i)
    write_pkl(begin)
    push_data()
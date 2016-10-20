#!/usr/bin/env python3
# _*_ conding: utf-8 _*_

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='python',
                       charset='utf8')
cur = conn.cursor()

random.seed(datetime.datetime.now())


# 数据库的添加
def store(title, content):
    sql = "insert into scrapy (title, content) values(\"{}\",\"{}\")".format(title, content)
    cur.execute(sql)
    cur.connection.commit()


# scrapy link
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    title = bsObj.find('h1').get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()

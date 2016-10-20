#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root',
                       passwd=None, db='python', charset='utf8')
cur = conn.cursor()


# insert page table
def insertPageIfNotExists(url):
    ssql = "SELECT * FROM pages WHERE url=\"{}\"".format(url)
    cur.execute(ssql)
    if cur.rowcount == 0:
        isql = "INSERT INTO pages (url) VALUES(\"{}\")".format(url)
        cur.execute(isql)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


# insert links table
def insertLink(fromPageId, toPageId):
    ssql = "SELECT * FROM links WHERE fromPageId = {} AND toPageId = {}".format(int(fromPageId), int(toPageId))
    cur.execute(ssql)
    if cur.rowcount == 0:
        isql = "INSERT INTO links(fromPageId, toPageId) VALUES(\"{}\", \"{}\")".format(int(fromPageId), int(toPageId))
        cur.execute(isql)
        conn.commit()


pages = set()


def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            # 遇到一个新页面，加入集合并搜索里面的词条链接
            newPage = link.attrs['href']
            pages.add(newPage)
            print("new page:{}".format(newPage))
            getLinks(newPage, recursionLevel + 1)

getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()

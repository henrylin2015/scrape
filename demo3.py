#!/usr/bin/env python3
# _*_ conding: utf-8 _*_
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print("title:{}".format(bsObj.h1.get_text()))
        print("mw-content-text:{}".format(bsObj.find(id="mw-content-text").
                                          findAll("p")[0]))
        print("ca-edit:{}".format(bsObj.find(id="ca-edit").find("span").
                                  find("a").attrs['href']))
    except Exception as e:
        print("页面缺少一些属性！不过不用担心！")
        print(e)

    for link in bsObj.findAll("a", href=re.compile("^/wiki/")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print("new pages:{}".format(newPage))
                print("-------------------------------")
                pages.add(newPage)
                getLinks(newPage)
getLinks("")

#!/usr/bin/env python3
# _*_ conding: utf-8 _*_


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# 查找出子标签
print("查找出子标签")
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)


# 处理兄弟标签
print("处理兄弟标签")
for siblings in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(siblings)

# 使用正则表达式抓取页面img中的src
print("使用正则表达式抓取页面img中的src:")
for image in bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")}):
    print(image['src'])

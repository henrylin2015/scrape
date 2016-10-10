# coding:utf8
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


class Handle(object):
    def __init__(self, url):
        self.url = url
        self.bsObj = ""
        print("welcome henry scrape!")

    def content(self):
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            print(e)
            exit(-1)
        self.bsObj = BeautifulSoup(html)
        return self.bsObj

    def findByAll(self, tag, attributes):
        try:
            data = self.content().findAll(tag, attributes)
        except Exception as e:
            print(e)
            exit(-1)
        return data


# 美剧
class Movies(object):
    """init url"""
    def __init__(self, url):
        self.url = url
        self.listUrl = ""
        print("Welcome movies run......")

    def getUrl(self):
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            print(e)
            print("error:url=>{}".format(self.url))
            return None
        return html

    def getListByUrl(self, tag, attributes):
        list = BeautifulSoup(self.getUrl())
        try:
            data = list.findAll(tag, attributes)
        except Exception as e:
            print(e)
            return None
        key = 1
        for i in data:
            href = re.findall(r'<a href="(.*?)".*?>(.*?)</a>', str(i))
            self.getPageContent(href[0][0])
            print("第{}部:{}  ok".format(key, href[0][0]))
            key += 1

    def getPageContent(self, url):
        try:
            content = urlopen(url)
        except HTTPError as e:
            print(e)
            print("error:url=>{}".format(url))
            return None
        data = BeautifulSoup(content)
        tag = "div"
        attributes = {"id": "entry"}
        self.getByContent(data, tag, attributes)

    def getByContent(self, data, tag, attributes):
        try:
            content = data.findAll(tag, attributes)
        except Exception as e:
            print(e)
            return None
        self.getText(content)

    def getText(self, content):
        txt = re.findall(r'<a href="(ed2k://\|file\|.*?)".*?>(.*?)</a>', str(content))
        fb = open('movies.txt', 'a+')
        for list in txt:
            s = "名称：{}, 地址：{}".format(list[1], list[0]) + "\n"
            fb.write(s)
            # print(s)
        fb.close()

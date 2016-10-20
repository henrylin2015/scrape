#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
获取网站的整个连接(外部连接和本网站的连接)
"""
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())


# 获取页面所有内链的列表
def getInternalLinks(bsObj, incluseUrl):
    incluseUrl = urlparse(incluseUrl).scheme+"://"+urlparse(incluseUrl).netloc
    internalLinks = []
    # 找出所有以”/“开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*)" +
                                                   incluseUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(incluseUrl, link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 获取页面所有的外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"wwww"开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|wwww)((?!"
                                                   + excludeUrl + "))*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressPath = address.replace("http://", "").split("/")
    return addressPath


def getRandomExternalLink(startingPage):
    print("url", str(startingPage))
    html = urlopen("http:/oreilly.com")
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"
        +urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(random.randint(0, len(internalLinks)-1))
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingPage):
    externalLinks = getRandomExternalLink(startingPage)
    print("随机外链是：{}".format(externalLinks))
    followExternalOnly(externalLinks)


followExternalOnly("http:/oreilly.com")

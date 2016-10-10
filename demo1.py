#!/usr/bin/env python3
# coding:utf8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitile(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("error:{}".format(e))
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h4
    except AttributeError as e:
        print("error:{}".format(e))
        return None
    return title


url = "http://pythonscraping.com/pages/page1.html"
title = getTitile(url)


if title == None:
    print("Title could not be found")
else:
    print(title)

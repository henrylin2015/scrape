#!/usr/bin/env python3
# coding:utf8
from handle import Movies

# url = "http://pythonscraping.com/pages/warandpeace.html"
url = "http://cn163.net/ddc1/ddc2/"

handle = Movies(url)
tag = "div"
attributes = {"class": "archive_title"}
list = handle.getListByUrl(tag, attributes)

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
伪装爬虫头部发送请求
"""
import requests
from bs4 import BeautifulSoup


session = requests.Session()
# header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accpt": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
url = "https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending"
# req = session.get(url, headers=header)
req = session.get(url)
bsObj = BeautifulSoup(req.text)
html = bsObj.find("table", {"class": "table-striped"}).get_text()
print("info:", html)

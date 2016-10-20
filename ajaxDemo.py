#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# 爬虫抓取ajax中的数据 phantomjs-2.1.1-macosx(这个不是库文件) selenium库

from selenium import webdriver
from bs4 import BeautifulSoup
import time

executable_path = "phantomjs-2.1.1-macosx/bin/phantomjs"
# driver = webdriver.PhantomJS(executable_path)
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# time.sleep(3)
# print(driver.find_element_by_id('content').text)
# driver.close()

driver = webdriver.PhantomJS(executable_path)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(5)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj.find(id="content").get_text())

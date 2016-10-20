#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
获取网站cookie的值
"""
from selenium import webdriver

executable_path = "phantomjs-2.1.1-macosx/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path)
driver.get("http://pythonscraping.com/")
driver.implicitly_wait(1)
print(driver.get_cookies())

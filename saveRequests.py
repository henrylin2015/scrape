#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# requests 库的使用
import requests

params = {"firstname": 'Ryan', "lastname": "Mitchell"}
r = requests.post("http://pythonscraping.com/pages/files/processing.php",
                  data=params)
print(r.text)

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import requests


params = {"username": 'lin', "password": 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",
                  data=params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("--------------------")
print("Going to profile page....")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
                 cookies=r.cookies)
print(r.text)

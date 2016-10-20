#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from urllib.request import urlopen
from bs4 import BeautifulSoup


def ngrams(input, n):
    input = input.split(" ")
    print("---------\n", input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i+2])
    return output


html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
print("-----------------------")
ngrams = ngrams(content, 2)
print(ngrams)

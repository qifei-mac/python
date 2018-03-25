# -*- coding: utf-8 -*-

import requests
import os
import re

def Get_Movies_Title(url):
    respon = requests.get(url)
    respon.encoding = 'gb2312'
    reg = r'<td><a href="(.*?)" target="_blank"><img src="(.*?)" alt="(.*?)"'
    title_url = re.findall(reg,respon.text)
    return title_url

def Get_Movies_torrent(url):
    respon = requests.get(url)
    respon.encoding = 'gb2312'
    #reg = r'<td bgcolor="#ffffbb" width="100%" .*? href="(.*?)">'
    reg = r'href="ed2k://(.*?)"'
    tottent_url = re.findall(reg,respon.text)
    if len((tottent_url)) > 0:
        print('ed2k://' + tottent_url[0])
y = 1
for x in range(1,11):
    for i in Get_Movies_Title("http://www.dygang.net/ys/index_%s.htm" %x):
        print("第%s部"%y,i[2])
        Get_Movies_torrent(i[0])
        y = y+1


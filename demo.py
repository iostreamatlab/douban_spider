
# -*- coding: utf-8 -*-

import requests


r = requests.get('https://book.douban.com/subject/25845930/reviews').text
from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
myAttrs={'class':'short-content'}
list1=[]
soups = soup.find_all(name='div',attrs=myAttrs)
for i in soups:
    list1.append(i)
for i in soups:
    print(i.text)




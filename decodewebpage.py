#!/usr/bin/python
######Method 1
import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
# print(soup)
for i in soup.find_all('span', 'articletitle').string :
    if i is not None :
        print(i)

#####Method 2

from bs4 import BeautifulSoup
import requests


def web_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for title in soup.find_all('h2', {'class': "story-heading"}):
        t = title.string
        if t is not None:
            print(t)

web_page('http://www.nytimes.com')


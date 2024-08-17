from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from urllib import *

visiturl = set()

def spider(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Failed Response {url}")
        return
    if response.status_code == 200:
        soup =BeautifulSoup(response.content,'html.parser')

        atag = soup.find_all('a')
        urls = []
        for t in atag:
            href = t.get("href")
            if href is not None and href !="":
                urls.append(href)

        for url2 in urls:
            if url2 not in visiturl:
                visiturl.add(url2)
                urjoin = urljoin(url,url2)
                if keyword in urjoin:
                    print(urjoin)
                    spider(urjoin, keyword)
            else:
                pass


url = input("Enter the url to scrape  ? ")
keyword = input("enter the keyword to find ?")
spider(url, keyword)
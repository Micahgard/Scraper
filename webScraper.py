from bs4 import BeautifulSoup

import requests

url = input(f"Enter a website to scrape: \n")

scrapedSite = requests.get("http://" + url)

data = scrapedSite.text

soup = BeautifulSoup(data)

webTitle = soup.title
webMeta = soup.find_all('meta')

print("Website Title: ", webTitle)

for meta in webMeta:
    if meta.has_attr('property'):
        if meta['property'] == 'og:description':
            print(meta)


# email = soup.find_all(id=True)
# print(email)


for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])

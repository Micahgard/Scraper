from bs4 import BeautifulSoup

import requests

url = input(f"Enter a website to scrape: \n")

scrapedSite = requests.get("http://" + url)

data = scrapedSite.text

print(data)

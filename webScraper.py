import requests
from bs4 import BeautifulSoup
# Circular import below fails
#import runProgram

def runDesc():
    
    #could potentially refactor variables to description over title as function pulls description
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
    # Want to give choice to user to restart program
    #    runProgram.runChoice()

def runLinks():
    url = input(f"Enter a website to scrape: \n")
    scrapedSite = requests.get("http://" + url)
    data = scrapedSite.text

    soup = BeautifulSoup(data)
    
    for a in soup.find_all('a', href=True):
        print ("Found the URL:", a['href'])

    # Want to give choice to user to restart program
    # runProgram.runChoice()

import requests
import whois
import sys, getopt, time
from bs4 import BeautifulSoup


def runLinks(soup):
    for a in soup.find_all('a', href=True):
        print("Found the URL:", a['href'])

    return()
    # Want to give choice to user to restart program


def runTitle(soup):
    webTitle = soup.title
    webMeta = soup.find_all('meta')

    print("Website Title: ", webTitle)

    for meta in webMeta:
        if meta.has_attr('property'):
            if meta['property'] == 'og:description':
                print(meta)

    return()
    # Want to give choice to user to restart program

def runWhois(webUrl):
    try: 
        whoInfo = whois.whois(webUrl)
        print("WhoIs: \n")
        print(whoInfo)
    except:
        "Error getting WhoIs Information \n"
    

def main(argv):
    url = sys.argv[1]        
        #could potentially refactor variables to description over title as function pulls description
    try:
        scrapedSite = requests.get("http://" + url)
        time.sleep(3)
        data = scrapedSite.text

        soup = BeautifulSoup(data, 'html.parser')
        time.sleep(3)

        runTitle(soup)
        runLinks(soup)
        runWhois(url)
    except getopt.GetoptError:
        sys.exit(2)

    print("\n...Finished Running Python")
 
if __name__ == "__main__":
    main(sys.argv[1:])

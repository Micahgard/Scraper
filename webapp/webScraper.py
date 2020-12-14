from bs4 import BeautifulSoup

import requests
import sys, getopt, time

def main(argv):
    url = sys.argv[1]

    try:
        scrapedSite = requests.get("http://" + url)
        time.sleep(3)
        data = scrapedSite.text

        soup = BeautifulSoup(data, 'html.parser')
        time.sleep(3)

        webTitle = soup.title
        webMeta = soup.find_all('meta')

        print("Website Title: ", webTitle)

        for meta in webMeta:
            if meta.has_attr('property'):
                if meta['property'] == 'og:description':
                    print(meta)
        
    except getopt.GetoptError:
        sys.exit(2)
    
    print("\n...Finished Running Python")

if __name__ == "__main__":
    main(sys.argv[1:])

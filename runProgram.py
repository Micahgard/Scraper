import webScraper



def runChoice():

    userChoice = input("Would you like to get the title, links or exit? ")
    userChoice.casefold()

    if userChoice == "links":
        webScraper.runLinks()

    elif userChoice == "title":
        webScraper.runTitle()

    elif userChoice == "exit":
       quit()

    else:
        print ("Invalid")
        runChoice()

    runChoice()

print ("Welcome to the web scraper")
runChoice()

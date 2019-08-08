from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def scrapeWeb(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    links = list(soup.findAll('meta'))
    return str(links[10]).split('"')[1]



x = input("Instagram link here!\n")
print(scrapeWeb(x))
c = input("Press enter to close!")
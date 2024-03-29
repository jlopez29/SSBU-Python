from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = "https://www.proguides.com/super-smash-bros-ultimate/characters/villager"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url=url, headers=headers) 
html = urlopen(req)

with open('page.html', 'wb') as handler:
            handler.write(html.read())

soup = BeautifulSoup(html,'html.parser')

divs = soup.find_all('div', attrs={'class': 'smash-attributes__bar-container'})

for div in divs:
    print(div.get('style'))
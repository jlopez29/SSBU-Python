from urllib.request import urlopen, Request
# url = "https://www.proguides.com/super-smash-bros-ultimate/characters/villager"
url = "https://en.wikipedia.org/wiki/Characters_in_the_Super_Smash_Bros._series"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = "https:XXXXOOOO"
req = Request(url=url, headers=headers) 
f = urlopen(req)

with open('wiki.html','wb') as html:
    html.write(f.read())


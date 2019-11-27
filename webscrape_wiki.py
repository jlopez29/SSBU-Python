from bs4 import BeautifulSoup
import json

with open('wiki.html','rb') as htmlFile:
  html = htmlFile.read()

soup = BeautifulSoup(html, 'html.parser')
body = soup.find('tbody')

chars = {}

for row in body.find_all('tr'):
  head = row.find('th')
  header = head.get_text()
  header = header.split('[')[0]
  header = header.strip()
  try:
    if(row.find_all('i')[0].find('a') is not None):
      series = row.find_all('i')[0].find('a').get_text()
    else:
      series = row.find('i').get_text()
  except:
    series = row.find('a').get_text()
    

  if(header.strip() != 'Fighter' and header.strip() != 'Total'):
    chars[header] = series
    print(header + " : " + series)
    print("\n")

with open('series.json','w') as series:
  json.dump(chars,series)
# header = body.find_all('th')
# print(header)
# row = body.find_all('a')
# print(row)

# The first tr contains the field names.
# headings = [th.get_text().strip() for th in table.find("thead").find_all("th")]

# # print(headings)

# table = soup.find('tbody')

# datasets = []
# for row in table.find_all("tr")[0:]:
#     dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
#     datasets.append(dataset)

# # print(datasets)

# with open('data.json', 'w') as f:
#     json.dump(datasets, f)
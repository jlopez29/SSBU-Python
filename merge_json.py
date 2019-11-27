import json 

with open('result.json') as json_file:
    chars = json.loads(json_file.read())


with open('series.json') as jfile:
    series = json.loads(jfile.read())

for char in chars:
    char['series'] = series[char['name']]

with open('final_results.json','w') as fin:
    json.dump(chars,fin)
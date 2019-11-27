import json
import requests
import os
 
dirpath = os.getcwd()

with open(dirpath + '/ssbu_scripts/scripts/series.json') as jfile:
    series = json.loads(jfile.read())

keyList = {'Back Aerial',
        'Back Throw',
        'Dash Attack',
        'Down Aerial',
        'Down Smash',
        'Down Special',
        'Down Throw',
        'Down Tilt',
        'Final Smash',
        'Forward Aerial',
        'Forward Smash',
        'Forward Throw',
        'Forward Tilt',
        'Grab',
        'Neutral Aerial',
        'Neutral Attack',
        'Neutral Special',
        'Side Special',
        'Up Aerial',
        'Up Smash',
        'Up Special',
        'Up Throw',
        'Up Tilt'}

# chars = [
#     'mario'
# ]

chars = [
    'mario', 'donkey-kong', 'link',
    'samus', 'dark-samus', 'yoshi',
    'kirby', 'fox', 'pikachu', 'luigi',
    'ness', 'captain-falcon', 'jigglypuff',
    'peach', 'daisy', 'bowser', 'ice-climbers',
    'sheik', 'zelda', 'dr-mario', 'pichu',
    'falco', 'marth', 'lucina', 'young-link',
    'ganondorf', 'mewtwo', 'roy', 'chrom', 
    'mr-game-watch', 'meta-knight', 'pit',
    'dark-pit', 'zero-suit-samus', 'wario', 'snake',
    'ike', 'pokemon-trainer-charizard','pokemon-trainer-ivysaur','pokemon-trainer-squirtle', 'diddy-kong', 'lucas',
    'sonic', 'king-dedede', 'olimar', 'lucario', 'r-o-b',
    'toon-link', 'wolf', 'villager', 'mega-man', 'wii-fit-trainer',
    'rosalina-luma', 'little-mac', 'greninja', 'mii-swordfighter','mii-gunner','mii-brawler',
    'palutena', 'pac-man', 'robin', 'shulk', 'bowser-jr',
    'duck-hunt', 'ryu', 'ken', 'cloud', 'corrin',
    'bayonetta', 'inkling', 'ridley', 'simon', 'richter',
    'king-k-rool', 'isabelle', 'incineroar', 'piranha-plant',
    'joker', 'hero', 'banjo-kazooie'
]

tiers = ['S','A','B','C','D','E']

finalList = []

def findTier(dictionary,charId):
    for tier in tiers:

        tierz = dictionary[str(tier)]
        
        try:
            tierz[str(charId)]
            return tier
        except:
            pass
        
    return tier
    

def iterate(dictionary,dataOut,moveList,featureList,advObj):
    for key, value in dictionary.items():

        if(key != 'id' and key != 'featured_moves' and key != 'move_set' and key != 'attribute_ratings' and key != 'key' and key != 'portrait_image' and key != 'primary_fighting_style' and key != 'secondary_fighting_style' and key != 'advantages' and key != 'disadvantages' and key != 'thumbnail_image' and key != 'series_image'):
            dataOut[key] = value
            if(key == 'name'):
                dataOut['series'] = series[value]
        elif(key == 'id'):
            dataOut['_id'] = value
        elif(key == 'attribute_ratings'):
            attrs = {}
            attrs['damage'] = value['Damage'] * 2
            attrs['kill_power'] = value['Kill Power'] * 2
            attrs['defense'] = value['Defense'] * 2
            attrs['speed'] = value['Speed'] * 2
            attrs['neutral'] = value['Neutral'] * 2
            attrs['weight'] = value['Weight'] * 2
            attrs['recovery'] = value['Recovery'] * 2
            dataOut['overall'] = round((((attrs['damage']+attrs['kill_power']+attrs['defense']+attrs['speed']+attrs['neutral']+attrs['weight']+attrs['recovery'])/ 70) * 100),2)

            dataOut['attributes'] = attrs
        elif(key == 'advantages' or key == 'disadvantages'):
            if(key == 'advantages'):
                advObj['advantages'] = value
            else:
                advObj['disadvantages'] = value
            
            dataOut['traits'] = advObj

        if(key == 'id'):
            tier_url = 'https://www.proguides.com/api/v2/game-meta/super-smash-bros-ultimate/characters/tier-list'
            tier_data = json.loads(requests.get(tier_url).content)
            dataOut['tier'] = findTier(tier_data,value)
            
        # print(dataOut)
        

def getMoves(dictionary,dataOut,moveList,featureList,advObj):
    for key in keyList:
        jsonData = {}
        move = {}
        obj = dictionary[key]

        # print(dictionary)
        
        move['move'] = obj['key']
        move['description'] = obj['description']
        move['video_uri'] = obj['video_file_url']

        jsonData['move'] = move
        moveList.append(jsonData['move'])

    dataOut['move_set'] = moveList

    finalList.append(dataOut)
    with open('results.json', 'w') as fp:
        json.dump(finalList, fp)

def getData():
    for char in chars:
        dataOut = {}
        moveList = []
        featureList = []
        advObj = {}
        stringy = 'https://www.proguides.com/api/v2/game-resources/super-smash-bros-ultimate/static-data/characters/by-key/{0}'.format(char)
        data = json.loads(requests.get(stringy).content)
        # print(data)

        iterate(data,dataOut,moveList,featureList,advObj)
        getMoves(data['move_set'],dataOut,moveList,featureList,advObj)

getData()
import json 

with open('./ssbu_scripts/data/result.json') as json_file:
    chars = json.loads(json_file.read())

import os

charNameMap = {
    'mario':'Mario', 
    'donkey_kong':'Donkey Kong', 
    'link':'Link',
    'samus':'Samus', 
    'dark_samus':'Dark Samus', 
    'yoshi':'Yoshi',
    'kirby':'Kirby', 
    'fox':'Fox', 
    'pikachu':'Pikachu', 
    'luigi':'Luigi',
    'ness':'Ness', 
    'captain_falcon':'Captain Falcon', 
    'jigglypuff':'Jigglypuff',
    'peach':'Peach', 
    'daisy':'Daisy', 
    'bowser':'Bowser', 
    'ice_climbers':'Ice Climbers',
    'sheik':'Sheik', 
    'zelda':'Zelda', 
    'dr_mario':'Dr. Mario', 
    'pichu':'Pichu',
    'falco':'Falco', 
    'marth':'Marth', 
    'lucina': 'Lucina', 
    'young_link':'Young Link',
    'ganondorf':'Ganondorf', 
    'mewtwo':'Mewtwo', 
    'roy':'Roy', 
    'chrom':'Chrom', 
    'mr_game_and_watch':'Mr. Game & Watch', 
    'meta_knight': 'Meta Knight', 
    'pit': 'Pit',
    'dark_pit': 'Dark Pit', 
    'zero_suit_samus': 'Zero Suit Samus', 
    'wario':'Wario', 
    'snake':'Snake',
    'ike':'Ike', 
    'pokemon_trainer':'Pokemon Trainer', 
    'diddy_kong': 'Diddy Kong', 
    'lucas':'Lucas',
    'sonic':'Sonic', 
    'king_dedede':'King Dedede', 
    'olimar':'Olimar', 
    'lucario':'Lucario', 
    'rob':'R.O.B.',
    'toon_link':'Toon Link', 
    'wolf':'Wolf', 
    'villager':'Villager', 
    'mega_man':'Mega Man', 
    'wii_fit_trainer':'Wii Fit Trainer',
    'rosalina_and_luma':'Rosalina & Luma', 
    'little_mac':'Little Mac', 
    'greninja':'Greninja', 
    'mii_fighter':'Mii Fighter',
    'palutena':'Palutena', 
    'pac_man':'Pac Man', 
    'robin':'Robin', 
    'shulk':'Shulk', 
    'bowser_jr':'Bowser Jr.',
    'duck_hunt':'Duck Hunt', 
    'ryu':'Ryu', 
    'ken':'Ken', 
    'cloud':'Cloud', 
    'corrin':'Corrin',
    'bayonetta':'Bayonetta', 
    'inkling':'Inkling', 
    'ridley':'Ridley', 
    'simon':'Simon', 
    'richter':'Richter',
    'king_k_rool':'King K. Rool', 
    'shizue':'Isabelle', 
    'incineroar':'Incineroar', 
    'piranha_plant':'Piranha Plant',
    'joker':'Joker', 
    'dq_hero':'Hero', 
    'banjo_and_kazooie':'Banjo & Kazoo', 
    'terry':'Terry'
}

def findChar(name):
    for i in range(len(chars)):
        print(chars[i]['name'] + " == " + name)
        if(chars[i]['name'] == name):
            print("found " + name)
            return chars[i]


obj = {}
skinList = []
currChar = ""
for subdir, dirs, files in os.walk("./ssbu_scripts/characters"):
    skinList = []
    for file in files:
        currChar = subdir.split('/')[3]
        # print(os.path.join(subdir, file))
        filepath = subdir + os.sep + file
        f = open(filepath,"r").read()
        skinList.append(f)

    try:
        charObj = findChar(charNameMap[currChar])
        charObj['skins'] = skinList
    except:
        pass
    # char['skins'] = skinList


with open('charSkins.json', 'w') as fp:
    json.dump(chars, fp)


    
        

import requests
import os

# characters_img = [
#     'villager'
# ]

# characters = [
#     'mario'
# ]

# characters_ic = [
#     'gaogaen', 'packun_flower'
# ]

characters = [
    'mario', 'donkey_kong', 'link',
    'samus', 'dark_samus', 'yoshi',
    'kirby', 'fox', 'pikachu', 'luigi',
    'ness', 'captain_falcon', 'jigglypuff',
    'peach', 'daisy', 'bowser', 'ice_climbers',
    'sheik', 'zelda', 'dr_mario', 'pichu',
    'falco', 'marth', 'lucina', 'young_link',
    'ganondorf', 'mewtwo', 'roy', 'chrom', 
    'mr_game_and_watch', 'meta_knight', 'pit',
    'dark_pit', 'zero_suit_samus', 'wario', 'snake',
    'ike', 'pokemon_trainer', 'diddy_kong', 'lucas',
    'sonic', 'king_dedede', 'olimar', 'lucario', 'rob',
    'toon_link', 'wolf', 'villager', 'mega_man', 'wii_fit_trainer',
    'rosalina_and_luma', 'little_mac', 'greninja', 'mii_fighter',
    'palutena', 'pac_man', 'robin', 'shulk', 'bowser_jr',
    'duck_hunt', 'ryu', 'ken', 'cloud', 'corrin',
    'bayonetta', 'inkling', 'ridley', 'simon', 'richter',
    'king_k_rool', 'shizue', 'incineroar', 'piranha_plant',
    'joker', 'dq_hero', 'banjo_and_kazooie', 'terry'
]

def fetch_character_img():
    for char in characters:
        os.mkdir("chars/"+char)
        for i in range(10):
            stringy = 'https://www.smashbros.com/assets_v2/img/fighter/{0}/main{1}.png'.format(char,i)
            img_data = requests.get(stringy).content
            with open('./chars/'+char+'/img_'+char+'_skin_'+str(i)+'.png', 'wb') as handler:
                handler.write(img_data)

# def fetch_character_icon():
#     for i in range(len(characters_ic)):
#         image_url = 'https://www.smashbros.com/assets_v2/img/fighter/pict/{0}.png'.format(characters_ic[i])
#         img_data = requests.get(image_url).content
#         with open('ic_{0}.png'.format(characters_ic[i]), 'wb') as handler:
#             handler.write(img_data)
#             print('Icon Downloaded... >>> ' + characters_ic[i])

fetch_character_img()
# fetch_character_icon()

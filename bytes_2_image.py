import base64
import os
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


for char in characters:
    for i in range(1,9):
        url = "characters/{0}/img_{0}_skin_{1}.txt".format(char,i)
        image = open(url,"rb").read()

        url = "characters/{0}/img_{0}_skin_{1}.png".format(char,i)
        g = open(url, "wb")
        g.write((base64.decodebytes(image)))
        g.close()
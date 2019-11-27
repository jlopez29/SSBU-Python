import requests

chars = [
    'villager'
]

def fetch_character_img():

    for i in range(len(chars)):
        stringy = 'https://www.proguides.com/api/v2/game-resources/super-smash-bros-ultimate/static-data/characters/by-key/{0}'.format(chars[i])
        img_data = requests.get(stringy).content
        with open('data_'+chars[i]+'.json', 'wb') as handler:
            handler.write(img_data)


fetch_character_img()
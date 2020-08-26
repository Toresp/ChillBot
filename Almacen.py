import random


def style(msg):
    msg.lower()
    music_type = {'chill':'CancionesC.csv','japanese_type':'CancionesJ.csv','electro':'CancionesE'}
    if msg in music_type:
        value = music_type[msg]
        with open(value, 'r') as link:
            links = link.read().split(';')
            msg = links[random.randint(0, len(links))-1]
            return msg



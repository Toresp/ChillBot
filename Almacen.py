import random


def style(msg):
    msg.lower()
    music_type = {'chill':'Canciones.csv','japanese_type':'CancionesR.csv'}
    if msg in music_type:
        value = music_type[msg]
        with open(value,'r') as link:
            links = link.read().split(';')
            return links[random.randint(0, len(links))-1]
    return 'no'



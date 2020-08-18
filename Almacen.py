import random


def style(msg):
    msg.lower()
    music_type = {'chill':'Canciones.csv','dubsteb':'CancionesD.cvs','rock':'CancionesR.csv'}
    value = music_type[msg]
    with open(value,'r') as link:
        links = link.read().split(';')
        print(links[random.randint(0, len(links))-1])
    return 0



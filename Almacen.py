import random
with open("Canciones.txt","r") as file:

generos = {'chill' : chill, 'rock' :rock,'dubsteb' : dubsteb}
txt='dubsteb'
print (generos[txt][random.randint(0,4)])
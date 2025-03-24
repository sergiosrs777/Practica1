import json
Practica1 = json.load(open("Practica1.json"))

# El atletico se fundo en 1903 en Madrid
print(f"El {Practica1['club']} se fundo en {Practica1['fundacion']} en {Practica1['ciudad']}")

# Juego en el Riyad Metropolitano y esta entrenado por Diego Simeone
print(f" Juegan en el {Practica1['estadio']} y esta entrenado {Practica1['entrenador']}")

# El atletico de madrid ha obtenido la liga 11 veces
print(f"El {Practica1['club']} ha obtenido la liga {Practica1['trofeos']['liga']} veces")

# Mi jugador favorito es Jualian alvarez
print(f"Mi jugador favorito es {Practica1['plantilla']['Delantero'][0]}")

#Jugadores
print("Plantilla:")
for posicion in Practica1['plantilla']:
    print(f"{posicion}")
    for jugador in Practica1['plantilla'][posicion]:
        print(f"{jugador}")
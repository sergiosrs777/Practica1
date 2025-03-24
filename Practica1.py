import json
Practica1 = json.load(open("Practica1.json"))

# El atletico se fundo en 1903 en Madrid
print(f"El {Practica1['club']} se fundo en {Practica1['fundacion']} en {Practica1['ciudad']}")


"""
Program that can retrieve multiple Pokemon and save their names
and moves to a file

Use a list to store about 6 pokemon IDs. Then in a for loop call
the API to retrieve the data for each Pokemon.

Save their names and moves into a file called pokemon.txt

"""
# Q3
# step 1: use a list to store 6 Pokemon IDs

import requests

pokemon_id = [
    249,
    849,
    898,
    248,
    887,
    345
]

# step 2: in a for loop call the API to retrieve the data for each Pokemon

pokemon_names = []

for i in pokemon_id:
    url = f'https://pokeapi.co/api/v2/pokemon/{i}/'
    response = requests.get(url)
    pokemon = response.json()
    pokemon_names.append(pokemon["name"])

# step 3: save their names and move into a file called 'pokemon.txt'

pokemon_names = []

for i in pokemon_id:
    url = f'https://pokeapi.co/api/v2/pokemon/{i}/'
    response = requests.get(url)
    pokemon = response.json()
    pokemon_names.append(pokemon["name"])

with open('pokemon.txt', 'w+') as pokemon_file:
    for item in pokemon_names:
        item2 = item + '\n'
        pokemon_file.write(item2)
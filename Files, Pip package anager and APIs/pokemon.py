import requests


# 6 pokemon IDS
pokemon_ids = [
    50,
    359,
    598,
    208,
    887,
    245
]

pokemons = []

for pokemonnames in pokemon_ids:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonnames}/"
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon["name"])


with open("pokemons.txt", "w+") as output:
   allpokemon = pokemon
   output.read(allpokemon + "\n")
#
# with open('pokemons.txt','r') as output:  # pokemon.txt (l know :P)
#     contents = output.read(pokemon_list + "\n")
#
# print(contents)

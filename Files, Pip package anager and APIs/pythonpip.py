# pip - a package manager used to install libraries that other people have done
# pip install requests

import requests
# from pprint import pprint
#
# pokemon_number = input("What is the Pokemon's ID? ")
#
# url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/"
# response = requests.get(url)
# print(response)
#
# pokemon = response.json()
# pprint(pokemon)


# 202 the request worked
# 404 couldn't find the urlyou request
# 400 the request you made isn't understood

"""
Get the height and weight of a specific 
Pokemon and print the output

Extension: Print the names of all of 
a specific Pokemon's moves

"""

from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/"
response = requests.get(url)


pokemon = response.json()
pprint(pokemon["name"])
pprint(pokemon["height"])
pprint(pokemon["weight"])

# for each in pokemon ["moves"]:
#     print(each["move"]["name"])

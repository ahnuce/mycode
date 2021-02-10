#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget

def main():
    x = str(input("Whos that Pokemon?")).lower().strip()
    pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+x).json()

    print(pokemon)

    picUrl= (pokemon["sprites"]["front_default"])

    wget.download(picUrl, "/home/student/static/")

    print("URL: ", picUrl)
    print("# of Games:", len(pokemon["game_indices"]))

    for movedict in pokemon["moves"]:
        print(movedict["move"]["name"])

main()

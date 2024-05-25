import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '05a6851538c085f08e87c3c5c6bf3f30'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "28368",
    "name": "Заврбульба",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_catch = {
    "pokemon_id": "28368"
}

response_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json= body_create)
print(response_create.text)

response_change = requests.put(url=f'{URL}/pokemons', headers = HEADER, json= body_change)
print(response_change.text)

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json= body_catch)
print(response_catch.text)
import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TRAINER_ID=2349

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code==200
import requests
from random import randint

BASE_URL = 'http://127.0.0.1:8009/getapi?num='

for i in range(1000):
    url = f'{BASE_URL}{i}'
    requests.request('GET', url)

import requests


response = requests.get('https://openexchangerates.org/api/latest.json?app_id=a73871bc447e4d4aadcbfe76e8857d08')

print(response.status_code)
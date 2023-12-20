import requests

def get_currencies():
    api_key = 'a73871bc447e4d4aadcbfe76e8857d08'
    url = 'https://openexchangerates.org/api/currencies.json?prettyprint=false&show_alternative=false&show_inactive=false&app_id=a73871bc447e4d4aadcbfe76e8857d08'

    headers = {
        'accept': 'application/json',
    }

    params = {
    'prettyprint': 'false',
    'show_alternative': 'false',
    'show_inactive': 'false',
    'app_id': api_key,
    }
    
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        # Access the currency data from the response
        currencies = list(data.keys())[:10]
        return currencies
    else:
        print('Failed to retrieve data. Status code:', response.status_code)    
        return None

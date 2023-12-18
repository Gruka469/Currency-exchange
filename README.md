# Currency exchange
A tkinter python app for currency exchange
```python

Requests

from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests

def get_conversion_rate(taregt_currency):
    api_key = 'a73871bc447e4d4aadcbfe76e8857d08'
    url = 'https://openexchangerates.org/api/latest.json?app_id=a73871bc447e4d4aadcbfe76e8857d08' #By default currency = USD

    #Graceful error handling
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][taregt_currency]
        return rate
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

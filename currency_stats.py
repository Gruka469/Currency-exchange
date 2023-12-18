from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests

def get_currencies():
    api_key = 'a73871bc447e4d4aadcbfe76e8857d08'
    url = 'https://openexchangerates.org/api/currencies.json?prettyprint=false&show_alternative=false&show_inactive=false&app_id=a73871bc447e4d4aadcbfe76e8857d08'

    try:
        response = requests.get(url)

    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None
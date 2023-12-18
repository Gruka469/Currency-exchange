from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests

#API request for conversion rates
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



def input_currency():
    # Destroy the current window
    window.destroy()

    # Create a new window for currency submission
    submit_window = tk.Tk()
    submit_window.title("Submit Currency")
    submit_window.geometry('400x200')

    first_currency_label = tk.Label(submit_window, text="Enter First Currency:")
    first_currency_entry = tk.Entry(submit_window)
    second_currency_label = tk.Label(submit_window, text="Enter Second Currency:")
    second_currency_entry = tk.Entry(submit_window)
    submit_button = tk.Button(submit_window, text="Submit", command=lambda: submit(first_currency_entry.get(), second_currency_entry.get())) #passing both of the arguments with "get" method

    first_currency_label.grid(row=0, column=0, padx=10, pady=10) #positioning accordingly
    first_currency_entry.grid(row=0, column=1, padx=10, pady=10) #positioning accordingly
    second_currency_label.grid(row=1, column=0, padx=10, pady=10) #positioning accordingly
    second_currency_entry.grid(row=1, column=1, padx=10, pady=10) #positioning accordingly
    submit_button.grid(row=2, column=0, columnspan=2, pady=10) #positioning accordingly

def submit(first_currency, second_currency):
    # Print or use the entered currencies as needed
    print("First Currency:", first_currency) #printing the currency inputed from the .entry
    print("Second Currency:", second_currency) #printing the currency inputed from the .entry

    conversion_rate = get_conversion_rate(first_currency, second_currency)

    if conversion_rate is not None:
        print(f"Conversion rate from {first_currency} to {second_currency}: {conversion_rate}")

# Create the main window
window = tk.Tk()
window.title("Currency Application")
window.geometry('400x200')

# Create a button to initiate the currency input
button = tk.Button(window, text="Click me", command=input_currency)
button.grid(row=0, column=0, pady=10)

# Start the Tkinter event loop
window.mainloop()

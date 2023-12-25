from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
from get_currencies import get_currencies
import traceback

#API request for conversion rates
#The API supports conversions only from a base or source currency make it work like that !!!
def get_conversion_rate(base_currency, target_currency):
    api_key = 'a73871bc447e4d4aadcbfe76e8857d08'
    url = 'https://openexchangerates.org/api/latest.json?app_id=a73871bc447e4d4aadcbfe76e8857d08' #By default currency = USD

    #Graceful error handling
    try:
        response = requests.get(url)
        data = response.json()
        if target_currency and target_currency in data['rates']:
            rate = data['rates'][target_currency]
            return rate
        else:
            print(f"Error: Invalid or empty target_currency: {target_currency}")
            return None

    except Exception as e:
        print(f"Error fetching data from API: {e}")
        traceback.print_exc()
        return None



def input_currency():
    # Destroy the current root
    root.destroy()

    # Create a new root for currency submission
    submit_root = tk.Tk()
    submit_root.title("Submit Currency")
    submit_root.geometry('600x400')
    # boxes for currency input
    first_currency_label = tk.Label(submit_root, text="Enter First Currency:")
    second_currency_label = tk.Label(submit_root, text="Enter Second Currency:")
    amount_label = tk.Label(submit_root, text="Enter Amount:")
    amount_entry = tk.Entry(submit_root) #That's the input box for the amount
    submit_button = tk.Button(submit_root, text="Submit", command=lambda: submit(selected_option, \
                                                                                selected_option1, submit_root)) #passing all of the arguments needed
    convert_button = tk.Button(submit_root, text="Convert", command=lambda: conversion_calc(selected_option, \
                                                                                            selected_option1, \
                                                                                            amount_entry, submit_root)) #passing all of the arguments needed
    #dropdown menu
    #Using combobox because it's more flexible
    selected_option = tk.StringVar(submit_root)
    selected_option1 = tk.StringVar(submit_root)
    combobox = ttk.Combobox(submit_root, textvariable=selected_option, values=get_currencies(), state="readonly", height=5)
    combobox1 = ttk.Combobox(submit_root, textvariable=selected_option1, values=get_currencies(), state="readonly", height=5)
    
    #grid system
    first_currency_label.grid(row=0, column=0, padx=10, pady=10) #positioning accordingly
    second_currency_label.grid(row=1, column=0, padx=10, pady=10) #positioning accordingly
    amount_label.grid(row=2, column=0, padx=10, pady=10) #positioning accordingly
    amount_entry.grid(row=2, column=1, padx=10, pady=10) #positioning accordingly
    submit_button.grid(row=3, column=0, columnspan=2, pady=10) #positioning accordingly
    convert_button.grid(row=3, column=1, columnspan=2, pady=10) #positioning accordingly
    combobox.grid(row=0, column=1, padx=10, pady=10) #positioning accordingly
    combobox1.grid(row=1, column=1, padx=10, pady=10) #positioning accordingly

def submit(selected_option, selected_option1, submit_root):
    first_currency = selected_option.get()
    second_currency = selected_option1.get()
    # Print entered currencies inside the GUI
    label1 = Label(submit_root, text=f"First Currency: {first_currency}")
    label1.grid(row=4, column=0, padx=10, pady=10)
    label2 = Label(submit_root, text=f"Second Currency: {second_currency}")
    label2.grid(row=5, column=0, padx=10, pady=10)

    conversion_rate = get_conversion_rate(first_currency, second_currency) #The whole conversion rate

    #Checks if the function is True and then returns some text
    if conversion_rate is not None:
        label3 = Label(submit_root, text=f"Conversion rate from {first_currency} to {second_currency}: {conversion_rate}")
        label3.grid(row=6, column=0, padx=10, pady=10)
        
#CREATE A FUNCTION TO TAKE ANY KIND OF SUM OF MONEY AND EXCHANGE THE CURRENCY        
def conversion_calc(selected_option, selected_option1, number_entry, root):
    """
    Error fetching data from API: ''
    """
    base_currency = selected_option.get()
    target_currency = selected_option1.get()
    number_to_convert = float(number_entry.get())  # convert the entry to a float

    try:
        conversion_rate = get_conversion_rate(base_currency, target_currency)
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        traceback.print_exc()
        return None
    
    if conversion_rate is not None:
        currency_calculation = conversion_rate * number_to_convert
        label1 = tk.Label(root, text=f"Converted amount: {currency_calculation:.2f}") #It's overwriting the previous statement remove the previous so it's alright
        label1.grid(row=6, column=0, padx=10, pady=10)


# Create the main root
root = tk.Tk()
root.title("Currency Application")
root.geometry('600x400')

# Create a button to initiate the currency input
button = tk.Button(root, text="Click me", command=input_currency)
button.grid(row=0, column=0, pady=10)

# Start the Tkinter event loop
root.mainloop()

from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
from currency_stats import get_currencies

#API request for conversion rates
def get_conversion_rate(base_currency, target_currency):
    api_key = 'a73871bc447e4d4aadcbfe76e8857d08'
    url = 'https://openexchangerates.org/api/latest.json?app_id=a73871bc447e4d4aadcbfe76e8857d08' #By default currency = USD

    #Graceful error handling
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None



def input_currency():
    # Destroy the current root
    root.destroy()

    # Create a new root for currency submission
    submit_root = tk.Tk()
    submit_root.title("Submit Currency")
    submit_root.geometry('400x200')
    # boxes for currency input
    first_currency_label = tk.Label(submit_root, text="Enter First Currency:")
    first_currency_entry = tk.Entry(submit_root)
    second_currency_label = tk.Label(submit_root, text="Enter Second Currency:")
    second_currency_entry = tk.Entry(submit_root)
    submit_button = tk.Button(submit_root, text="Submit", command=lambda: submit(first_currency_entry.get(), second_currency_entry.get(), selected_option, selected_option1)) #passing both of the arguments with "get" method
    #dropdown menu
    selected_option = tk.StringVar(submit_root)
    selected_option1 = tk.StringVar(submit_root)
    combobox = ttk.Combobox(submit_root, textvariable=selected_option, values=get_currencies(), state="readonly", height=5)
    combobox1 = ttk.Combobox(submit_root, textvariable=selected_option1, values=get_currencies(), state="readonly", height=5)
    
    #grid system
    first_currency_label.grid(row=0, column=0, padx=10, pady=10) #positioning accordingly
    first_currency_entry.grid(row=0, column=1, padx=10, pady=10) #positioning accordingly
    second_currency_label.grid(row=1, column=0, padx=10, pady=10) #positioning accordingly
    second_currency_entry.grid(row=1, column=1, padx=10, pady=10) #positioning accordingly
    submit_button.grid(row=2, column=0, columnspan=2, pady=10) #positioning accordingly
    combobox.grid(row=0, column=3, padx=10, pady=10)
    combobox1.grid(row=1, column=3, padx=10, pady=10)

def submit(first_currency, second_currency, selected_option, selected_option1):
    # If the entry fields are empty, use the dropdown values
    if not first_currency:
        first_currency = selected_option.get()
    if not second_currency:
        second_currency = selected_option1.get()
    # Print or use the entered currencies as needed
    print("First Currency:", first_currency) #printing the currency inputed from the .entry
    print("Second Currency:", second_currency) #printing the currency inputed from the .entry

    conversion_rate = get_conversion_rate(first_currency, second_currency)

    if conversion_rate is not None:
        print(f"Conversion rate from {first_currency} to {second_currency}: {conversion_rate}")
        
#FUNCTION TO RETURN THE CURRENCY RATE IN THE APP!!!!


# Create the main root
root = tk.Tk()
root.title("Currency Application")
root.geometry('400x200')

# Create a button to initiate the currency input
button = tk.Button(root, text="Click me", command=input_currency)
button.grid(row=0, column=0, pady=10)

# Start the Tkinter event loop
root.mainloop()

from tkinter import *
from tkinter import ttk
import tkinter as tk


def input_currency():
    first_currency = tk.Label(text="Currency")
    first_currency_entry = tk.Entry(window)
    second_currency = tk.Label(text="Currency")
    second_currency_entry = tk.Entry(window)

    first_currency.pack(padx=10, pady=10)
    first_currency_entry.pack(padx=10, pady=10)
    second_currency.pack(padx=10, pady=10)
    second_currency_entry.pack(padx=10, pady=10)

window = tk.Tk()
window.title("Currency Application")

button = tk.Button(window, text="Click me", command=input_currency)
button.pack(pady=10)

window.mainloop()

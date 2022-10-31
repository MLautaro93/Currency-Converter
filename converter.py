import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

# Create window
window = tk.Tk()
window.geometry('512x256')
window.resizable(False, False)
window.title('Currency Converter')

# Fetch data
url = 'https://api.exchangerate-api.com/v4/latest/USD'
data = requests.get(url).json()['rates']

# Variables
amount = tk.IntVar(value = '')

# Label
intro_label = tk.Label(text = 'Currency converter', font = 'lucida 15 bold', fg = 'white', bg = 'green')
intro_label.pack()

# Entries
from_entry = tk.Entry(textvariable = amount)
from_entry.place(relx = .25, y = 125, anchor = tk.CENTER)
to_entry = tk.Entry()
to_entry.place(relx = .75, y = 125, anchor = tk.CENTER)

# Comboboxes
currencies = list(data.keys())

from_box = ttk.Combobox(values = currencies, state = 'readonly')
from_box.place(relx = .25, y = 75, anchor = tk.CENTER)
to_box = ttk.Combobox(values = currencies, state = 'readonly')
to_box.place(relx = .75, y = 75, anchor = tk.CENTER)

# Convert function
def convert(*args):
    try:
        from_rate = data[from_box.get()]
        to_rate = data[to_box.get()]
        conversion = amount.get() / from_rate * to_rate
        to_entry.delete(0, tk.END)
        to_entry.insert(tk.END, conversion)
    except:
        tk.messagebox.showinfo('Error', 'Please, enter a number and select two currencies to convert.')

# Swap function
def swap():
    x = from_entry.get()
    y = to_entry.get()
    from_entry.delete(0, tk.END)
    from_entry.insert(tk.END, y)
    to_entry.delete(0, tk.END)
    to_entry.insert(tk.END, x)

    a = from_box.get()
    b = to_box.get()
    from_box.set(b)
    to_box.set(a)

# Convert button
convert_button = tk.Button(text = 'Convert', fg = 'white', bg = 'green', command = convert)
convert_button.place(relx = .5, y = 175, anchor = tk.CENTER)
window.bind('<Return>', convert)

# Swap button
swap_img = Image.open('swap.jpg').resize((25, 25))
swap_image = ImageTk.PhotoImage(swap_img)
swap_button = tk.Button(image = swap_image, command = swap)
swap_button.place(relx = .5, y = 100, anchor = tk.CENTER)


window.mainloop()
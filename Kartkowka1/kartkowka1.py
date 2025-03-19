'''
Site Downloader - program polegający na pobieraniu zawartości strony internetowej za pomocą urllib.request do pliku .html.
'''

import tkinter as tk
import urllib.request as req

def create_window():
    root = tk.Tk()
    root.title("site downloader")
    root.geometry("400x300")

    # Display
    url_label = tk.Label(root, text="url")
    url_label.grid(row=0, column=0)
    display = tk.Entry(root, width=40, borderwidth=5)
    display.grid(row=1, column=0, columnspan=5)

    # Display2
    path_label = tk.Label(root, text="path")
    path_label.grid(row=2, column=0)
    display2 = tk.Entry(root, width=40, borderwidth=5)
    display2.grid(row=3, column=0, columnspan=5)

    # Logic for buttons
    def click_button():
        url = display.get()
        file = display2.get()
        req.urlretrieve(url, file)
        display.delete(0, tk.END)
        display2.delete(0, tk.END)
        display.insert(0, "Downloaded")

    # Buttons
    buttons = [
        ('Download', click_button)
    ]

    row = 4
    col = 0
    for (text, command) in buttons:
        tk.Button(root, text=text, width=10, command=command).grid(row=row, column=col)
        col += 1
        if col > 4:
            col = 0
            row += 1

    root.mainloop()

create_window()
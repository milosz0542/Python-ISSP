import tkinter as tk

def submit_data():
    print(f"Name: {name.get()}")
    print(f"Album Number: {album_number.get()}")
    print(f"Password: {password.get()}")

def create_form():
    global name, album_number, password

    root = tk.Tk()
    root.title("Form")
    root.geometry("300x200")

    tk.Label(root, text="Name").grid(row=0, column=0)
    tk.Label(root, text="Album Number").grid(row=1, column=0)
    tk.Label(root, text="Password").grid(row=2, column=0)

    name = tk.Entry(root)
    album_number = tk.Entry(root)
    password = tk.Entry(root, show="*")

    name.grid(row=0, column=1)
    album_number.grid(row=1, column=1)
    password.grid(row=2, column=1)

    submit_button = tk.Button(root, text="Submit", command=submit_data)
    submit_button.grid(row=3, column=1)

    root.mainloop()

create_form()
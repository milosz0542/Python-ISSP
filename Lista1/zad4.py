import tkinter as tk
import math

def create_calculator():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x300")

    # Display
    display = tk.Entry(root, width=20, borderwidth=5)
    display.grid(row=0, column=0, columnspan=5)

    # Logic for buttons
    def click_button(button):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current + button)

    def clear_display():
        display.delete(0, tk.END)

    def calculate():
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    def calculate_function(func):
        try:
            current = display.get()
            result = str(func(float(current)))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    # Buttons
    buttons = [
        ('7', lambda: click_button('7')), ('8', lambda: click_button('8')), ('9', lambda: click_button('9')), ('/', lambda: click_button('/')), ('sinh', lambda: calculate_function(math.sinh)),
        ('4', lambda: click_button('4')), ('5', lambda: click_button('5')), ('6', lambda: click_button('6')), ('*', lambda: click_button('*')), ('cosh', lambda: calculate_function(math.cosh)),
        ('1', lambda: click_button('1')), ('2', lambda: click_button('2')), ('3', lambda: click_button('3')), ('-', lambda: click_button('-')), ('tanh', lambda: calculate_function(math.tanh)),
        ('C', clear_display), ('0', lambda: click_button('0')), ('=', calculate), ('+', lambda: click_button('+')), ('coth', lambda: calculate_function(lambda x: 1 / math.tanh(x))),
        ('ln', lambda: calculate_function(math.log)), ('log', lambda: calculate_function(math.log10)), ('sqrt', lambda: calculate_function(math.sqrt)), ('pow', lambda: click_button('**')),
        ('sin', lambda: calculate_function(math.sin)), ('cos', lambda: calculate_function(math.cos)), ('tan', lambda: calculate_function(math.tan)), ('cot', lambda: calculate_function(lambda x: 1 / math.tan(x))),
        ('(', lambda: click_button('(')), (')', lambda: click_button(')')), ('pi', lambda: click_button(str(math.pi))), ('e', lambda: click_button(str(math.e)))
    ]

    row = 1
    col = 0
    for (text, command) in buttons:
        tk.Button(root, text=text, width=5, command=command).grid(row=row, column=col)
        col += 1
        if col > 4:
            col = 0
            row += 1

    root.mainloop()

create_calculator()
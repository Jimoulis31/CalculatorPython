from tkinter import *

window = Tk()
window.title("Calculator made by Mitsos")
window.geometry('600x500')
window.configure(bg="#1e1e1e")

equation = StringVar()
result = ""

def press(num):
    global result
    result += str(num)
    equation.set(result)

def clear():
    global result
    result = ""
    equation.set("")

def equalpress():
    global result
    try:
        total = str(eval(result))
        equation.set(total)
        result = ""
    except:
        equation.set("Error")
        result = ""

txt = Entry(window, textvariable=equation, font=("Arial", 24), bd=5, relief=RIDGE, justify=RIGHT)
txt.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

button_style = {"font": ("Arial", 18), "bd": 3, "relief": RAISED, "bg": "#ff9999", "fg": "#000"}

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('.', 5, 0), ('(', 5, 1), (')', 5, 2), ('**', 5, 3)
]

for (text, row, col) in buttons:
    if text == "C":
        btn = Button(window, text=text, command=clear, **button_style)
    elif text == "=":
        btn = Button(window, text=text, command=equalpress, **button_style)
    else:
        btn = Button(window, text=text, command=lambda t=text: press(t), **button_style)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)






window.mainloop()

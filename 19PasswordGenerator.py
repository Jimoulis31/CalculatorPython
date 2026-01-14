import tkinter as tk
from tkinter import StringVar, ttk
import random
import datetime

window = tk.Tk()
window.title("Password Generator by Mitsos")
window.geometry("750x500")
window.configure(bg="#1e1e1e")
window.resizable(False, False)

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
PasswordLength = ["6","8","10","12","14","16","18","20"]
Password = StringVar()
x = datetime.datetime.now()
key = (x.day + x.month) * 3

def encryption():
    NewPass = ""
    for char in Password.get():
        position = digits.index(char)
        NewPass += digits[(position + key) % len(digits)]
    EncryptEntry.config(state="normal")
    EncryptEntry.delete(0, tk.END)
    EncryptEntry.insert(0, NewPass)
    EncryptEntry.config(state="readonly")

def decryption():
    NewPass = ""
    for char in EncryptEntry.get():
        position = digits.index(char)
        NewPass += digits[(position - key) % len(digits)]
    EncryptEntry.config(state="normal")
    EncryptEntry.delete(0, tk.END)
    EncryptEntry.insert(0, NewPass)
    EncryptEntry.config(state="readonly")

def generate(*args):
    length = int(LengthBox.get())
    strength = diff.get()
    password = ""
    if strength=="Low":
        password = ''.join(random.choice(lower) for _ in range(length))
    elif strength=="Medium":
        password = ''.join(random.choice(upper) for _ in range(length))
    else:
        password = ''.join(random.choice(digits) for _ in range(length))
    Password.set(password)

def copy_to_clipboard(entry_widget):
    window.clipboard_clear()
    window.clipboard_append(entry_widget.get())

def on_enter(e):
    e.widget['background'] = "#ff9999"
def on_leave(e):
    e.widget['background'] = "#ff6666"

label_font = ("Arial", 16, "bold")
entry_font = ("Arial", 14)
button_font = ("Arial", 14, "bold")


title = tk.Label(window, text="Password Generator", font=("Arial", 28, "bold"), bg="#1e1e1e", fg="#ffffff")
title.pack(pady=20)

pass_frame = tk.Frame(window, bg="#1e1e1e")
pass_frame.pack(pady=10, fill="x", padx=50)

tk.Label(pass_frame, text="Password:", font=label_font, bg="#1e1e1e", fg="#ffffff").grid(row=0, column=0, sticky="w")
PassEntry = tk.Entry(pass_frame, textvariable=Password, font=entry_font, state="readonly", bd=0, relief="solid", width=30)
PassEntry.grid(row=1, column=0, pady=5, padx=(0,10))
Copy1 = tk.Button(pass_frame, text="Copy", font=button_font, bg="#ff6666", fg="#000", width=12, command=lambda: copy_to_clipboard(PassEntry))
Copy1.grid(row=1, column=1, padx=5)
Copy1.bind("<Enter>", on_enter)
Copy1.bind("<Leave>", on_leave)

Generate = tk.Button(pass_frame, text="Generate", font=button_font, bg="#ff6666", fg="#000", width=12, command=generate)
Generate.grid(row=1, column=2, padx=5)
Generate.bind("<Enter>", on_enter)
Generate.bind("<Leave>", on_leave)

options_frame = tk.Frame(window, bg="#1e1e1e")
options_frame.pack(pady=10, fill="x", padx=50)

tk.Label(options_frame, text="Length:", font=label_font, bg="#1e1e1e", fg="#ffffff").grid(row=0, column=0, sticky="w")
LengthBox = ttk.Combobox(options_frame, values=PasswordLength, font=entry_font, width=5)
LengthBox.set("12")
LengthBox.grid(row=0, column=1, padx=10, sticky="w")

diff = StringVar()
diff.set("Strong")
tk.Label(options_frame, text="Strength:", font=label_font, bg="#1e1e1e", fg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
rad1 = tk.Radiobutton(options_frame, text="Low", variable=diff, value="Low", bg="#1e1e1e", fg="#ffffff", selectcolor="#333333", font=entry_font)
rad2 = tk.Radiobutton(options_frame, text="Medium", variable=diff, value="Medium", bg="#1e1e1e", fg="#ffffff", selectcolor="#333333", font=entry_font)
rad3 = tk.Radiobutton(options_frame, text="Strong", variable=diff, value="Strong", bg="#1e1e1e", fg="#ffffff", selectcolor="#333333", font=entry_font)
rad1.grid(row=1, column=1, sticky="w")
rad2.grid(row=1, column=2, sticky="w")
rad3.grid(row=1, column=3, sticky="w")

encrypt_frame = tk.Frame(window, bg="#1e1e1e")
encrypt_frame.pack(pady=20, fill="x", padx=50)

tk.Label(encrypt_frame, text="Encrypted Password:", font=label_font, bg="#1e1e1e", fg="#ffffff").grid(row=0, column=0, sticky="w")
EncryptEntry = tk.Entry(encrypt_frame, font=entry_font, state="readonly", bd=0, relief="solid", width=30)
EncryptEntry.grid(row=1, column=0, pady=5, padx=(0,10))

Copy2 = tk.Button(encrypt_frame, text="Copy", font=button_font, bg="#ff6666", fg="#000", width=12, command=lambda: copy_to_clipboard(EncryptEntry))
Copy2.grid(row=1, column=1, padx=5)
Copy2.bind("<Enter>", on_enter)
Copy2.bind("<Leave>", on_leave)

EncryptBut = tk.Button(encrypt_frame, text="Encrypt", font=button_font, bg="#ff6666", fg="#000", width=12, command=encryption)
EncryptBut.grid(row=1, column=2, padx=5)
EncryptBut.bind("<Enter>", on_enter)
EncryptBut.bind("<Leave>", on_leave)

DecryptBut = tk.Button(encrypt_frame, text="Decrypt", font=button_font, bg="#ff6666", fg="#000", width=12, command=decryption)
DecryptBut.grid(row=2, column=0, pady=10, sticky="w")
DecryptBut.bind("<Enter>", on_enter)
DecryptBut.bind("<Leave>", on_leave)

footer = tk.Label(window, text="Made by Mitsos", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#ff9999")
footer.pack(side="bottom" , pady=20)

window.mainloop()
